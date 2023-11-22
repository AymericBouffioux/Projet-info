from tkinter.tix import COLUMN
import customtkinter as ctk
from configurator import get_data
import animation 

def rejouer_niveau(fenetre):

    map_a_rejouer = get_data("map_actuelle")
    screen = animation.AppForCanvas("carte " + str(map_a_rejouer))
    fenetre.withdraw()

    screen.mainloop()

def niveau_suivant(fenetre):

    map_a_jouer = get_data("map_actuelle") +1
    

    screen = animation.AppForCanvas("carte " + str(map_a_jouer))

    fenetre.withdraw()

    screen.mainloop()

def afficher_win():
    # Créez la fenêtre principale
    fenetre_winner = ctk.CTk()
    fenetre_winner.resizable(0,0)

    
    # Écrir Winner
    text1 = ctk.CTkLabel(fenetre_winner, text="Winner" , justify="center", font=("Arial",60))
    text1.grid(row = 0, column = 2)

    # Créez un bouton_restart
    bouton_restart= ctk.CTkButton(fenetre_winner, text="REJOUER",height=25, width=50, command=lambda: rejouer_niveau(fenetre_winner))
    bouton_restart.grid(row = 2, column = 2)


    # Créez un bouton_next_map 
    map_actuelle = get_data("map_actuelle") 
    if map_actuelle < 3:
        bouton_next_map = ctk.CTkButton(fenetre_winner, text="MAP SUIVANTE", command=lambda: niveau_suivant(fenetre_winner))
        bouton_next_map.grid(row=3, column=2) 

    

    # Créez une étoile dans la fenêtre
    def dessiner_etoile(canvas):
        # Coordonnées des points pour dessiner une étoile
        points = [50, 10, 60, 30, 80, 30, 65, 45, 75, 65, 50, 50, 25, 65, 35, 45, 20, 30, 40, 30]

        # Dessiner une étoile en utilisant le polygone
        canvas.create_polygon(points, fill='yellow', outline='black', width=2)

    # Créer un canvas (zone de dessin)
    canvas_étoile = ctk.CTkCanvas(fenetre_winner, width=100, height=100)
    canvas_étoile.grid(row=1, column=2, padx=10, pady=10)  # Utilisez grid

    # Appeler la fonction pour dessiner l'étoile
    dessiner_etoile(canvas_étoile)

    # Lancez la boucle principale
    fenetre_winner.mainloop()