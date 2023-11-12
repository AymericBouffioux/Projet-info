from tkinter import BOTH
import customtkinter as ctk

# Créer une fenêtre
fr_options = ctk.CTk()
fr_options.title("Option")

# Variable de contrôle pour le thème
theme_var = ctk.StringVar()
theme_var.set("light")  # "light" pour le thème "light", "dark" pour le thème "dark"

# Widget de texte pour afficher le titre
text_label = ctk.CTkLabel(fr_options, text="Page Option ",fg_color=("#ADD8E6", 'blue'))
text_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
# Widget de texte pour afficher le titre thème
text_label1 = ctk.CTkLabel(fr_options, text="Thème ",fg_color=("#ADD8E6", 'blue'))
text_label1.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

# Fonction pour changer le thème
def change_theme():
    theme = theme_var.get()
    ctk.set_appearance_mode(theme)

# Radiobuttons pour choisir le thème
light_radio = ctk.CTkRadioButton(fr_options, text="Light / clair ", variable=theme_var, value="light", command=change_theme)
dark_radio = ctk.CTkRadioButton(fr_options, text="Dark / sombre ", variable=theme_var, value="dark", command=change_theme)
light_radio.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
dark_radio.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

# Widget de texte pour afficher le titre langue
text_label2 = ctk.CTkLabel(fr_options, text=" Langue " ,fg_color=("#ADD8E6", 'blue'))
text_label2.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

# Fonction pour changer la langue
def change_language(event):
    language = language_optionmenu.get()
    if language == "Français":
        text_label.configure(text="Page Option")
        text_label.configure(text="thème")
    elif language == "English":
        text_label.configure(text="Option Page")
        text_label1.configure(text="theme")

# OptionMenu pour choisir la langue
language_optionmenu = ctk.CTkOptionMenu(fr_options, values=["Français", "English"],command=change_language)
language_optionmenu.set("Français")
language_optionmenu.grid(row=5, column=0, padx=20, pady=20, sticky="ew")


fr_options.mainloop()


