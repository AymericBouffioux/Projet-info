from tkinter.tix import COLUMN
import customtkinter as ctk
import tkinter as tk
import animation
from configurator import get_data



        

def rejouer_niveau(fenetre):

    map_a_rejouer = get_data("map_actuelle")
    screen = animation.AppForCanvas("carte " + str(map_a_rejouer))
    fenetre.withdraw()
    screen.mainloop()


def dessiner_tete_de_mort(canvas):
    # Dessiner le crâne
    canvas.create_oval(50, 50, 150, 150, outline="black", width=2, fill="black")

    # Dessiner les yeux
    canvas.create_oval(80, 80, 100, 100, outline="black", width=2, fill="white")
    canvas.create_oval(120, 80, 140, 100, outline="black", width=2, fill="white")

    # Dessiner le nez (un triangle)
    canvas.create_polygon(110, 110, 120, 120, 130, 110, outline="black", fill="black")

    # Dessiner la bouche (une ligne courbe)
    canvas.create_line(80, 130, 140, 130, width=2, smooth=True)

def retour_fr_start(fenetre):
    fenetre.withdraw()
    from Projet_info import App
    
    screen = App()
    screen.show_fr_start()
    screen.mainloop()




    
def afficher_loser():
    # Créez la fenêtre principale
    fenetre_gameover = ctk.CTk()
    fenetre_gameover.resizable(0, 0)

    # Canvas pour la tête de mort
    canvas_tete = ctk.CTkCanvas(fenetre_gameover, width=200, height=200)
    canvas_tete.grid(row=3, column=2)

    # Étiquette "GAME OVER"
    ctk.CTkLabel(fenetre_gameover, text="GAME OVER", justify="center", font=("Arial", 60)).grid(row=0, column=2)

    # Bouton "REJOUER"
    bouton_restart = ctk.CTkButton(fenetre_gameover, text="REJOUER", height=25, width=50, command=lambda: rejouer_niveau(fenetre_gameover))
    bouton_restart.grid(row=2, column=2)

    # Bouton "Retour"
    bouton_retour_start = ctk.CTkButton(fenetre_gameover, text="home", height=25, width=50, command=lambda: retour_fr_start(fenetre_gameover))
    bouton_retour_start.grid(row=3, column=2)


    # Appeler la fonction pour dessiner la tête de mort
    dessiner_tete_de_mort(canvas_tete)
    

    fenetre_gameover.mainloop()



    """
    # Créez la fenêtre principale
    fenetre_gameover = ctk.CTk()
    fenetre_gameover.resizable(0,0)

    # Écrir Winner
    text1 = ctk.CTkLabel(fenetre_gameover, text="GAME OVER" , justify="center", font=("Arial",60))
    text1.grid(row = 0, column = 2)

    # Créez un bouton_restart
    bouton_restart= ctk.CTkButton(fenetre_gameover, text="REJOUER",height=25, width=50)
    bouton_restart.grid(row = 2, column = 2)

    def dessiner_tete_de_mort(canvas):
        # Dessiner le crâne
        canvas_tete.create_oval(50, 50, 150, 150, outline="black", width=2, fill="black")

        # Dessiner les yeux
        canvas_tete.create_oval(80, 80, 100, 100, outline="black", width=2, fill="white")
        canvas_tete.create_oval(120, 80, 140, 100, outline="black", width=2, fill="white")

        # Dessiner le nez (un triangle)
        canvas_tete.create_polygon(110, 110, 120, 120, 130, 110, outline="black", fill="black")

        # Dessiner la bouche (une ligne courbe)
        canvas_tete.create_line(80, 130, 140, 130, width=2, smooth=True)

    
    # Créer un canvas
    canvas_tete = ctk.CTkCanvas(fenetre_gameover, width=200, height=200)
    canvas_tete.grid(row=3, column=2)

    # Appeler la fonction pour dessiner la tête de mort
    dessiner_tete_de_mort(canvas_tete)

    # Lancez la boucle principale
    fenetre_gameover.mainloop()"""