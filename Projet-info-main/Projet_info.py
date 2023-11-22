
from tkinter import BOTH
import customtkinter as ctk
import fr_modulation
import fr_th_la
import animation
from configurator import *

# Multi fenêtre
class App(ctk.CTk) :

    def __init__(self, *args, **kwargs) :
        ctk.CTk.__init__(self, *args, **kwargs)
        self.title("Angry Balls")
        self.resizable(0,0)
        data_init()
     
# Création page Main
        fr_main = ctk.CTkFrame(self)
        

        btn_start = ctk.CTkButton(fr_main, text="Start",height=50, width=100,
                                  command=lambda: self.show_frame(fr_main, fr_start))
        btn_start.grid(row=2, column=2)
        btn_help = ctk.CTkButton(fr_main, text="Help",
                                  command=lambda: self.show_frame(fr_main, fr_help))
        btn_help.grid(row=3, column=1)
        btn_options = ctk.CTkButton(fr_main, text="Options",
                                  command=lambda: self.show_frame(fr_main, fr_options))
        btn_options.grid(row=3, column=3)
        fr_main.pack(fill=BOTH, expand=True)

# Création page Start
        fr_start = ctk.CTkFrame(self)
        cadre_boutons_map = ctk.CTkFrame(fr_start, fg_color="#ADD8E6")
        cadre_boutons_map.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="ew", columnspan=5)
        # Créer les boutons "Map1", "Map2" et "Map3" centrés horizontalement dans le rectangle rose
        bouton_map1 = ctk.CTkButton(fr_start, text="Carte 1", command=lambda: self.bouton_clic("Carte 1"))
        bouton_map2 = ctk.CTkButton(fr_start, text="Carte 2", command=lambda: self.bouton_clic("Carte 2"))
        bouton_map3 = ctk.CTkButton(fr_start, text="Carte 3", command=lambda: self.bouton_clic("Carte 3"))
        bouton_map1.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="w")
        bouton_map2.grid(row=3, column=2, padx=20, pady=(0, 20), sticky="w")
        bouton_map3.grid(row=3, column=4, padx=20, pady=(0, 20), sticky="w")

        # Créer le bouton "Modulation des Boules" en haut à gauche
        bouton_boules = ctk.CTkButton(fr_start, text="Modulation des Boules", 
                                      command=lambda: self.bouton_clic("Modulation des Boules"))
        # bouton_boules.configure(bg="blue", width=11, height=2)  # Changer la couleur, la largeur et la hauteur du bouton
        bouton_boules.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")
        # Créer le bouton "Modulation des Catapultes" en haut à droite
        bouton_catapultes = ctk.CTkButton(fr_start, text="Modulation des Catapultes", 
                                          command=lambda: self.bouton_clic("Modulation des Catapultes"))
        # bouton_catapultes.configure(bg="red", width=11, height=2)  # Changer la couleur, la largeur et la hauteur du bouton
        bouton_catapultes.grid(row=1, column=3, padx=20, pady=(0, 20), sticky="w")
        # Lancer la boucle principale de l'application
        btn_SM = ctk.CTkButton(fr_start, text="Retour page d'acceuil",
                                 command=lambda: self.show_frame(fr_start, fr_main))
        btn_SM.grid(row=0, column=0)
        
# Création page Help
        fr_help = ctk.CTkFrame(self)
        btn_HM = ctk.CTkButton(fr_help, text="Retour page d'acceuil",
                                 command=lambda: self.show_frame(fr_help, fr_main))
        btn_HM.grid(row=0, column=0)
        
        lbl_title_help = ctk.CTkLabel(fr_help, text="Règles" , justify="center", font=("Arial",60))
        lbl_title_help.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        texte_regles_label = ctk.CTkLabel(fr_help,height=200, width=100, text="""
            Règle 1 : Objectif principal : Éliminer tous les ennemis en lançant habilement des boules sur les structures les abritant.
            Règle 2 : Choix stratégique : Sélectionner judicieusement le poids et la taille des boules pour optimiser la réussite du niveau.
            Règle 3 : Précision catapultée : Utiliser la catapulte avec précision pour cibler et atteindre les ennemis.
            Règle 4 : Chronométrage optimal : Terminer le niveau en 7 secondes pour obtenir 3 étoiles, en 12 secondes pour 2 étoiles.
            Règle 5 : Réactivité requise : Assurer un mouvement constant dans les 15 secondes, sinon la partie se termine.
            """ , justify="left", font=("Arial",15))
        texte_regles_label.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        
# Création page Options
        fr_options = ctk.CTkFrame(self)
        
        btn_OM = ctk.CTkButton(fr_options, text="Retour page d'acceuil",
                                 command=lambda: self.show_frame(fr_options, fr_main))
        btn_OM.grid(row=0, column=0)

        # Widget de texte pour afficher le titre
        text_label = ctk.CTkLabel(fr_options, text="Page Option ",fg_color=("#ADD8E6", 'blue'))
        text_label.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        
        # Widget de texte pour afficher le bouton thème

        text_bouton_th = ctk.CTkButton(fr_options, text="Thème",
                                       command=lambda: self.bouton_clic("Thème"))
        text_bouton_th.grid(row=2, column=0, padx=20, pady=20, sticky="ew")



        # Widget de texte pour afficher le boutopn langues
        text_bouton_th = ctk.CTkButton(fr_options, text="Langues",
                                       command=lambda: self.bouton_clic("Langues"))
        text_bouton_th.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

# Création showframe
    def show_frame(self, frame_forget, frame_display):
        frame_forget.pack_forget()
        frame_display.pack(fill=BOTH, expand=True)
        
# Utilisation de fonctions dans d'autres documents 
    def bouton_clic(self, nom):
        # Accès à fr_modulation
        if nom == "Modulation des Catapultes":
            fr_modulation.create_cata()        
        elif nom == "Modulation des Boules":
            fr_modulation.create_boules()
        # Accès à fr_th_la
        elif nom == "Thème":
            fr_th_la.change_theme()
        elif nom == "Langues":
            fr_th_la.change_language()
        # Accès à animation
        elif nom == "Carte 1":
            
            screen1 = animation.AppForCanvas('carte 1')
            screen1.mainloop()
            #animation.AppForCanvas().mainloop()
        elif nom == "Carte 2":
            screen2 = animation.AppForCanvas('carte 2')
            screen2.mainloop()

        elif nom == "Carte 3":
            screen3 = animation.AppForCanvas('carte 3')
            screen3.mainloop()
            
        print("Le bouton '%s' a été cliqué" % (nom))

     
# Fermeture app   
app = App()
app.mainloop() 