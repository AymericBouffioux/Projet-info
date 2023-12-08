from tkinter import *
import customtkinter as ctk
import time
import animation
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
        self.title("Angry Balls")
        self.fr = ctk.CTkFrame(self)
        self.fr.pack()
        self.can = animation.MyCanvas(self, self.fr, width=AppForCanvas.width_max, height=AppForCanvas.height_max, bg='white' )
        self.can.pack()
        
        self.image_principal = Image.open("Projet-info-main/images/angry.jpg")
        self.image_principal.thumbnail((900,700))
        self.photo_angry= ImageTk.PhotoImage(master = self.can, image = self.image_principal)
        self.image_widget_principal = self.can.create_image(AppForCanvas.width_max/2, AppForCanvas.height_max/2 +30, anchor = 'center', image = self.photo_angry)
        self.niveau = None          # Initialize the level
        
        self.map = map              #permet de savoir on est dans quel map
        self.determiner_map()
        self.score_label = ctk.CTkLabel(self.can, text="Score: 0", fg_color='lightgreen', text_color = ("black", "black"))
        self.score_label.place(x=450, y=10)

        self.ennemis_positions = [AppForCanvas.ennemi1, AppForCanvas.ennemi2, AppForCanvas.ennemi3]
        self.ennemis_a_tuer = len(self.ennemis_positions)
        self.score = 0          # Initialize the score
        

        self.level_label = ctk.CTkLabel(self.can, text="Niveau: Actuel",  fg_color='#FF6666', text_color = ("black", "black"))
        self.level_label.place(x=250, y=10)  # Adjust the coordinates as needed

        self.ball_counter = 0  # Initialize the ball counter


        # Initialiser une liste vide pour stocker les ennemis
        self.ennemis = []
        
        self.temps_label = ctk.CTkLabel(self.can, text="Temps restant: 60", fg_color='lightblue', text_color = ("black", "black"))
        self.temps_label.place(x=700, y=10)
        self.ball_count_label = ctk.CTkLabel(self.can, text="Boules lancées: 0",  fg_color='yellow', text_color = ("black", "black"))
        self.ball_count_label.place(x=50, y=10)  # Adjust the coordinates as needed
        self.temps_debut = None
        self.temps_after_id = None  # Ajout de l'ID du timer
  
        self.generer_ennemis_fixes()# Générer les ennemis initiaux
        self.generer_obstacles()
        self.generer_cata()
        self.mise_a_jour_temps()  # Appel initial pour lancer le timer
    
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
            self.can.create_obstacle1()
        
        if self.map == 'carte 2' :
            for i in range(self.ennemis_a_tuer):
                position = self.ennemis_positions[i]
                posx_ennemi, posy_ennemi = position
                self.can.create_obstacle(posx_ennemi-50,posy_ennemi + 21 ,posx_ennemi+50, 600,'#966F33')
                self.can.create_obstacle(posx_ennemi-50,posy_ennemi -30 ,posx_ennemi-45, posy_ennemi + 21,'#C0C0C0')
        
    def check_time_limit(self):
        if self.temps_debut is not None:
            temps_ecoule = int(time.time() - self.temps_debut)
            if temps_ecoule >= 60:  # Check if the time limit (5 seconds) is exceeded
                animation.MyCanvas.in_game = False
                self.arreter_timer()  # Stop the timer
                self.withdraw()
                self.can.unbind("<Motion>") 
                fr_loser.afficher_loser() # Show the lose window
       
    
    def mise_a_jour_temps(self):

        if self.temps_debut is not None:
            temps_ecoule = int(time.time() - self.temps_debut)
            temps_restant = 60 - temps_ecoule
            self.temps_label.configure(text=f"Temps restant: {temps_restant} secondes")
            self.level_label.configure(text=f"Niveau : {self.niveau} ")
            
            if self.score < self.ennemis_a_tuer:
                # Continuer à mettre à jour le temps tant que le score est inférieur au nombre d'ennemis à tuer
                self.temps_after_id = self.after(1000,self.mise_a_jour_temps)
                 # Check if the time limit has been exceeded
                self.check_time_limit()
            

    def arreter_timer(self):
        # Arrêter le timer s'il est en cours
        if self.temps_after_id is not None:
            self.after_cancel(self.temps_after_id)
    
    def afficher_win(self):
        self.withdraw()  # Masquer la fenêtre principale
        fr_winner.afficher_win()



if __name__ == "__main__":
    root = AppForCanvas("carte 3")
    root.mainloop()

# dbloQUER LES NIVEAU AU FUR ET A MESURE