
from tkinter import BOTH
import customtkinter as ctk

def destroy_window(window):
    window.destroy()

# Fonction pour modifier la catapulte
def create_cata():
# Créer une fenêtre
    fr_modul_cata = ctk.CTk()
    fr_modul_cata.title(" modulation catapulte")

    # Widget de texte pour afficher le titre
    text_label = ctk.CTkLabel(fr_modul_cata, text="modulation catapulte ",fg_color=("#ADD8E6", 'blue'))
    text_label.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

    # Widget de texte pour afficher le titre
    text_label = ctk.CTkLabel(fr_modul_cata, text="élasticité ",fg_color=("#ADD8E6", 'blue'))
    text_label.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

    # slider pr determiner l'elasticité
    def slider_event(value):
        print(value)
    # slider pr determiner l'elasticité
    slider_elasticité = ctk.CTkSlider(fr_modul_cata, from_=0, to=5, command=slider_event)
    slider_elasticité.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

    # Widget de texte pour afficher le titre
    text_label1 = ctk.CTkLabel(fr_modul_cata, text="vitesse de chargement ",fg_color=("#ADD8E6", 'blue'))
    text_label1.grid(row=6, column=0, padx=20, pady=20, sticky="ew")

    # slider pr determiner la vitesse de chargement
    slider_vitesse_de_chargement= ctk.CTkSlider(fr_modul_cata, from_=0, to=5, command=slider_event)
    slider_vitesse_de_chargement.grid(row=7, column=0, padx=20, pady=20, sticky="ew")
    
    # bouton save
    btn_MS1 = ctk.CTkButton(fr_modul_cata, text="sauver",
                                 command=lambda: destroy_window(fr_modul_cata))
    btn_MS1.grid(row=0, column=0)

    fr_modul_cata.mainloop()
    
    
# Fonction pour modifier les boules   
def create_boules():
    # Créer une fenêtre
    fr_modul_boules = ctk.CTk()
    fr_modul_boules.title(" modulation des boules")

    # Widget de texte pour afficher le titre
    titre = ctk.CTkLabel(fr_modul_boules, text="modulation des boules ",fg_color=("#ADD8E6", 'blue'))
    titre.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

    # Widget de texte pour afficher le titre
    text_label = ctk.CTkLabel( fr_modul_boules, text="poids ",fg_color=("#ADD8E6", 'blue'))
    text_label.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

    # slider pr determiner l'elasticité
    def slider_event(value):
        print(value)
    # slider pr determiner l'elasticité
    slider_elasticité = ctk.CTkSlider(fr_modul_boules, from_=0, to=5, command=slider_event)
    slider_elasticité.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

    # Widget de texte pour afficher le titre
    text_label1 = ctk.CTkLabel(fr_modul_boules, text="taille ",fg_color=("#ADD8E6", 'blue'))
    text_label1.grid(row=6, column=0, padx=20, pady=20, sticky="ew")

    # slider pr determiner la vitesse de chargement
    slider_vitesse_de_chargement= ctk.CTkSlider(fr_modul_boules, from_=0, to=5, command=slider_event)
    slider_vitesse_de_chargement.grid(row=7, column=0, padx=20, pady=20, sticky="ew")
    
        # bouton save
    btn_MS2 = ctk.CTkButton(fr_modul_boules, text="sauver",
                                 command=lambda: fr_modul_boules)
    btn_MS2.grid(row=0, column=0)

    fr_modul_boules.mainloop()
    