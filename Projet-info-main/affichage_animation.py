from tkinter import *
import customtkinter as ctk
import time
import animation
from configurator import *
import fr_winner
import fr_loser
from PIL import Image, ImageTk

class AppForCanvas(ctk.CTk):
    width_max = 900             # Initialise la hauteur et largeur max
    height_max = 600            

    ennemi1 = None              # Initialise la position des ennemis
    ennemi2 = None 
    ennemi3 = None

    def __init__(self, map,  *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.title("Angry Balls")
        self.fr = ctk.CTkFrame(self)
        self.fr.pack()
        self.can = animation.MyCanvas(self, self.fr, width=AppForCanvas.width_max, height=AppForCanvas.height_max, bg='white' )
        self.can.pack()
        
        self.max_timing = 60        # Initialise temps max de jeu
        self.niveau = None          # Initialise le niveau

        self.image_principal = Image.open("images/angry.jpg")      #mise en place d'un background
        self.image_principal.thumbnail((900,700))
        self.photo_angry= ImageTk.PhotoImage(master = self.can, image = self.image_principal)
        self.image_widget_principal = self.can.create_image(AppForCanvas.width_max/2, AppForCanvas.height_max/2 +30, anchor = 'center', image = self.photo_angry)
        
        
        self.map = map            
        self.determiner_map()        #permet de placer les ennemis en fct de la map

        
        self.score_label = ctk.CTkLabel(self.can, text="Score: 0", fg_color='lightgreen', text_color = ("black", "black"))      #mise en place de tous les labels
        self.score_label.place(x=450, y=10)

        self.level_label = ctk.CTkLabel(self.can, text="Niveau: Actuel",  fg_color='#FF6666', text_color = ("black", "black"))
        self.level_label.place(x=250, y=10) 

        self.temps_label = ctk.CTkLabel(self.can, text="Temps restant: %i" % self.max_timing, fg_color='lightblue', text_color = ("black", "black"))
        self.temps_label.place(x=700, y=10)

        self.ball_count_label = ctk.CTkLabel(self.can, text="Boules lancées: 0",  fg_color='yellow', text_color = ("black", "black"))
        self.ball_count_label.place(x=50, y=10) 

        

        self.score = 0              # Initialise le score
        self.ball_counter = 0       # Initialise le compte des boules lancées

        self.ennemis_positions = [AppForCanvas.ennemi1, AppForCanvas.ennemi2, AppForCanvas.ennemi3]  #place les ennemis
        self.ennemis_a_tuer = len(self.ennemis_positions)
        self.ennemis = []           # Initialiser une liste vide pour stocker les ennemis
        
        self.temps_debut = None 
        self.temps_after_id = None  # Ajout de l'ID du timer
  
        self.generer_ennemis_fixes()    # Générer les ennemis initiaux
        self.generer_obstacles()        # Générer les obstacles en fct du niveau
        self.generer_cata()             # Générer le lance boules
        self.mise_a_jour_temps()        # Appel initial pour lancer le timer
    
    def determiner_map(self):
        if self.map == 'carte 1':
            AppForCanvas.ennemi1, AppForCanvas.ennemi2, AppForCanvas.ennemi3 = (850, 350) , (750, 450), (650, 550)
            update("map_actuelle", 1)
            self.niveau = 1

        elif self.map == 'carte 2':
            AppForCanvas.ennemi1, AppForCanvas.ennemi2, AppForCanvas.ennemi3 =(850, 350) , (750, 450), (650, 550)
            update("map_actuelle", 2)
            self.niveau = 2

        else :
            AppForCanvas.ennemi1, AppForCanvas.ennemi2, AppForCanvas.ennemi3 =(850, 300) , (650, 350), (450, 300)
            update("map_actuelle", 3)
            self.niveau = 3
        

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
                self.can.create_obstacle(posx_ennemi-50,posy_ennemi + 21 ,posx_ennemi+50, 600,'#966F33')

        if self.map == 'carte 3':
            self.can.create_obstacle_lvl_3()
        
        if self.map == 'carte 2' :
            for i in range(self.ennemis_a_tuer):
                position = self.ennemis_positions[i]
                posx_ennemi, posy_ennemi = position
                self.can.create_obstacle(posx_ennemi-50,posy_ennemi + 21 ,posx_ennemi+50, 600,'#966F33')
                self.can.create_obstacle(posx_ennemi-50,posy_ennemi -30 ,posx_ennemi-45, posy_ennemi + 21,'#C0C0C0')
        
    def check_time_limit(self):
        if self.temps_debut is not None:
            temps_ecoule = int(time.time() - self.temps_debut)
            if temps_ecoule >= self.max_timing:                     # Check si le temps max est atteint
                animation.MyCanvas.in_game = False
                self.arreter_timer()                                # Stop le timer
                self.withdraw()
                self.can.unbind("<Motion>") 
                fr_loser.afficher_loser()                           # Show la fenetre loser
       
    
    def mise_a_jour_temps(self): 
        if self.temps_debut is not None:
            temps_ecoule = int(time.time() - self.temps_debut)
            temps_restant = self.max_timing - temps_ecoule
            self.temps_label.configure(text="Temps restant: %i secondes"%(temps_restant))
            self.level_label.configure(text="Niveau : %i "%(self.niveau))
            
            if self.score < self.ennemis_a_tuer :
                self.temps_after_id = self.after(1000,self.mise_a_jour_temps) # Continuer à mettre à jour le temps tant que le score est inférieur au nombre d'ennemis à tuer
                self.check_time_limit()                                       # Check si on a dépassé la limite de temps
            

    def arreter_timer(self):                        # Arrêter le timer s'il est en cours
        if self.temps_after_id is not None:         
            self.after_cancel(self.temps_after_id)
    
    def afficher_win(self):                         #affiche la fenetre win 
        self.destroy()                              # Masquer la fenêtre principale
        fr_winner.afficher_win()



if __name__ == "__main__":
    root = AppForCanvas("carte 3")
    root.mainloop()
