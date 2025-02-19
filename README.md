# Gestionnaire de Mots de Passe (Tkinter + Chiffrement)

Ce programme est une application graphique développée en Python avec **Tkinter** pour permettre aux utilisateurs de **stocker, afficher, modifier et supprimer** leurs mots de passe de manière **sécurisée**. Les mots de passe sont **chiffrés avec la bibliothèque Cryptography (Fernet)** avant d'être enregistrés dans un fichier CSV local.

---

## 📌 **Installation**
### Prérequis
Assurez-vous d'avoir **Python 3.x** installé sur votre machine.

Installez les dépendances nécessaires avec la commande suivante :
```sh
pip install cryptography
```

---

## 🛠 **Utilisation**
### **Lancer l'application**
Exécutez le script principal en lançant la commande :
```sh
python password_manager_gui.py
```

L'interface graphique s'ouvrira automatiquement.

### **Fonctionnalités**
🔹 **Ajouter un mot de passe** : Ajoutez un site web et un mot de passe chiffré.
🔹 **Afficher les mots de passe** : Visualisez les mots de passe déchiffrés dans l'interface.
🔹 **Modifier un mot de passe** : Mettez à jour un mot de passe existant.
🔹 **Supprimer un mot de passe** : Supprimez un mot de passe du fichier CSV.

---

## 🔐 **Sécurité**
1. **Les mots de passe sont chiffrés** avant d’être enregistrés dans le fichier CSV.
2. Une **clé de chiffrement** est générée et stockée dans un fichier `key.key`.
3. **Si vous perdez le fichier `key.key`, vous ne pourrez plus déchiffrer les mots de passe enregistrés.**

---

## 📂 **Structure du projet**
```
📂 projet-password-manager/
│── main.py    # Code source principal
│── key.key                    # Clé de chiffrement (générée automatiquement)
│── passwords.csv              # Fichier contenant les mots de passe chiffrés
│── README.md                  # Documentation
```

---

## 📌 **Améliorations possibles**
✅ Ajouter un **mot de passe maître** pour protéger l'accès.
✅ Enregistrer les mots de passe dans une **base de données** plutôt qu'un fichier CSV.
✅ Générer des **mots de passe aléatoires sécurisés** pour l'utilisateur.

---

## 🤝 **Contributions**
Les contributions sont les bienvenues ! Si vous souhaitez proposer des améliorations, n’hésitez pas à **forker** ce projet et à envoyer une **pull request**.

---

## 📜 **Licence**
Ce projet est sous licence **MIT**. Vous êtes libre de l’utiliser et de le modifier à votre guise.

---

🚀 **Bon développement et sécurisez vos mots de passe !** 🔐

