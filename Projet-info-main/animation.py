import tkinter as ctk
import math
import time

class AppForCanvas(ctk.Tk):
    width_max = 900
    height_max = 600

    ennemi1 = (400, 550)
    ennemi2= (500, 550)
    ennemi3= (550, 550)

    def __init__(self, *args, **kwargs):
        ctk.Tk.__init__(self, *args, **kwargs)
        self.title("Catapulte")
        self.fr = ctk.Frame(self)
        self.fr.pack()
        self.can = MyCanvas(self, self.fr, width=AppForCanvas.width_max, height=AppForCanvas.height_max, bg='white')
        self.can.pack()
        
        self.score_label = ctk.Label(self, text="Score: 0")
        self.score_label.place(x=300, y=10)

        self.ennemis_positions = [AppForCanvas.ennemi1, AppForCanvas.ennemi2, AppForCanvas.ennemi3]
        self.ennemis_a_tuer = len(self.ennemis_positions)
        self.score = 0
        self.niveau = 1

        # Initialiser une liste vide pour stocker les ennemis
        self.ennemis = []

        self.temps_label = ctk.Label(self, text="Temps écoulé: 0")
        self.temps_label.place(x=300, y=40)

        self.temps_debut = None
        self.mise_a_jour_temps()

        # Générer les ennemis initiaux
        self.generer_ennemis_fixes()
        self.niveau_suivant_button = ctk.Button(self, text="Niveau Suivant", command=self.niveau_suivant)
        self.niveau_suivant_button.place(x=400, y=10)
        self.niveau_suivant_button["state"] = "disabled"  # Désactiver le bouton au début

        self.temps_after_id = None

    def generer_ennemis_fixes(self):
        self.temps_debut = time.time()  # Démarre le chronomètre lorsque les ennemis sont générés

        # Générer exactement 3 ennemis
        for i in range(self.ennemis_a_tuer):
            position = self.ennemis_positions[i]
            x, y = position
            ennemi = self.can.create_ennemi(x, y)
            self.ennemis.append(ennemi)
    

    def mise_a_jour_temps(self):
        if self.temps_debut is not None:
            temps_ecoule = int(time.time() - self.temps_debut)
            self.temps_label.config(text=f"Temps écoulé: {temps_ecoule} secondes")
            # Stocker l'ID de l'after pour pouvoir l'annuler plus tard
            self.temps_after_id = self.after(1000, self.mise_a_jour_temps) 


    def niveau_suivant(self):
        self.niveau += 1
        self.score = 0
        self.ennemis = []  # Réinitialiser la liste des ennemis
        self.score_label.config(text=f"Score: {self.score}")
        self.temps_label.config(text="Temps écoulé: 0")
        self.generer_ennemis_fixes()  # Générer de nouveaux ennemis pour le niveau suivant
        self.niveau_suivant_button["state"] = "disabled"  # Désactiver le bouton après le passage au niveau suivant
        self.mise_a_jour_temps()  # Redémarrer la mise à jour du temps


class MyCanvas(ctk.Canvas):
    def __init__(self, root, *args, **kwargs):
        ctk.Canvas.__init__(self, *args, **kwargs)
        self.root = root
        self.catapulte_x, self.catapulte_y = 50, 350
        self.catapulte_tension = 0
        self.boule_x, self.boule_y = self.catapulte_x, self.catapulte_y
        self.tension = None
        self.bouger_boule_id = None
        self.angle = None
        self.vitesse = None
        self.trajectoire_ligne = None
        self.trajectoire_points = []

        self.catapulte = self.create_polygon(self.catapulte_x - 15, self.catapulte_y,
                                             self.catapulte_x + 15, self.catapulte_y,
                                             self.catapulte_x, self.catapulte_y - 50,
                                             fill='brown')
        self.boule = None

        self.bind("<Button-1>", self.tendre_catapulte)
        self.bind("<ButtonRelease-1>", self.tirer_boule)
        self.bind("<Motion>", self.trace_trajectoire)

    def tendre_catapulte(self, event):
        if not self.catapulte_tension:
            self.catapulte_tension = 1
            self.tension = self.create_line(self.catapulte_x, self.catapulte_y - 50, event.x, event.y, fill="green", width=3)

    def tirer_boule(self, event=None):
        if self.catapulte_tension:
            self.catapulte_tension = 0
            self.delete(self.tension)
            

            if self.boule:
                self.delete(self.boule)

            angle_radians = math.atan2(self.catapulte_y - event.y, event.x - self.catapulte_x)

            if event.x < self.catapulte_x:
                self.angle = math.degrees(angle_radians) - 180
            else:
                self.angle = math.degrees(angle_radians)

            distance = math.sqrt((event.x - self.catapulte_x) ** 2 + (self.catapulte_y - event.y) ** 2)
            self.vitesse = distance / 10

            self.boule_x = self.catapulte_x
            self.boule_y = self.catapulte_y
            self.boule = self.create_boule(self.boule_x, self.boule_y)

        self.bouger_boule()

    def bouger_boule(self):
        
        rayon = 10  # Rayon de la boule
        self.boule_x += self.vitesse * math.cos(math.radians(self.angle))
        self.boule_y -= self.vitesse * math.sin(math.radians(self.angle))

        # Vérifier la collision avec le bas du canevas
        if self.boule_y + rayon > self.winfo_height():
            # Réduire la vitesse à chaque rebond pour simuler un rebond réaliste
            self.vitesse = -0.8 * self.vitesse
            self.boule_y = self.winfo_height() - rayon  # Ajuster la position pour éviter le chevauchement

            # Ajouter une composante horizontale à l'angle après le rebond
            self.angle = 180 - self.angle

        self.coords(self.boule, self.boule_x - rayon, self.boule_y - rayon, self.boule_x + rayon,
                    self.boule_y + rayon)
        self.bouger_boule_id = self.after(50, self.bouger_boule)

        # Vérifier la collision avec les ennemis
        boule_bbox = self.bbox(self.boule)
        if boule_bbox:
            ennemis_a_supprimer = []
            for ennemi in self.root.ennemis:
                ennemi_bbox = self.bbox(ennemi[0])  # Ennemi[0] est le corps de l'ennemi
                if ennemi_bbox and boule_bbox[2] >= ennemi_bbox[0] and boule_bbox[0] <= ennemi_bbox[2] and \
                        boule_bbox[3] >= ennemi_bbox[1] and boule_bbox[1] <= ennemi_bbox[3]:
                    # Réduire la vie de l'ennemi
                    ennemi[7] -= 0.25

                    # Mettre à jour la couleur de la barre de vie en fonction de la vie restante
                    self.itemconfig(ennemi[6], fill='red' if ennemi[7] <= 0 else 'green')

                    if ennemi[7] <= 0:
                        # Supprimer l'ennemi lorsque sa vie atteint zéro
                        self.delete(ennemi[0])  # Supprimer le corps de l'ennemi
                        self.delete(ennemi[1])  # Supprimer la tête de l'ennemi
                        self.delete(ennemi[2])  # Supprimer le bras gauche
                        self.delete(ennemi[3])  # Supprimer le bras droit
                        self.delete(ennemi[4])  # Supprimer la jambe gauche
                        self.delete(ennemi[5])  # Supprimer la jambe droite
                        self.delete(ennemi[6])  # Supprimer la barre de vie
                        ennemis_a_supprimer.append(ennemi)
                        self.delete(self.boule)
                        self.root.score += 1
                        self.root.score_label.config(text=f"Score: {self.root.score}")
                    else:
                    # Si la balle touche l'ennemi, supprimer la balle
                        self.delete(self.boule)

            for ennemi in ennemis_a_supprimer:
                self.root.ennemis.remove(ennemi)

            if self.root.score >= self.root.ennemis_a_tuer:
                # Le niveau est terminé
                self.root.niveau += 1
                self.root.score_label.config(text=f"Passer au niveau {self.root.niveau}")
                self.root.temps_label.config(text="Niveau terminé! Cliquez sur 'Niveau Suivant'.")
                self.root.niveau_suivant_button["state"] = "normal"  # Activer le bouton 'Niveau Suivant'
                # Annuler la mise à jour du temps
                if self.root.temps_after_id:
                    self.root.after_cancel(self.root.temps_after_id)

    def trace_trajectoire(self, event):
        if self.catapulte_tension:
            self.trajectoire_points = [self.catapulte_x, self.catapulte_y - 50, event.x, event.y]
            self.coords(self.tension, self.trajectoire_points)

    def create_ennemi(self, x, y):
        ennemi = self.create_oval(x - 15, y - 40, x + 15, y, fill='green')
        tete = self.create_oval(x - 10, y - 40, x + 10, y - 20, fill='red')
        bras_gauche = self.create_line(x - 10, y - 30, x - 20, y - 10, fill='brown', width=2)
        bras_droit = self.create_line(x + 10, y - 30, x + 20, y - 10, fill='brown', width=2)
        jambe_gauche = self.create_line(x - 10, y, x - 10, y + 20, fill='brown', width=2)
        jambe_droite = self.create_line(x + 10, y, x + 10, y + 20, fill='brown', width=2)

        vie_rectangle = self.create_rectangle(x - 20, y - 50, x + 20, y - 45, fill='red')
        

        vie_ennemi = 1.0
        return [ennemi, tete, bras_gauche, bras_droit, jambe_gauche, jambe_droite, vie_rectangle, vie_ennemi]

    def create_boule(self, x, y):
        rayon = 10  # Rayon de la boule
        boule = self.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, fill='blue')
        return boule

    

if __name__ == "__main__":
    root = AppForCanvas()
    root.mainloop()