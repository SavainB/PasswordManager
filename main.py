import tkinter as tk
import csv
import tempfile
import os
import shutil
from cryptography.fernet import Fernet

# Générer une clé de chiffrement et la sauvegarder
KEY_FILE = "key.key"
CSV_FILE = "passwords.csv"

def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)

def load_key():
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

generate_key()
key = load_key()
cipher_suite = Fernet(key)

def encrypt_password(password):
    return cipher_suite.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return cipher_suite.decrypt(encrypted_password.encode()).decode()

def add_password(website, password):
    encrypted_password = encrypt_password(password)
    fields = ["website", "password"]
    entry = {"website": website, "password": encrypted_password}
    
    file_exists = os.path.exists(CSV_FILE) and os.path.getsize(CSV_FILE) > 0
    
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        if not file_exists:
            writer.writeheader()
        writer.writerow(entry)

def delete_entry(line_number):
    temp_file = tempfile.NamedTemporaryFile(mode="w", newline="", encoding="utf-8", delete=False)
    
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file, temp_file:
        reader = csv.reader(file)
        writer = csv.writer(temp_file)
        
        for i, row in enumerate(reader):
            if i != line_number:
                writer.writerow(row)
    
    shutil.move(temp_file.name, CSV_FILE)
    display_page("manage")

def modify_entry(index, website, new_password):
    lines = []
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        lines = list(reader)
    
    if index < len(lines):
        lines[index]["website"] = website
        lines[index]["password"] = encrypt_password(new_password)
    
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["website", "password"])
        writer.writeheader()
        writer.writerows(lines)
    
    display_page("manage")

def display_page(page):
    for widget in root.winfo_children():
        widget.destroy()
    
    if page == "home":
        tk.Label(root, text="Gestionnaire de mots de passe", font=("Arial", 16)).pack(pady=20)
        tk.Button(root, text="Ajouter un mot de passe", command=lambda: display_page("add")).pack()
        tk.Button(root, text="Gérer les mots de passe", command=lambda: display_page("manage")).pack()
    
    elif page == "add":
        tk.Label(root, text="Ajouter un mot de passe", font=("Arial", 16)).pack(pady=20)
        website_entry = tk.Entry(root, font=("Arial", 14))
        website_entry.pack(pady=10)
        password_entry = tk.Entry(root, font=("Arial", 14), show="*")
        password_entry.pack(pady=10)
        tk.Button(root, text="Ajouter", command=lambda: add_password(website_entry.get(), password_entry.get())).pack()
        tk.Button(root, text="Retour", command=lambda: display_page("home")).pack()
    
    elif page == "manage":
        tk.Label(root, text="Vos mots de passe", font=("Arial", 16)).pack()
        
        try:
            with open(CSV_FILE, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for i, row in enumerate(reader):
                    website = row["website"]
                    decrypted_password = decrypt_password(row["password"])
                    
                    frame = tk.Frame(root)
                    frame.pack()
                    
                    tk.Label(frame, text=f"{website} - {decrypted_password}", font=("Arial", 12)).pack(side=tk.LEFT)
                    tk.Button(frame, text="Modifier", command=lambda i=i: display_modify_page(i, row["website"]) ).pack(side=tk.LEFT)
                    tk.Button(frame, text="Supprimer", command=lambda i=i: delete_entry(i+1)).pack(side=tk.LEFT)
        except FileNotFoundError:
            tk.Label(root, text="Aucun mot de passe enregistré.").pack()
        
        tk.Button(root, text="Retour", command=lambda: display_page("home")).pack()
    
    elif page == "modify":
        pass  # Page définie dans display_modify_page()

def display_modify_page(index, website):
    display_page("modify")
    tk.Label(root, text="Modifier le mot de passe", font=("Arial", 16)).pack(pady=20)
    website_entry = tk.Entry(root, font=("Arial", 14))
    website_entry.insert(0, website)
    website_entry.pack(pady=10)
    password_entry = tk.Entry(root, font=("Arial", 14), show="*")
    password_entry.pack(pady=10)
    tk.Button(root, text="Modifier", command=lambda: modify_entry(index, website_entry.get(), password_entry.get())).pack()
    tk.Button(root, text="Retour", command=lambda: display_page("manage")).pack()

# Création de l'interface principale
root = tk.Tk()
root.title("Gestionnaire de mots de passe")
root.geometry("500x500")
display_page("home")
root.mainloop()
