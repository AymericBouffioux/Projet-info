import customtkinter as ctk
import affichage_animation
from configurator import get_data
from PIL import Image, ImageTk
        

def rejouer_niveau(fenetre):

    map_a_rejouer = get_data("map_actuelle")
    screen = affichage_animation.AppForCanvas("carte " + str(map_a_rejouer))
    fenetre.withdraw()
    screen.mainloop()

def retour_fr_start(fenetre):
    fenetre.withdraw()
    from Projet_info import App
    #screen = App()
    #screen.show_fr_start()
    #screen.mainloop()


def quitter(frame):
    frame.destroy()
    
    
def afficher_loser():
    # Créez la fenêtre principale
    fenetre_gameover = ctk.CTk()
    fenetre_gameover.resizable(0, 0)

    # Canvas pour la tête de mort
    canvas_tete = ctk.CTkCanvas(fenetre_gameover, width=300, height=300)
    canvas_tete.grid(row=4, column=2)
    image_principale = Image.open("Projet-info-main/images/ghost.png")
    image_principale.thumbnail((300,300))
    photo_angry= ImageTk.PhotoImage(master = canvas_tete, image = image_principale)
    image_widget_principal = canvas_tete.create_image(150, 150, anchor = 'center', image = photo_angry)

    # Étiquette "GAME OVER"
    ctk.CTkLabel(fenetre_gameover, text="GAME OVER", justify="center", font=("Arial", 60)).grid(row=0, column=2)

    # Bouton "REJOUER"
    bouton_restart = ctk.CTkButton(fenetre_gameover, text="REJOUER", height=25, width=50, command=lambda: rejouer_niveau(fenetre_gameover))
    bouton_restart.grid(row=1, column=2)

    # Bouton "Retour"
    bouton_retour_start = ctk.CTkButton(fenetre_gameover, text="RETOUR", height=25, width=50, command=lambda: retour_fr_start(fenetre_gameover))
    bouton_retour_start.grid(row=2, column=2)
    
    # Bouton "quitter"
    bouton_quitter = ctk.CTkButton(fenetre_gameover, text="QUITTER", height=25, width=50, command=lambda: quitter(fenetre_gameover))
    bouton_quitter.grid(row=3, column=2)

    

    fenetre_gameover.mainloop()
if __name__ == "__main__":
    afficher_loser() #ça permet de tester