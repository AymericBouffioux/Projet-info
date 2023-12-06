"""from tkinter.tix import COLUMN
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

afficher_win()"""

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
    map_a_jouer = get_data("map_actuelle") + 1
    screen = animation.AppForCanvas("carte " + str(map_a_jouer))
    fenetre.withdraw()
    screen.mainloop()

def afficher_win():
    # Créez la fenêtre principale
    fenetre_winner = ctk.CTk()
    fenetre_winner.resizable(0, 0)

    # Écrir Winner
    text1 = ctk.CTkLabel(fenetre_winner, text="Winner", justify="center", font=("Arial", 60))
    text1.grid(row=0, column=1)

    # Créez un bouton_restart
    bouton_restart = ctk.CTkButton(fenetre_winner, text="REJOUER", height=25, width=50, command=lambda: rejouer_niveau(fenetre_winner))
    bouton_restart.grid(row=2, column=1)

    # Créez un bouton_next_map 
    map_actuelle = get_data("map_actuelle") 
    if map_actuelle < 3:
        bouton_next_map = ctk.CTkButton(fenetre_winner, text="MAP SUIVANTE", command=lambda: niveau_suivant(fenetre_winner))
        bouton_next_map.grid(row=3, column=1)

    # Fonction pour dessiner une étoile
    def dessiner_etoile(canvas, x, y,couleur = 'white'):
        points = [x, y - 20, x + 10, y + 10, x + 30, y + 10, x + 15, y + 25, x + 25, y + 45, x, y + 30, x - 25, y + 45, x - 15, y + 25, x - 30, y + 10, x - 10, y + 10]
        canvas.create_polygon(points,fill = couleur, outline='black', width=2)
    
    
    nb_boules = get_data("nb_boules")
    score = 1
    if nb_boules <= 10 :
        score = 3
    if nb_boules > 10 and nb_boules <=20:
        score = 2
    
    
    # Créer un canvas (zone de dessin) pour chaque étoile
    for i in range(3):
        canvas_etoile = ctk.CTkCanvas(fenetre_winner, width=60, height=100)
        canvas_etoile.grid(row=1, column=i)
        x_position = 31    # Ajuster la position horizontale
        y_position = 50  # Ajuster la position verticales
        dessiner_etoile(canvas_etoile,x_position, y_position)
        if score == 1:
            if i == 0 :
                dessiner_etoile(canvas_etoile,x_position, y_position,"yellow")
            ctk.CTkLabel(fenetre_winner, text="Félicitations! Vous avez obtenu toutes les étoiles!", font=("Arial", 16)).grid(row=5, column=1)
        if score == 2:
            if i <= 1 :
                dessiner_etoile(canvas_etoile,x_position, y_position,"yellow")
            ctk.CTkLabel(fenetre_winner, text="Félicitations! Vous avez obtenu toutes les étoiles!", font=("Arial", 16)).grid(row=5, column=1)
        if score == 3:
            dessiner_etoile(canvas_etoile,x_position, y_position,"yellow")
            ctk.CTkLabel(fenetre_winner, text="Félicitations! Vous avez obtenu toutes les étoiles!", font=("Arial", 16)).grid(row=5, column=1)

    # Afficher le score et ajuster les étoiles en fonction du score
    score_label = ctk.CTkLabel(fenetre_winner, text=f"Score: {score}", font=("Arial", 20))
    score_label.grid(row=4, column=1)

    

    # Lancez la boucle principale
    fenetre_winner.mainloop()

# Exemple d'utilisation
score_obtenu = 3 # Remplacez cela par le score réel que vous avez obtenu
#afficher_win(score_obtenu)
