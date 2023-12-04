
from tkinter import BOTH, DoubleVar
from tokenize import Double
import customtkinter as ctk
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
        btn_start = ctk.CTkButton(fr_main, text="Start",height=50, width=100,command=lambda: self.show_frame(fr_main, fr_start))
        btn_start.grid(row=2, column=2)
        btn_help = ctk.CTkButton(fr_main, text="Help",command=lambda: self.show_frame(fr_main, fr_help))
        btn_help.grid(row=3, column=1)
        btn_options = ctk.CTkButton(fr_main, text="Options",command=lambda: self.show_frame(fr_main, fr_options))
        btn_options.grid(row=3, column=3)
        fr_main.pack(fill=BOTH, expand=True)

        # Création page Start
        fr_start = ctk.CTkFrame(self)
        surround_btns_map = ctk.CTkFrame(fr_start, fg_color="#ADD8E6")
        surround_btns_map.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="ew", columnspan=5)

        # Créer les boutons "Map1", "Map2" et "Map3" centrés horizontalement dans le rectangle rose
        btn_map1 = ctk.CTkButton(fr_start, text="Carte 1", command=lambda: self.bouton_clic('Carte 1'))
        btn_map2 = ctk.CTkButton(fr_start, text="Carte 2", command=lambda: self.bouton_clic('Carte 2'))
        btn_map3 = ctk.CTkButton(fr_start, text="Carte 3", command=lambda: self.bouton_clic('Carte 3'))
        btn_map1.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="w")
        btn_map2.grid(row=3, column=2, padx=20, pady=(0, 20), sticky="w")
        btn_map3.grid(row=3, column=4, padx=20, pady=(0, 20), sticky="w")

        # Créer le bouton "Modulation des Boules" en haut à gauche
        btn_ball_modulation = ctk.CTkButton(fr_start, text="Modulation des Boules", command=lambda: self.show_frame(fr_start, fr_modul_boules))
        
        btn_ball_modulation.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")
        # Créer le bouton "Modulation des Catapultes" en haut à droite
        btn_modulation_of_catapult = ctk.CTkButton(fr_start, text="Modulation des Catapultes",  command=lambda: self.show_frame(fr_start, fr_modul_cata))
        
        btn_modulation_of_catapult.grid(row=1, column=3, padx=20, pady=(0, 20), sticky="w")
        # Lancer la boucle principale de l'application
        btn_back = ctk.CTkButton(fr_start, text="Retour page d'acceuil",command=lambda: self.show_frame(fr_start, fr_main))
        btn_back.grid(row=0, column=0)
        
        # Création page Help
        fr_help = ctk.CTkFrame(self)
        btn_back = ctk.CTkButton(fr_help, text="Retour page d'acceuil",command=lambda: self.show_frame(fr_help, fr_main))
        btn_back.grid(row=0, column=0)
        
        lbl_title_help = ctk.CTkLabel(fr_help, text="Règles" , justify="center", font=("Arial",60))
        lbl_title_help.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        lbl_help_rules = ctk.CTkLabel(fr_help,height=200, width=100, text="""
            Règle 1 : Objectif principal : Éliminer tous les ennemis en lançant habilement des boules sur les structures les abritant.
            Règle 2 : Choix stratégique : Sélectionner judicieusement le poids et la taille des boules pour optimiser la réussite du niveau.
            Règle 3 : Précision catapultée : Utiliser la catapulte avec précision pour cibler et atteindre les ennemis.
            Règle 4 : Chronométrage optimal : Terminer le niveau en 7 secondes pour obtenir 3 étoiles, en 12 secondes pour 2 étoiles.
            Règle 5 : Réactivité requise : Assurer un mouvement constant dans les 15 secondes, sinon la partie se termine.
            """ , justify="left", font=("Arial",15))
        lbl_help_rules.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        
        # Création page Options
        fr_options = ctk.CTkFrame(self)
        
        btn_back = ctk.CTkButton(fr_options, text="Retour page d'acceuil",
                                 command=lambda: self.show_frame(fr_options, fr_main))
        btn_back.grid(row=0, column=0)

        # Widget de texte pour afficher le titre
        label_fr_option = ctk.CTkLabel(fr_options, text="Page Option ",fg_color=("#ADD8E6", 'blue'))
        label_fr_option.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        
        # Widget de texte pour afficher le bouton thème

        btn_theme = ctk.CTkButton(fr_options, text="Thème",command=lambda: self.show_frame(fr_options, fr_change_theme))
        btn_theme.grid(row=2, column=0, padx=20, pady=20, sticky="ew")



        # Widget de texte pour afficher le boutopn langues
        btn_language = ctk.CTkButton(fr_options, text="Langues",command=lambda: self.show_frame(fr_options, fr_change_language))
        btn_language.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        
        
        # Créer une fenêtre Change theme
        fr_change_theme = ctk.CTkFrame(self)
        lbl_change_theme = ctk.CTkLabel(fr_change_theme, text="Changer le thème" , justify="center", font=("Arial",20))
        lbl_change_theme.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        
        # Variable de contrôle pour le thème
        self.theme_var = ctk.StringVar(self)
        self.theme_var.set("light") 
        
        # Radiobuttons pour choisir le thème
        light_radio = ctk.CTkRadioButton(fr_change_theme, text="Light / Clair ", variable=self.theme_var, value="light", command=self.set_theme)
        dark_radio = ctk.CTkRadioButton(fr_change_theme, text="Dark / Sombre ", variable=self.theme_var, value="dark", command=self.set_theme)
        light_radio.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        dark_radio.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
          
        btn_back = ctk.CTkButton(fr_change_theme, text="retour",command=lambda: self.show_frame(fr_change_theme, fr_options))
        btn_back.grid(row=1, column=0)
        
        # Créer une fenêtreChange language
        fr_change_language = ctk.CTkFrame(self)
        lbl_change_language = ctk.CTkLabel(fr_change_language, text="Changer la langue" , justify="center", font=("Arial",20))
        lbl_change_language.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
    
        # OptionMenu pour choisir la langue
        language_optionmenu = ctk.CTkOptionMenu(fr_change_language, values=["Français", "English"], command=self.update_language)
        language_optionmenu.set("Français")
        language_optionmenu.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        
        btn_back = ctk.CTkButton(fr_change_language, text="retour",command=lambda: self.show_frame(fr_change_language, fr_options))
        btn_back.grid(row=1, column=0)
        
        # Créer une fenêtre modulation catapulte
        fr_modul_cata = ctk.CTkFrame(self)
        #lbl_modulation_catapult = ctk.CTkLabel(fr_modul_cata, text="Modulation de la catapulte" , justify="center", font=("Arial",20))
        #lbl_modulation_catapult.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        
        self.elasticite_value = DoubleVar(value=2.5) 

        # Widget de texte pour afficher le titre
        lbl_elasticity = ctk.CTkLabel(fr_modul_cata, text="élasticite ",fg_color=("#ADD8E6", 'blue'))
        lbl_elasticity.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        
        # slider pr determiner l'elasticité
        slider_elasticity = ctk.CTkSlider(fr_modul_cata, from_=1, to=5, command=self.slider_event_elasticite)
        slider_elasticity.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
    
    
        # bouton save
        btn_save = ctk.CTkButton(fr_modul_cata, text="sauver", command=lambda: (self.save_elasticite(self.elasticite_value)))
        btn_save.grid(row=1, column=0)
    
        # bouton retour
        btn_retour = ctk.CTkButton(fr_modul_cata, text="Retour à la page Start", command=lambda: self.show_frame(fr_modul_cata, fr_start))
        btn_retour.grid(row=0, column=0)
        
        # Créer une fenêtre modulation boules
        fr_modul_boules = ctk.CTkFrame(self)
        #lbl_modulation_balls = ctk.CTkLabel(fr_modul_boules, text="Modulation des boules" , justify="center", font=("Arial",20))
        #lbl_modulation_balls.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.poids_value = DoubleVar(value=2.5) 
        self.taille_value = DoubleVar(value=2.5)
        self.couleur_value = DoubleVar(value=0)
        
        # Widget de texte pour afficher le titre
        label_poids = ctk.CTkLabel( fr_modul_boules, text="poids",fg_color=("#ADD8E6", 'blue'))
        label_poids.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
    
        # slider pr determiner la taille
        slider_poids = ctk.CTkSlider(fr_modul_boules, from_=1, to=5, command=self.slider_event_taille)
        slider_poids.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
        
        # Widget de texte pour afficher le titre
        label_taille = ctk.CTkLabel(fr_modul_boules, text="taille",fg_color=("#ADD8E6", 'blue'))
        label_taille.grid(row=6, column=0, padx=20, pady=20, sticky="ew")

        # slider pr determiner le poids
        slider_taille= ctk.CTkSlider(fr_modul_boules, from_=2.5, to=7.5, command=self.slider_event_poids)
        slider_taille.grid(row=7, column=0, padx=20, pady=20, sticky="ew")
        
        # Widget de texte pour afficher le titre
        lbl_color = ctk.CTkLabel(fr_modul_boules, text="couleur", fg_color=("#ADD8E6", 'blue'))
        lbl_color.grid(row=8, column=0, padx=20, pady=20, sticky="ew")

        # Bouton pour ouvrir le sélecteur de couleur
        choice_color_optionmenu = ctk.CTkOptionMenu(fr_modul_boules, values=["Rouge", "Bleu", "Rose"], command=self.update_color)
        choice_color_optionmenu.grid(row=9, column=0, padx=20, pady=20, sticky="ew")   

        # bouton retour
        btn_back = ctk.CTkButton(fr_modul_boules, text="Retour à la page Start", command=lambda: self.show_frame(fr_modul_boules, fr_start))
        btn_back.grid(row=0, column=0)


        # bouton save
        btn_Save = ctk.CTkButton(fr_modul_boules, text="sauver",command=lambda: (self.save_poids(self.poids_value), self.save_taille(self.taille_value),self.save_couleur(self.couleur_value)))
        btn_Save.grid(row=1, column=0)

    # Fonctions supplémentaires

    #c'est pr pouvoir afficher fr_start
    def show_fr_start(self):
        # Assurez-vous que fr_start est bien configuré avant de l'afficher
        self.fr_start.pack(fill=BOTH, expand=True)

    # Création showframe
    def show_frame(self, frame_forget, frame_display):
        frame_forget.pack_forget()
        frame_display.pack(fill=BOTH, expand=True)

    def hide_frame(self):
        self.withdraw()
      
# Utilisation de fonctions dans d'autres documents 
    def bouton_clic(self, nom):
        # Accès à animation
        if nom == "Carte 1":
            screen1 = animation.AppForCanvas('carte 1')
            self.hide_frame()
            screen1.mainloop()

        elif nom == "Carte 2":
            screen2 = animation.AppForCanvas('carte 2')
            self.hide_frame()
            screen2.mainloop()

        elif nom == "Carte 3":
            screen3 = animation.AppForCanvas('carte 3')
            self.hide_frame()
            screen3.mainloop()
        #print("Le bouton '%s' a été cliqué" % (nom))
        
    # Fonction pour changer le thème de la fenêtre
    def set_theme(self):
        selected_theme = self.theme_var.get()
        # Change le thème en light mode
        if selected_theme == "light":
            ctk.set_appearance_mode("Light")
        # Change le thème en dark mode
        elif selected_theme == "dark":
            ctk.set_appearance_mode("Dark")

        
    # Fonction pour mettre à jour la langue
    def update_language(self, selected_language):
        print('langue selectionnée', selected_language)
        if selected_language == "Français":
            pass
            
        elif selected_language == "English":
            pass
        
        
    # slider pr determiner l'elasticité
    def slider_event_elasticite(self, value):
        self.elasticite_value.set(value)

    # slider pr determiner la taille
    def slider_event_taille(self, value):
        self.taille_value.set(value)

    # slider pr determiner le poids
    def slider_event_poids(self, value):
        self.poids_value.set(value)
    
    # Update color   
    def update_color(self, selected_color):
        if selected_color == "Rouge":
            couleur = 0
        elif selected_color == "Bleu":
            couleur = 1
        elif selected_color == "Rose":
            couleur = 2
        self.couleur_value.set(couleur)

    # Fonction pour sauvegarder l'élasticité
    def save_elasticite(self, elasticite_value):
        print(f"Elasticite sauvée : {elasticite_value.get()}")
        update("elasticite",elasticite_value.get())
        
    # Fonction pour sauvegarder le poids
    def save_poids(self, poids_value):
        print(f"Poids sauvée : {poids_value.get()}")
        update("poids",poids_value.get())

    # Fonction pour sauvegarder la taille
    def save_taille(self, taille_value):
        print(f"Taille sauvée : {taille_value.get()}")
        update("taille",taille_value.get())

    # Fonction pour sauvegarder la couleur   
    def save_couleur(self, couleur_value):
        print(f"Couleur sauvée : {couleur_value.get()}")
        update("couleur",couleur_value.get())

# Fermeture app   
app = App()
app.mainloop()