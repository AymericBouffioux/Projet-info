import customtkinter as ctk
from configurator import get_data
import animation
import affichage_animation

def rejouer_niveau(fenetre):
    map_a_rejouer = get_data("map_actuelle")
    screen = animation.AppForCanvas("carte " + str(map_a_rejouer))
    screen = affichage_animation.AppForCanvas("carte " + str(map_a_rejouer))
    fenetre.withdraw()
    screen.mainloop()

def niveau_suivant(fenetre):
    map_a_jouer = get_data("map_actuelle") + 1
    screen = affichage_animation.AppForCanvas("carte " + str(map_a_jouer))
    screen = affichage_animation.AppForCanvas("carte " + str(map_a_jouer))
    fenetre.withdraw()
    screen.mainloop()
    
def quitter(frame):
    frame.destroy()
    
def retour_fr_start(fenetre):
    fenetre.withdraw()
    from Projet_info import App
   
def afficher_win():
    # Créez la fenêtre principale
    fenetre_winner = ctk.CTk()
    fenetre_winner.resizable(0, 0)

    # Écrire Winner
    lbl_winner = ctk.CTkLabel(fenetre_winner, text="WINNER", justify="center", font=("Arial", 60))
    lbl_winner.pack()

    # Créez un seul canevas pour les étoiles
    canvas = ctk.CTkCanvas(fenetre_winner, width=300, height=100, bg='white') 
    canvas.pack()

    # Fonction pour dessiner une étoile
    def dessiner_etoile(x, y, couleur='yellow'):
        canvas.create_polygon(
            x + 50, y + 15, x + 60, y + 45, x + 90, y + 45,
            x + 65, y + 60, x + 75, y + 90, x + 50, y + 75,
            x + 25, y + 90, x + 35, y + 60, x + 10, y + 45,
            x + 40, y + 45, fill=couleur, outline='black'
        )
    nb_boules = get_data("nb_boules")
    score = 0 
    if nb_boules <= 10 : 
        score = 3
    elif nb_boules >= 10 and nb_boules <= 20 : 
        score = 2
    else : 
       score = 1
    # Mettez ici le score réel que vous avez obtenu

    # Dessiner les étoiles sur le même canevas à différentes positions horizontales
    for i in range(score):
        x_position = i * 100  # Ajuster la position horizontale
        y_position = 0        # Ajuster la position verticale
        dessiner_etoile(x_position, y_position)

    # Dessiner les étoiles restantes en gris
    for i in range(score, 3):
        x_position = i * 100  # Ajuster la position horizontale
        y_position = 0        # Ajuster la position verticale
        dessiner_etoile(x_position, y_position, couleur='gray')
        
    map_actuelle = get_data("map_actuelle") 
    if map_actuelle < 3:
        bouton_next_map = ctk.CTkButton(fenetre_winner, text="CARTE SUIVANTE",height=25, width=150, command=lambda: niveau_suivant(fenetre_winner))
        bouton_next_map.pack()

    # Créez un bouton_restart
    bouton_restart = ctk.CTkButton(fenetre_winner, text="REJOUER", height=25, width=150, command=lambda: rejouer_niveau(fenetre_winner))
    bouton_restart.pack()
    # Bouton "Retour"
    bouton_retour_start = ctk.CTkButton(fenetre_winner, text="RETOUR", height=25, width=100, command=lambda: retour_fr_start(fenetre_winner))
    bouton_retour_start.pack()
    # Bouton "Quitter"
    bouton_quitter = ctk.CTkButton(fenetre_winner, text="QUITTER", height=20, width=20, command=lambda: quitter(fenetre_winner))
    bouton_quitter.pack()
    
    fenetre_winner.mainloop()

# Test
if __name__ == "__main__":
    afficher_win()