
from tkinter import BOTH
import customtkinter as ctk

def destroy_window(window):
    window.destroy()

# Fonction pour changer le thème        
def change_theme():
    # Créer une fenêtre
    fr_change_theme = ctk.CTk()
    fr_change_theme.title("Changer le thème")
    
    # Variable de contrôle pour le thème
    theme_var = ctk.StringVar()
    theme_var.set("light") 
    
    # Fonction pour changer le thème de la fenêtre
    def set_theme():
        selected_theme = theme_var.get()
        # Change le thème en light mode
        if selected_theme == "light":
            ctk.set_appearance_mode("Light")
        # Change le thème en dark mode
        elif selected_theme == "dark":
            ctk.set_appearance_mode("Dark")

            
    # Radiobuttons pour choisir le thème
    light_radio = ctk.CTkRadioButton(fr_change_theme, text="Light / Clair ", variable=theme_var, value="light", command=set_theme)
    dark_radio = ctk.CTkRadioButton(fr_change_theme, text="Dark / Sombre ", variable=theme_var, value="dark", command=set_theme)
    light_radio.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
    dark_radio.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
          
    btn_TO = ctk.CTkButton(fr_change_theme, text="sauver",
                                 command=lambda: destroy_window(fr_change_theme))
    btn_TO.grid(row=0, column=0)

    fr_change_theme.mainloop()
        
                   
# Fonction pour changer de langue
def change_language():
    # Créer une fenêtre
    fr_change_language = ctk.CTk()
    fr_change_language.title("Changer la langue")
    
    # OptionMenu pour choisir la langue
    language_optionmenu = ctk.CTkOptionMenu(fr_change_language, values=["Français", "English"],
                                            command=update_language)
    language_optionmenu.set("Français")
    language_optionmenu.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        
    btn_LO = ctk.CTkButton(fr_change_language, text="sauver",
                                command=lambda: destroy_window(fr_change_language))
    btn_LO.grid(row=0, column=0)

    fr_change_language.mainloop()

# Modifie le texte en français
def update_french_language(label):
    label.config(text="Page Options", fg_color=("#ADD8E6", 'blue'))
# Modifie le texte en anglais
def update_english_language(label):
    label.config(text="Options Page", fg_color=("#ADD8E6", 'blue'))

# Fonction pour mettre à jour la langue
def update_language(selected_language):
    if selected_language == "Français":
        update_french_language()
    elif selected_language == "English":
        update_english_language()

