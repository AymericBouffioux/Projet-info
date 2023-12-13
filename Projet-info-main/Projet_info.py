
from tkinter import BOTH, DoubleVar
import customtkinter as ctk
import affichage_animation
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
        self.btn_start = ctk.CTkButton(fr_main, text="Démarer",height=50, width=100,command=lambda: self.show_frame(fr_main, self.fr_start))
        self.btn_start.grid(row=2, column=2)
        self.btn_help = ctk.CTkButton(fr_main, text="Règles",command=lambda: self.show_frame(fr_main, fr_help))
        self.btn_help.grid(row=3, column=1)
        self.btn_options = ctk.CTkButton(fr_main, text="Options",command=lambda: self.show_frame(fr_main, fr_options))
        self.btn_options.grid(row=3, column=3)
        self.btn_quitter = ctk.CTkButton(fr_main, text="Quitter",height=20, width=70,command=lambda:self.quitter(fr_main))
        self.btn_quitter.grid(row=0, column=1)
        fr_main.pack(fill=BOTH, expand=True)

        # Création page Start
        self.fr_start = ctk.CTkFrame(self)
        surround_btns_map = ctk.CTkFrame(self.fr_start, fg_color="#ADD8E6")
        surround_btns_map.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="ew", columnspan=5)

        # Créer les boutons "Map1", "Map2" et "Map3" centrés horizontalement dans le rectangle rose
        self.btn_map1 = ctk.CTkButton(self.fr_start, text="Carte 1", command=lambda: self.bouton_clic('Carte 1'))
        self.btn_map2 = ctk.CTkButton(self.fr_start, text="Carte 2", command=lambda: self.bouton_clic('Carte 2'))
        self.btn_map3 = ctk.CTkButton(self.fr_start, text="Carte 3", command=lambda: self.bouton_clic('Carte 3'))
        self.btn_map1.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="w")
        self.btn_map2.grid(row=3, column=2, padx=20, pady=(0, 20), sticky="w")
        self.btn_map3.grid(row=3, column=4, padx=20, pady=(0, 20), sticky="w")

        # Créer le bouton "Modulation des Boules" en haut à gauche
        self.btn_ball_modulation = ctk.CTkButton(self.fr_start, text="Modulation des Boules", command=lambda: self.show_frame(self.fr_start, fr_modul_boules))
        self.btn_ball_modulation.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")
        
        # Créer le bouton "Modulation des Catapultes" en haut à droite
        self.btn_modulation_of_catapult = ctk.CTkButton(self.fr_start, text="Modulation des Catapultes",  command=lambda: self.show_frame(self.fr_start, fr_modul_cata))
        self.btn_modulation_of_catapult.grid(row=1, column=3, padx=20, pady=(0, 20), sticky="w")
        
        # Lancer la boucle principale de l'application
        self.btn_back_st = ctk.CTkButton(self.fr_start, text="Retour page d'acceuil",command=lambda: self.show_frame(self.fr_start, fr_main))
        self.btn_back_st.grid(row=0, column=0)
        
        # Création page Help
        fr_help = ctk.CTkFrame(self)
        self.btn_back_help = ctk.CTkButton(fr_help, text="Retour page d'acceuil",command=lambda: self.show_frame(fr_help, fr_main))
        self.btn_back_help.grid(row=0, column=0)
        
        self.lbl_title_help = ctk.CTkLabel(fr_help, text="Règles" , justify="center", font=("Arial",60))
        self.lbl_title_help.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.lbl_help_rules = ctk.CTkLabel(fr_help,height=200, width=100, text="""
            Règle 1 : Objectif principal : Éliminer tous les ennemis en lançant habilement des boules dessus.
            Règle 2 : Choix stratégique : Sélectionner judicieusement le poids et la taille des boules pour optimiser la réussite du niveau.
            Règle 3 : Précision catapultée : Utiliser la catapulte avec précision pour cibler et atteindre les ennemis.
            Règle 4 : Chronométrage optimal : Terminer le niveau en le moins de boules possible.
            Règle 5 : Réactivité requise : Terminer le niveau en maximum 60 secondes.
            """ , justify="left", font=("Arial",15))
        self.lbl_help_rules.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        
        # Création page Options
        fr_options = ctk.CTkFrame(self)
        
        self.btn_back_option = ctk.CTkButton(fr_options, text="Retour page d'acceuil",
                                 command=lambda: self.show_frame(fr_options, fr_main))
        self.btn_back_option.grid(row=0, column=0)

        # Widget de texte pour afficher le titre
        self.label_fr_option = ctk.CTkLabel(fr_options, text="Page Option ")
        self.label_fr_option.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        
        # Widget de texte pour afficher le bouton thème
        self.btn_theme = ctk.CTkButton(fr_options, text="Thème",command=lambda: self.show_frame(fr_options, fr_change_theme))
        self.btn_theme.grid(row=2, column=0, padx=20, pady=20, sticky="ew")


        # Widget de texte pour afficher le boutopn langues
        self.btn_language = ctk.CTkButton(fr_options, text="Langues",command=lambda: self.show_frame(fr_options, fr_change_language))
        self.btn_language.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        
        
        # Créer une fenêtre Change theme
        fr_change_theme = ctk.CTkFrame(self)
        self.lbl_change_theme = ctk.CTkLabel(fr_change_theme, text="Changer le thème" , justify="center", font=("Arial",20))
        self.lbl_change_theme.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        
        # Variable de contrôle pour le thème
        self.theme_var = ctk.StringVar(self)
        self.theme_var.set("light") 
        
        # Radiobuttons pour choisir le thème
        self.light_radio = ctk.CTkRadioButton(fr_change_theme, text="Clair ", variable=self.theme_var, value="light", command=self.set_theme)
        self.dark_radio = ctk.CTkRadioButton(fr_change_theme, text="Sombre ", variable=self.theme_var, value="dark", command=self.set_theme)
        self.light_radio.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        self.dark_radio.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
        
        self.btn_back_opt = ctk.CTkButton(fr_change_theme, text="Retour",command=lambda: self.show_frame(fr_change_theme, fr_options))
        self.btn_back_opt.grid(row=1, column=0)
        
        # Créer une fenêtreChange language
        fr_change_language = ctk.CTkFrame(self)
        self.lbl_change_language = ctk.CTkLabel(fr_change_language, text="Changer la langue" , justify="center", font=("Arial",20))
        self.lbl_change_language.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
    
        # OptionMenu pour choisir la langue
        language_optionmenu = ctk.CTkOptionMenu(fr_change_language, values=["Français", "English"], command=self.update_language)
        language_optionmenu.set("Français")
        language_optionmenu.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        
        self.btn_back_opt = ctk.CTkButton(fr_change_language, text="Retour",command=lambda: self.show_frame(fr_change_language, fr_options))
        self.btn_back_opt.grid(row=1, column=0)
        
        # Créer une fenêtre modulation catapulte
        fr_modul_cata = ctk.CTkFrame(self)        
        self.elasticite_value = DoubleVar(value=2.5) 

        # Widget de texte pour afficher le titre
        self.lbl_elasticity = ctk.CTkLabel(fr_modul_cata, text="Elasticité ")
        self.lbl_elasticity.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        
        # slider pr determiner l'elasticité
        slider_elasticity = ctk.CTkSlider(fr_modul_cata, from_=1, to=2, command=self.slider_event_elasticite)
        slider_elasticity.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
    
    
        # bouton save
        self.btn_save_ela = ctk.CTkButton(fr_modul_cata, text="Sauver", command=lambda: (self.save_elasticite(self.elasticite_value)))
        self.btn_save_ela.grid(row=1, column=0)
    
        # bouton retour
        self.btn_retour_ela = ctk.CTkButton(fr_modul_cata, text="Retour au choix de carte", command=lambda: self.show_frame(fr_modul_cata, self.fr_start))
        self.btn_retour_ela.grid(row=0, column=0)
        
        # Créer une fenêtre modulation boules
        fr_modul_boules = ctk.CTkFrame(self)

        self.poids_value = DoubleVar(value=2.5) 
        self.taille_value = DoubleVar(value=2.5)
        self.couleur_value = DoubleVar(value=0)
        
        # Widget de texte pour afficher le titre
        self.label_taille = ctk.CTkLabel( fr_modul_boules, text="Taille")
        self.label_taille.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
    
        # slider pr determiner la taille
        slider_poids = ctk.CTkSlider(fr_modul_boules, from_=1, to=5, command=self.slider_event_taille)
        slider_poids.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
        
        # Widget de texte pour afficher le titre
        self.label_poids = ctk.CTkLabel(fr_modul_boules, text="Poids")
        self.label_poids.grid(row=6, column=0, padx=20, pady=20, sticky="ew")

        # slider pr determiner le poids
        slider_taille= ctk.CTkSlider(fr_modul_boules, from_=5, to=8, command=self.slider_event_poids)
        slider_taille.grid(row=7, column=0, padx=20, pady=20, sticky="ew")
        
        # Widget de texte pour afficher le titre
        self.lbl_color = ctk.CTkLabel(fr_modul_boules, text="Couleur")
        self.lbl_color.grid(row=8, column=0, padx=20, pady=20, sticky="ew")

        # Bouton pour ouvrir le sélecteur de couleur
        self.choice_color_optionmenu = ctk.CTkOptionMenu(fr_modul_boules, values=["Rouge", "Bleu", "Rose"], command=self.update_color)
        self.choice_color_optionmenu.grid(row=9, column=0, padx=20, pady=20, sticky="ew")   

        # bouton retour
        self.btn_back_boules = ctk.CTkButton(fr_modul_boules, text="Retour au choix de carte", command=lambda: self.show_frame(fr_modul_boules, self.fr_start))
        self.btn_back_boules.grid(row=0, column=0)


        # bouton save
        self.btn_Save_boules = ctk.CTkButton(fr_modul_boules, text="Sauver",command=lambda: (self.save_poids(self.poids_value), self.save_taille(self.taille_value),self.save_couleur(self.couleur_value)))
        self.btn_Save_boules.grid(row=1, column=0)

    
    def quitter(self,frame):        #permet de fermer la fenetre
        frame.quit()
    
    
    def show_fr_start(self):
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
        if nom == "Carte 1" :
            screen1 = affichage_animation.AppForCanvas('carte 1')
            self.destroy()
            screen1.mainloop()

        elif nom == "Carte 2":
            screen2 = affichage_animation.AppForCanvas('carte 2')
            self.destroy()
            screen2.mainloop()

        elif nom == "Carte 3":
            screen3 = affichage_animation.AppForCanvas('carte 3')
            self.destroy()
            screen3.mainloop()
        
    # Fonction pour changer le thème de la fenêtre
    def set_theme(self):
        selected_theme = self.theme_var.get()
        
        if selected_theme == "light":       # Change le thème en light mode
            ctk.set_appearance_mode("Light")
        
        elif selected_theme == "dark":          # Change le thème en dark mode
            ctk.set_appearance_mode("Dark")

   
    # Fonction pour mettre à jour la langue
    def update_language(self, selected_language):
        print('Langue selectionnée', selected_language)
        if selected_language == "Français":
            self.btn_start.configure(text = "Démarrer")
            self.btn_help.configure(text = "Règles")
            self.btn_options.configure(text = "Options")
            self.btn_map1.configure(text = "Carte 1")
            self.btn_map2.configure(text = "Carte 2") 
            self.btn_map3.configure(text = "Carte 3")           
            self.btn_ball_modulation.configure(text = "Modulation des boules")
            self.btn_modulation_of_catapult.configure(text = "Modulation de la catapulte")
            self.btn_back_st.configure(text = "Retour à la page d'acceuil")
            self.btn_back_help.configure(text = "Retour à la page d'acceuil")
            self.btn_back_option.configure(text = "Retour à la page d'acceuil")
            self.lbl_title_help.configure(text = "Règles")
            self.lbl_help_rules.configure(text = """
            Règle 1 : Objectif principal : Éliminer tous les ennemis en lançant habilement des boules dessus.
            Règle 2 : Choix stratégique : Sélectionner judicieusement le poids et la taille des boules pour optimiser la réussite du niveau.
            Règle 3 : Précision catapultée : Utiliser la catapulte avec précision pour cibler et atteindre les ennemis.
            Règle 4 : Chronométrage optimal : Terminer le niveau en le moins de boules possible.
            Règle 5 : Réactivité requise : Terminer le niveau en maximum 60 secondes.
            """)
            self.label_fr_option.configure(text = "Page d'options")
            self.btn_theme.configure(text = "Thème")
            self.lbl_change_theme.configure(text = "Changer le thème")
            self.light_radio.configure(text = "Claire")
            self.dark_radio.configure(text = "Sombre")
            self.btn_back_opt.configure(text = "Retour")
            self.btn_language.configure(text = "Langue")
            self.lbl_change_language.configure(text = "Changer la langue")
            self.lbl_elasticity.configure(text = "Elasticité")
            self.btn_save_ela.configure(text = "Sauver")
            self.btn_retour_ela.configure(text = "Retour au choix de carte")
            self.label_poids.configure(text = "Poids")
            self.label_taille.configure(text = "Taille")
            self.lbl_color.configure(text = "Couleur")
            self.btn_back_boules.configure(text = "Retour au choix de carte")
            self.btn_Save_boules.configure(text = "Sauver")
            self.choice_color_optionmenu.configure(values = ["Rouge", "Bleu", "Rose"])
            
        elif selected_language == "English":
            self.btn_start.configure(text = "Start")
            self.btn_help.configure(text = "Rules")
            self.btn_options.configure(text = "Options")
            self.btn_map1.configure(text = "Map 1")
            self.btn_map2.configure(text = "Map 2") 
            self.btn_map3.configure(text = "Map 3")           
            self.btn_ball_modulation.configure(text = "Balls modulation")
            self.btn_modulation_of_catapult.configure(text = "Catapult modlation")
            self.btn_back_st.configure(text = "Back to home page")
            self.btn_back_help.configure(text = "Back to home page")
            self.btn_back_option.configure(text = "Back to home page")
            self.lbl_title_help.configure(text = "Rules")
            self.lbl_help_rules.configure(text = """
            Rule 1: Main objective: Eliminate all enemies by skillfully throwing balls at them.
            Rule 2: Strategic choice: Wisely select ball weight and size to optimize level success.
            Rule 3: Catapult accuracy: Use the catapult with precision to target and hit enemies.
            Rule 4: Optimum timing: Complete the level in as few balls as possible.
            Rule 5: Reactivity required: Complete the level in a maximum of 60 seconds.
            """)
            self.label_fr_option.configure(text = "Option page")
            self.btn_theme.configure(text = "Theme")
            self.lbl_change_theme.configure(text = "Change Theme")
            self.light_radio.configure(text = "Light")
            self.dark_radio.configure(text = "Dark")
            self.btn_back_opt.configure(text = "Return")
            self.btn_language.configure(text = "Language")
            self.lbl_change_language.configure(text = "Change Language")
            self.lbl_elasticity.configure(text = "Elasticity")
            self.btn_save_ela.configure(text = "Save")
            self.btn_retour_ela.configure(text = "Return to map choice")
            self.label_poids.configure(text = "Weight")
            self.label_taille.configure(text = "Size")
            self.lbl_color.configure(text = "Color")
            self.btn_back_boules.configure(text = "Return to map choice")
            self.btn_Save_boules.configure(text = "Save")
            self.choice_color_optionmenu.configure(values = ["Red", "Blue", "Pink"])
        
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
        couleur = 0
        if selected_color == ("Rouge" or "Red"):
            couleur = 0
        elif selected_color == ("Bleu" or "Blue"):
            couleur = 1
        elif selected_color == ("Rose" or "Pink"):
            couleur = 2
        self.couleur_value.set(couleur)

    # Fonction pour sauvegarder l'élasticité
    def save_elasticite(self, elasticite_value):
        update("elasticite",elasticite_value.get())

        
    # Fonction pour sauvegarder le poids
    def save_poids(self, poids_value):
        update("poids",poids_value.get())


    # Fonction pour sauvegarder la taille
    def save_taille(self, taille_value):
        update("taille",taille_value.get())

    # Fonction pour sauvegarder la couleur   
    def save_couleur(self, couleur_value):
        update("couleur",couleur_value.get())

# Fermeture app   
app = App()
app.mainloop()
