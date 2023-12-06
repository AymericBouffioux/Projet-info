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

    # Écrire Winner
    lbl_winner = ctk.CTkLabel(fenetre_winner, text="Winner", justify="center", font=("Arial", 60))
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

    score = get_data("nb_boules")
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

    # Afficher le score
    score_label = ctk.CTkLabel(fenetre_winner, text=f"Score = {score}", font=("Arial", 20))
    score_label.pack()

    # Créez un bouton_restart
    bouton_restart = ctk.CTkButton(fenetre_winner, text="REJOUER", height=25, width=50, command=lambda: rejouer_niveau(fenetre_winner))
    bouton_restart.pack()

    # Créez un bouton_next_map 
    map_actuelle = get_data("map_actuelle") 
    if map_actuelle < 3:
        bouton_next_map = ctk.CTkButton(fenetre_winner, text="MAP SUIVANTE", command=lambda: niveau_suivant(fenetre_winner))
        bouton_next_map.pack()

    # Lancez la boucle principale
    fenetre_winner.mainloop()

# Exemple d'utilisation
if __name__ == "__main__":
    afficher_win()
