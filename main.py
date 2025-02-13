import tkinter as tk

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Application avec plusieurs pages")
fenetre.geometry("400x300")
string =["Ajoutez votre mot de passe"]

def addpassword(enter):
    print("mdp ajouter : "+enter)
# Fonction pour afficher une page
def afficher_page(page):
    # Supprime tout le contenu actuel
    for widget in fenetre.winfo_children():
        widget.destroy()

    if page == "accueil":
        label = tk.Label(fenetre, text="Quelle option ?", font=("Arial", 16))
        label.pack(pady=20)
        bouton = tk.Button(fenetre, text="Ajoutez votre mot de passe", command=lambda: afficher_page("add"))
        bouton.pack()
        bouton = tk.Button(fenetre, text="Editez vos mot de passe", command=lambda: afficher_page("CRUD"))
        bouton.pack()
    elif page == "add":
        label = tk.Label(fenetre, text="Ajoutez votre mot de passe", font=("Arial", 16))
        label.pack(pady=20)
        champ = tk.Entry(fenetre, font=("Arial", 14))  # Champ de saisie
        champ.pack(pady=20)
        bouton = tk.Button(fenetre, text="ajoutez", command=lambda:addpassword(champ.get()))
        bouton.pack()
        bouton = tk.Button(fenetre, text="Menu", command=lambda: afficher_page("accueil"))
        bouton.pack()
    elif page == "CRUD":
        label = tk.Label(fenetre, text="Editez vos mot de passe", font=("Arial", 16))
        label.pack(pady=20)
        bouton = tk.Button(fenetre, text="Menu", command=lambda: afficher_page("accueil"))
        bouton.pack()

# Afficher la première page (accueil)
afficher_page("accueil")

# Lancer la fenêtre
fenetre.mainloop()
