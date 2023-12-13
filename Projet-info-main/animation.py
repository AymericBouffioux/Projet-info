from tkinter import *
import customtkinter as ctk
import math
import time
from configurator import *

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

        self.bind("<Button-1>", self.tendre_catapulte)
        self.bind("<ButtonRelease-1>", self.tirer_boule)
        self.bind("<Motion>", self.trace_trajectoire)

    def on_close(self):
        # Function to handle window close event
        if hasattr(self, 'boule') and self.boule:
            self.delete(self.boule)
        self.root.destroy()
        
    def tendre_catapulte(self, event):
        if not self.catapulte_tension:
            self.catapulte_tension = 1
            self.tension = self.create_line(self.catapulte_x, self.catapulte_y - 50, event.x, event.y, fill="black", width=3)

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
            self.vitesse = (distance / 10) * (elasticite/2)
            self.boule_x = self.catapulte_x
            self.boule_y = self.catapulte_y - 50
            self.boule = self.create_boule(self.boule_x, self.boule_y)

            # Increment the ball counter
            self.root.ball_counter += 1
            update("nb_boules", self.root.ball_counter )
            self.root.ball_count_label.configure(text=f"Boules lancées: {self.root.ball_counter}")
        self.bouger_boule()
    
        
    def bouger_boule(self):
        rayon = get_data("taille") * 2  # Rayon de la boule
        temps_interval = 0.05  # Intervalle de temps entre chaque déplacement
        temps_total = 0
        coefficient_restitution = 0.5  # Coefficient de restitution pour simuler le rebond
        gravite = 9.81
        while True:
            self.boule_x += self.vitesse * math.cos(math.radians(self.angle))
            self.boule_y -= self.vitesse * math.sin(math.radians(self.angle)) - 0.5 * gravite * temps_total ** 2
            # Vérifier la collision avec le sol


 
            if self.root.niveau == 3 :
                rebond = self.find_withtag('obstacle2')
                rebond_bbox = self.bbox(rebond)
                if self.boule_y + rayon > rebond_bbox[1] and self.boule_x + rayon > rebond_bbox[0] and self.boule_x + rayon <  rebond_bbox[2] : 
                        self.vitesse *= coefficient_restitution  # Réduire la vitesse avec une perte d'énergie
                        self.boule_y =  rebond_bbox[1]- rayon  # Ajuster la position pour éviter le chevauchement
                        temps_total = 0  # Réinitialiser le temps après le rebond
            

            if self.boule_x + rayon > self.winfo_width():
                self.delete(self.boule)  # Supprimer la boule
                return 
            if self.boule_y + rayon > self.winfo_height():
                self.vitesse *= coefficient_restitution  # Réduire la vitesse avec une perte d'énergie
                self.boule_y = self.winfo_height() - rayon  # Ajuster la position pour éviter le chevauchement
                temps_total = 0  # Réinitialiser le temps après le rebond
            self.coords(self.boule, self.boule_x - rayon, self.boule_y - rayon, self.boule_x + rayon, self.boule_y + rayon)
            self.update()
            time.sleep(temps_interval)
            temps_total += temps_interval

            # Vérifier la collision avec les ennemis si la boule existe
            
            boule_bbox = self.bbox(self.boule)
            if boule_bbox:
                ennemis_a_supprimer = []
                for ennemi in self.root.ennemis:
                    ennemi_bbox = self.bbox(ennemi[0])
                    ennemi_bbox = self.bbox(ennemi[1])
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


    def create_ennemi(self, x, y):#essayer de mettre en place des images 
        ennemi = self.create_oval(x - 15, y - 40, x + 15, y, fill='green')
        tete = self.create_oval(x - 10, y - 40, x + 10, y - 20, fill='red')
        bras_gauche = self.create_line(x - 10, y - 30, x - 20, y - 10, fill='black', width=2)
        bras_droit = self.create_line(x + 10, y - 30, x + 20, y - 10, fill='black', width=2)
        jambe_gauche = self.create_line(x - 10, y-3, x - 10, y + 20, fill='black', width=2)
        jambe_droite = self.create_line(x + 10, y-3, x + 10, y + 20, fill='black', width=2)
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
                                        fill='#808080')
        obs = self.create_line(500, 372,825,372 , fill="black", width=1,tags='obstacle2')
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
                                        fill='#8B4513')
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
    print("Veuillez lancer le fichier afichage_animation si vous voulez tester l'animation")