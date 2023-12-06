from tkinter import *
import customtkinter as ctk
import math
import time
from configurator import *
import fr_winner
import fr_loser
from PIL import Image, ImageTk

class AppForCanvas(ctk.CTk):
    width_max = 900
    height_max = 600

    ennemi1 = None
    ennemi2 = None
    ennemi3 = None

    def __init__(self, map,  *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.title("Catapulte")
        self.fr = ctk.CTkFrame(self)
        self.fr.pack()
        self.can = MyCanvas(self, self.fr, width=AppForCanvas.width_max, height=AppForCanvas.height_max, bg='white' )
        self.can.pack()
        
        self.image_principal = Image.open("Projet-info-main/images/angry.jpg")
        self.image_principal.thumbnail((900,600))
        self.photo_angry= ImageTk.PhotoImage(master = self.can, image = self.image_principal)
        self.image_widget_principal = self.can.create_image(AppForCanvas.width_max/2, AppForCanvas.height_max/2, anchor = 'center', image = self.photo_angry)

        #permet de savoir on est ds quel map
        self.map = map
        self.determiner_map()
        self.score_label = ctk.CTkLabel(self, text="Score: 0")
        self.score_label.place(x=300, y=10)

        self.ennemis_positions = [AppForCanvas.ennemi1, AppForCanvas.ennemi2, AppForCanvas.ennemi3]
        self.ennemis_a_tuer = len(self.ennemis_positions)
        self.score = 0
        self.niveau = 1

        # Initialiser une liste vide pour stocker les ennemis
        self.ennemis = []

        self.temps_label = ctk.CTkLabel(self, text="Temps écoulé: 0")
        self.temps_label.place(x=300, y=40)
        self.ball_count_label = ctk.CTkLabel(self, text="Boules lancées: 0")
        self.ball_count_label.place(x=300, y=70)  # Adjust the coordinates as needed

        self.temps_debut = None
        self.temps_fin_niveau = None  # Ajout de la variable pour stocker le temps de fin du niveau
        self.temps_after_id = None  # Ajout de l'ID du timer
  
        self.generer_ennemis_fixes()# Générer les ennemis initiaux
        self.generer_obstacles()
        self.generer_cata()
        self.mise_a_jour_temps()  # Appel initial pour lancer le timer
        

    def determiner_map(self):
        # on vérifie pas la map 1 
        if self.map == 'carte 1':
            AppForCanvas.ennemi1, AppForCanvas.ennemi2, AppForCanvas.ennemi3 = (850, 350) , (750, 450), (650, 550)
            update("map_actuelle", 1)

        elif self.map == 'carte 2':
            AppForCanvas.ennemi1, AppForCanvas.ennemi2, AppForCanvas.ennemi3 = (850, 300) , (650, 350), (450, 300)
            update("map_actuelle", 2)

        else :
            AppForCanvas.ennemi1, AppForCanvas.ennemi2, AppForCanvas.ennemi3 =(850, 350) , (750, 450), (650, 550)
            update("map_actuelle", 3)

    def generer_cata(self):
        self.can.create_cata()

    def generer_ennemis_fixes(self):
        self.temps_debut = time.time()  # Démarre le chronomètre lorsque les ennemis sont générés

        # Générer exactement 3 ennemis
        for i in range(self.ennemis_a_tuer):
            position = self.ennemis_positions[i]
            posx_ennemi, posy_ennemi = position
            ennemi = self.can.create_ennemi(posx_ennemi, posy_ennemi)
            self.ennemis.append(ennemi)

    def generer_obstacles(self):
        if self.map == 'carte 1' :
            for i in range(self.ennemis_a_tuer):
                position = self.ennemis_positions[i]
                posx_ennemi, posy_ennemi = position
                self.can.create_obstacle(posx_ennemi-50,posy_ennemi + 21 ,posx_ennemi+50, 600,'brown')

        if self.map == 'carte 2':
            self.can.create_obstacle1()
        
        if self.map == 'carte 3' :
            for i in range(self.ennemis_a_tuer):
                position = self.ennemis_positions[i]
                posx_ennemi, posy_ennemi = position
                self.can.create_obstacle(posx_ennemi-50,posy_ennemi + 21 ,posx_ennemi+50, 600,'brown')
                self.can.create_obstacle(posx_ennemi-50,posy_ennemi -50 ,posx_ennemi-45, posy_ennemi + 21,'brown')
                self.can.create_obstacle(posx_ennemi+45,posy_ennemi -50 ,posx_ennemi+50, posy_ennemi + 21,'brown')
        #support du catapulte
        self.can.create_obstacle(0,550 ,100, 600,'pink')
        
    def check_time_limit(self):
        if self.temps_debut is not None:
            temps_ecoule = int(time.time() - self.temps_debut)
            if temps_ecoule >= 60:  # Check if the time limit (5 seconds) is exceeded
                MyCanvas.in_game = False
                self.arreter_timer()  # Stop the timer
                self.withdraw()
                self.can.unbind("<Motion>") 
                fr_loser.afficher_loser() # Show the lose window
       
    
    def mise_a_jour_temps(self):
        if self.temps_debut is not None:
            temps_ecoule = int(time.time() - self.temps_debut)
            self.temps_label.configure(text=f"Temps écoulé: {temps_ecoule} secondes")
            self.ball_count_label.configure(text=f"Boules lancées: {self.can.ball_counter}")
            #self.can.save_ball_counter(self.can.ball_counter)
            
            if self.score < self.ennemis_a_tuer:
                # Continuer à mettre à jour le temps tant que le score est inférieur au nombre d'ennemis à tuer
                self.temps_after_id = self.after(1000, self.mise_a_jour_temps)
                 # Check if the time limit has been exceeded
                self.check_time_limit()
            elif self.temps_fin_niveau is None:
                # Niveau terminé, enregistrer le temps de fin
                self.temps_fin_niveau = time.time() -self.temps_debut

    def arreter_timer(self):
        # Arrêter le timer s'il est en cours
        if self.temps_after_id is not None:
            self.after_cancel(self.temps_after_id)
    
    def afficher_win(self):
        self.withdraw()  # Masquer la fenêtre principale
        fr_winner.afficher_win()
class MyCanvas(ctk.CTkCanvas):
    def __init__(self, root, *args, **kwargs):
        ctk.CTkCanvas.__init__(self, *args, **kwargs)
        self.root = root
        
        self.catapulte_x, self.catapulte_y = 50, 550
        self.catapulte_tension = 0
        self.boule_x, self.boule_y = self.catapulte_x, self.catapulte_y
        self.tension = None
        self.angle = 0
        self.vitesse = 0
        self.trajectoire_ligne = None
        self.trajectoire_points = []
        self.boule = None
        self.ball_counter = 0  # Initialize the ball counter

        self.bind("<Button-1>", self.tendre_catapulte)
        self.bind("<ButtonRelease-1>", self.tirer_boule)
        self.bind("<Motion>", self.trace_trajectoire)
    #def save_ball_counter(self,nb_boules_value) : 
     #   update("nb_boules",nb_boules_value.get())
      #  print("nb_boules",nb_boules_value.get())
        
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

            # Calcul trajectoire
            angle_radians = math.atan2(self.catapulte_y - event.y, event.x - self.catapulte_x)
            self.angle = (math.degrees(angle_radians) + 360) % 360 - 180

            distance = math.sqrt((event.x - self.catapulte_x) ** 2 + (self.catapulte_y - event.y) ** 2)

            # Calcul vitesse
            elasticite = get_data("elasticite")
            self.vitesse = (distance / 10) * elasticite
            self.boule_x = self.catapulte_x
            self.boule_y = self.catapulte_y - 50
            self.boule = self.create_boule(self.boule_x, self.boule_y)

            # Increment the ball counter
            self.ball_counter += 1
            #print(f"Ball Count: {self.ball_counter}")
        self.bouger_boule()
       
    def bouger_boule(self):
        rayon = get_data("taille") * 2  # Rayon de la boule
        temps_interval = 0.05  # Intervalle de temps entre chaque déplacement
        temps_total = 0
        coefficient_restitution = 0.8  # Coefficient de restitution pour simuler le rebond
        gravite = 9.81
        while True:
            self.boule_x += self.vitesse * math.cos(math.radians(self.angle))
            self.boule_y -= self.vitesse * math.sin(math.radians(self.angle)) - 0.5 * gravite * temps_total ** 2
            # Vérifier la collision avec le sol
            if self.boule_y + rayon > self.winfo_height():
                self.vitesse *= coefficient_restitution  # Réduire la vitesse avec une perte d'énergie
                self.boule_y = self.winfo_height() - rayon  # Ajuster la position pour éviter le chevauchement
                temps_total = 0  # Réinitialiser le temps après le rebond
            self.coords(self.boule, self.boule_x - rayon, self.boule_y - rayon, self.boule_x + rayon, self.boule_y + rayon)
            self.update()
            time.sleep(temps_interval)
            temps_total += temps_interval
            # Vérifier la collision avec les ennemis
            
            boule_bbox = self.bbox(self.boule)
            if boule_bbox:
                ennemis_a_supprimer = []
                for ennemi in self.root.ennemis:
                    ennemi_bbox = self.bbox(ennemi[0])
                    if ennemi_bbox and boule_bbox[2] >= ennemi_bbox[0] and boule_bbox[0] <= ennemi_bbox[2] and \
                            boule_bbox[3] >= ennemi_bbox[1] and boule_bbox[1] <= ennemi_bbox[3]:
                        ennemi[7] -= get_data("poids")*0.1
                        #mise à jour de la barre des vies                    

                        x0, y0, x1, y1 = self.bbox(ennemi[6])
                        vie_totale = x1 - x0
                        nv_vie = vie_totale * ennemi[7]
                        self.coords(ennemi[6], x0, y0, (x0 + nv_vie) , y1)
                        if ennemi[7] <= 0:
                            self.delete(ennemi[0])
                            self.delete(ennemi[1])
                            self.delete(ennemi[2])
                            self.delete(ennemi[3])
                            self.delete(ennemi[4])
                            self.delete(ennemi[5])
                            self.delete(ennemi[6])
                            ennemis_a_supprimer.append(ennemi)
                            self.delete(self.boule)
                            self.root.score += 1
                            self.root.score_label.configure(text=f"Score: {self.root.score}")
                        else:
                            self.delete(self.boule)
                for obstacle in self.find_withtag('obstacle'):
                    obstacle_bbox = self.bbox(obstacle)
                    if obstacle_bbox and boule_bbox[2] >= obstacle_bbox[0] and boule_bbox[0] <= obstacle_bbox[2] and \
                            boule_bbox[3] >= obstacle_bbox[1] and boule_bbox[1] <= obstacle_bbox[3]:
                        # Supprimer la boule si elle heurte un obstacle
                        self.delete(self.boule)
                        return  # Quitter la fonction pour arrêter tout mouvement ultérieur de la boule
                for obstacle in self.find_withtag('obstacle1'):
                    obstacle_bbox = self.bbox(obstacle)
                    if obstacle_bbox and boule_bbox[2] >= obstacle_bbox[0] and boule_bbox[0] <= obstacle_bbox[2] and \
                            boule_bbox[3] >= obstacle_bbox[1] and boule_bbox[1] <= obstacle_bbox[3]:
                        # Supprimer la boule si elle heurte un obstacle
                        self.delete(self.boule)
                        return  # Quitter la fonction pour arrêter tout mouvement ultérieur de la boule
                for ennemi in ennemis_a_supprimer:
                    self.root.ennemis.remove(ennemi)
            
            if self.root.score >= self.root.ennemis_a_tuer:
                self.root.niveau += 1
                self.root.score_label.configure(text=f"Passer au niveau {self.root.niveau}")
                self.root.temps_label.configure(text="Niveau terminé! Cliquez sur 'Niveau Suivant'.")
                self.root.afficher_win()
        
    def trace_trajectoire(self, event):
        if self.catapulte_tension:
            self.trajectoire_points = [self.catapulte_x, self.catapulte_y - 50, event.x, event.y]
            self.coords(self.tension, self.trajectoire_points)


    def create_ennemi(self, x, y):
        ennemi = self.create_oval(x - 15, y - 40, x + 15, y, fill='green')
        tete = self.create_oval(x - 10, y - 40, x + 10, y - 20, fill='red')
        bras_gauche = self.create_line(x - 10, y - 30, x - 20, y - 10, fill='brown', width=2)
        bras_droit = self.create_line(x + 10, y - 30, x + 20, y - 10, fill='brown', width=2)
        jambe_gauche = self.create_line(x - 10, y-3, x - 10, y + 20, fill='brown', width=2)
        jambe_droite = self.create_line(x + 10, y-3, x + 10, y + 20, fill='brown', width=2)
        vie_rectangle = self.create_rectangle(x - 20, y - 50, x + 20, y - 45, fill='red')
        vie_ennemi = 1.0
        
        return [ennemi, tete,  bras_gauche, bras_droit, jambe_gauche, jambe_droite, vie_rectangle, vie_ennemi]

    def create_obstacle(self , x ,y,x1 ,y1, color):
        obstacle = self.create_rectangle(x , y  , x1 , y1  , fill=color,tags='obstacle')
        return obstacle
    def create_obstacle2(self , x ,y,x1 ,y1, color):
        obstacle = self.create_rectangle(x , y  , x1 , y1  , fill=color,tags='obstacle2')
        obstacle1 = self.create_rectangle(x , y  , x1 , y1  , fill=color,tags='obstacle2')
        obstacle2 = self.create_rectangle(x , y  , x1 , y1  , fill=color,tags='obstacle2')
        return obstacle , obstacle1, obstacle2
    
    def create_obstacle1(self):
        obstacle1 = self.create_polygon(900,600,
                                        425,600,
                                        425,325,
                                        475,325,
                                        475,245,
                                        425,245,
                                        425,225,
                                        457,200,
                                        500,225,
                                        500,372,
                                        825,372,
                                        825,325,
                                        875,325,
                                        875,245,
                                        825,245,
                                        825,220,
                                        857,200,
                                        900,220,
                                        900,600,
                                        fill='grey')
        obs = self.create_line(500, 372,825,372 , fill="black", width=1,tags='obstacle1')
        obs1 = self.create_line(425,600,425,325, fill="black", width=1,tags='obstacle1')
        obs7 = self.create_line(425,325,475,325, fill="black", width=1,tags='obstacle1')
        obs8 = self.create_line(475,325,475,245, fill="black", width=1,tags='obstacle1')
        
        

        obs2 = self.create_line( 425,245, 425,225, fill="black", width=1,tags='obstacle1')
        obs3 = self.create_line(825,372, 825,325, fill="black", width=1,tags='obstacle1')
        obs4 = self.create_line(825,245,825,220, fill="black", width=1,tags='obstacle1')
        obs5 = self.create_line( 425,225, 457,200,fill="black", width=1,tags='obstacle1')
        obs6 = self.create_line(825,220,857,200, fill="black", width=1,tags='obstacle1')
        
        return obstacle1,obs,obs1,obs2 , obs3 , obs4 , obs5 , obs6 , obs7 ,obs8
    
    def create_cata(self):
        
        catapulte = self.create_polygon(self.catapulte_x - 4, self.catapulte_y,
                                        self.catapulte_x - 4, self.catapulte_y-45,
                                        self.catapulte_x - 20, self.catapulte_y-65,
                                        self.catapulte_x - 12, self.catapulte_y-65,
                                        self.catapulte_x , self.catapulte_y-50,
                                        self.catapulte_x +12 , self.catapulte_y-65,
                                        self.catapulte_x +20, self.catapulte_y-65,
                                        self.catapulte_x + 4, self.catapulte_y-45,   
                                        self.catapulte_x +4, self.catapulte_y ,
                                        fill='brown')
        return catapulte

    def create_boule(self, x, y):
        couleur = get_data("couleur")
        if couleur == 0 :
            color ='red'
        if couleur == 1 :
            color = 'blue'
        if couleur == 2 :
            color = 'pink'
        rayon = get_data("taille") * 2  # Rayon de la boule
        boule = self.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, fill=color)
        return boule

if __name__ == "__main__":
    root = AppForCanvas("carte 1")
    root.mainloop()