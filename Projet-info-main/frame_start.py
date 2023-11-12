from tkinter import BOTH
import customtkinter as ctk
import fr_modulation



def bouton_clic(nom):
    if nom == "Modulation des Catapultes":
        fr_modulation.create_cata()
        
    elif nom == "Modulation des Boules":
        fr_modulation.create_boules()

    print(f"Bouton {nom} cliqué")
    
fr_start= ctk.CTk()
# Créer une fenêtre

fr_start.title(" Start ")
# Créer un cadre pour les boutons "Map1", "Map2" et "Map3"
cadre_boutons_map = ctk.CTkFrame(fr_start, fg_color="#ADD8E6")
cadre_boutons_map.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="ew", columnspan=5)
# Créer les boutons "Map1", "Map2" et "Map3" centrés horizontalement dans le rectangle rose
bouton_map1 = ctk.CTkButton(fr_start, text="Map1", command=lambda: bouton_clic("Map1"))
bouton_map2 = ctk.CTkButton(fr_start, text="Map2", command=lambda: bouton_clic("Map2"))
bouton_map3 = ctk.CTkButton(fr_start, text="Map3", command=lambda: bouton_clic("Map3"))
bouton_map1.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="w")
bouton_map2.grid(row=3, column=2, padx=20, pady=(0, 20), sticky="w")
bouton_map3.grid(row=3, column=4, padx=20, pady=(0, 20), sticky="w")


# Créer le bouton "Modulation des Boules" en haut à gauche
bouton_boules = ctk.CTkButton(fr_start, text="Modulation des Boules", command=lambda: bouton_clic("Modulation des Boules"))
# bouton_boules.configure(bg="blue", width=11, height=2)  # Changer la couleur, la largeur et la hauteur du bouton

bouton_boules.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")
# Créer le bouton "Modulation des Catapultes" en haut à droite
bouton_catapultes = ctk.CTkButton(fr_start, text="Modulation des Catapultes", command=lambda: bouton_clic("Modulation des Catapultes"))
# bouton_catapultes.configure(bg="red", width=11, height=2)  # Changer la couleur, la largeur et la hauteur du bouton
bouton_catapultes.grid(row=1, column=3, padx=20, pady=(0, 20), sticky="w")
# Lancer la boucle principale de l'application
fr_start.mainloop()
