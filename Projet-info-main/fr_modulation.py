
from tkinter import BOTH, DoubleVar
from tokenize import Double
import customtkinter as ctk
from configurator import update   


def destroy_window(window):
    window.destroy()

# Fonction pour modifier la catapulte
def create_cata():
    # Créer une fenêtre
    fr_modul_cata = ctk.CTk()
    fr_modul_cata.title(" modulation catapulte")
    
    elasticite_value = DoubleVar(value=2.5) 
    

    # Fonction pour sauvegarder l'élasticité
    def save_elasticite(elasticite_value):
        print(f"Elasticite sauvée : {elasticite_value.get()}")
        update("elasticite",elasticite_value.get())
    
    # Widget de texte pour afficher le titre
    text_label = ctk.CTkLabel(fr_modul_cata, text="modulation catapulte ",fg_color=("#ADD8E6", 'blue'))
    text_label.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

    # Widget de texte pour afficher le titre
    text_label = ctk.CTkLabel(fr_modul_cata, text="elasticite ",fg_color=("#ADD8E6", 'blue'))
    text_label.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

    # slider pr determiner l'elasticité
    def slider_event(value):
        elasticite_value.set(value)
        print(value)
    # slider pr determiner l'elasticité
    slider_elasticité = ctk.CTkSlider(fr_modul_cata, from_=1, to=5, command=slider_event)
    slider_elasticité.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
    
    
    # bouton save
    btn_Save = ctk.CTkButton(fr_modul_cata, text="sauver",
                                 command=lambda: (save_elasticite(elasticite_value)))#, save_vitesse_charge(vitesse_char_value)
    btn_Save.grid(row=1, column=0)
    
    # bouton retour
    btn_SM = ctk.CTkButton(fr_modul_cata, text="Retour à la page Start", command=lambda: destroy_window(fr_modul_cata))
    btn_SM.grid(row=0, column=0)

    fr_modul_cata.mainloop()
    return elasticite_value.get()


    
    
# Fonction pour modifier les boules   
def create_boules():
    # Créer une fenêtre
    fr_modul_boules = ctk.CTk()
    fr_modul_boules.title(" modulation des boules")

    poids_value = DoubleVar(value=2.5) 
    taille_value = DoubleVar(value=2.5)
    couleur_value = DoubleVar(value=0)

    # Fonction pour sauvegarder le poids
    def save_poids(poids_value):
        print(f"Poids sauvée : {poids_value.get()}")
        update("poids",poids_value.get())
    # Fonction pour sauvegarder la vitesse de chargement
    def save_taille(taille_value):
        print(f"Taille sauvée : {taille_value.get()}")
        update("taille",taille_value.get())
    
    def save_couleur(couleur_value):
        #print(f"Couleur sauvée : {couleur_value.get()}")
        update("couleur",couleur_value.get())


    # Widget de texte pour afficher le titre
    titre = ctk.CTkLabel(fr_modul_boules, text="modulation des boules ",fg_color=("#ADD8E6", 'blue'))
    titre.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

    # slider pr determiner le poids
    def slider_event(value):
        poids_value.set(value)
        print(value)

    # Widget de texte pour afficher le titre
    text_label = ctk.CTkLabel( fr_modul_boules, text="poids",fg_color=("#ADD8E6", 'blue'))
    text_label.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
    
    # slider pr determiner l'elasticité
    slider_poids = ctk.CTkSlider(fr_modul_boules, from_=1, to=5, command=slider_event)
    slider_poids.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

    # slider pr determiner la taille
    def slider_event(value):
        taille_value.set(value)
        print(value)

    # Widget de texte pour afficher le titre
    text_label1 = ctk.CTkLabel(fr_modul_boules, text="taille",fg_color=("#ADD8E6", 'blue'))
    text_label1.grid(row=6, column=0, padx=20, pady=20, sticky="ew")

    # slider pr determiner la vitesse de chargement
    slider_taille= ctk.CTkSlider(fr_modul_boules, from_=2.5, to=7.5, command=slider_event)
    slider_taille.grid(row=7, column=0, padx=20, pady=20, sticky="ew")
    
    
    def update_color(selected_color):
        #global couleur_value
        if selected_color == "Rouge":
            couleur = 0
            
        elif selected_color == "Bleu":
            couleur = 1

        elif selected_color == "Rose":
            couleur = 2


        couleur_value.set(couleur)

   

    # Widget de texte pour afficher le titre
    text_label2 = ctk.CTkLabel(fr_modul_boules, text="couleur", fg_color=("#ADD8E6", 'blue'))
    text_label2.grid(row=8, column=0, padx=20, pady=20, sticky="ew")

    language_optionmenu = ctk.CTkOptionMenu(fr_modul_boules, values=["Rouge", "Bleu", "Rose"],
                                            command=update_color)
    # Bouton pour ouvrir le sélecteur de couleur
    
    language_optionmenu.grid(row=9, column=0, padx=20, pady=20, sticky="ew")   

     # bouton retour
    btn_SM = ctk.CTkButton(fr_modul_boules, text="Retour à la page Start", command=lambda: destroy_window(fr_modul_boules))
    btn_SM.grid(row=0, column=0)


    # bouton save
    btn_Save = ctk.CTkButton(fr_modul_boules, text="sauver",
                                 command=lambda: (save_poids(poids_value), save_taille(taille_value),save_couleur(couleur_value)))
    btn_Save.grid(row=1, column=0)
    
    
    fr_modul_boules.mainloop()
