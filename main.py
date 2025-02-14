import tkinter as tk
import csv
# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Application avec plusieurs pages")
fenetre.geometry("400x300")
string =["Ajoutez votre mot de passe"]

import csv
fichier_csv = "passwords.csv"
def addpassword(enterWebSite, enterPassword):

    champs = ["website", "password"]

    # Créer un dictionnaire contenant les données
    entry = {"website": enterWebSite, "password": enterPassword}

    # Vérifier si le fichier existe et s'il est vide
    try:
        with open(fichier_csv, mode="r", encoding="utf-8") as fichier:
            contient_donnees = fichier.read().strip() != ""  # Vérifie si le fichier contient déjà des données
    except FileNotFoundError:
        contient_donnees = False  # Si le fichier n'existe pas, on le considère comme vide

    # Ouvrir le fichier en mode ajout ("a")
    with open(fichier_csv, mode="a", newline="", encoding="utf-8") as fichier:
        writer = csv.DictWriter(fichier, fieldnames=champs)

        # Écrire l'en-tête uniquement si le fichier est vide
        if not contient_donnees:
            writer.writeheader()

        # Écriture de l'entrée
        writer.writerow(entry)  # ✅ Correction : on écrit une seule ligne

    print("Mot de passe ajouté avec succès !")



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
        champ=["",""]
        champ_website = tk.Entry(fenetre, font=("Arial", 14))  # Champ de saisie
        champ_website.pack(pady=20)
        champ = tk.Entry(fenetre, font=("Arial", 14))  # Champ de saisie
        champ.pack(pady=20)
        bouton = tk.Button(fenetre, text="ajoutez", command=lambda:addpassword(champ_website.get(),champ.get()))
        bouton.pack()
        bouton = tk.Button(fenetre, text="Menu", command=lambda: afficher_page("accueil"))
        bouton.pack()
    elif page == "CRUD":
        label = tk.Label(fenetre, text="Editez vos mot de passe", font=("Arial", 16))
        try:
            with open(fichier_csv, mode="r", encoding="utf-8") as fichier:
                reader = csv.DictReader(fichier)  # Lire les données sous forme de dictionnaires
                
                data = list(reader)  # Convertir en liste de dictionnaires
                
                print(data ) # Retourne toutes les lignes sous forme de liste de dictionnaires
        
        except FileNotFoundError:
            print("Le fichier n'existe pas encore.")
            return []  
        label.pack(pady=20)
        bouton = tk.Button(fenetre, text="Menu", command=lambda: afficher_page("accueil"))
        bouton.pack()

# Afficher la première page (accueil)
afficher_page("accueil")

# Lancer la fenêtre
fenetre.mainloop()
