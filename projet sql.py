import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from tkinter import font

# Configuration de la base de données
configuration = {
    'user': 'root',
    'password': 'donotforgetme3',
    'host': '127.0.0.1',
    'database': 'Etudiants',
    'raise_on_warnings': True
}

# Création de la connexion et gestion des erreurs
try:
    connexion = mysql.connector.connect(**configuration)
    print("Connexion réussie")
except mysql.connector.Error as err:
    print(f"Erreur lors de la connexion : {err}")
    exit()

# Fonction pour changer la couleur des boutons en fonction de l'endroit où on se trouve
def update_button_colors(active_button):
    buttons = [info_button, parcours_button, autre_button]
    for button in buttons:
        button.config(bg='#F5F5DC', fg='black')
    active_button.config(bg='#0B3D91', fg='white')

# Fonction pour masquer les champs de connexion
def hide_login_fields():
    email_label.pack_forget()
    email_entry.pack_forget()
    password_label.pack_forget()
    password_entry.pack_forget()
    login_button.pack_forget()

# Fonction pour récupérer les données d'un seul étudiant avec email et mot de passe
def get_student_data():
    email = email_entry.get()
    password = password_entry.get()
   
    if not email or not password:
        messagebox.showwarning("Avertissement", "Veuillez entrer l'email et le mot de passe.")
        return

    try:
        cursor = connexion.cursor()
        query = "SELECT * FROM InformationsPersonnelles WHERE Email = %s AND Mot_de_passe = %s"
        cursor.execute(query, (email, password))
        row = cursor.fetchone()

        if row:
            hide_login_fields()  
            
            # Afficher le cadre de texte et les boutons
            nav_frame.pack(fill=tk.X)
            text_frame.pack()

            text_area.config(state='normal')  # Activer temporairement l'édition
            text_area.delete(1.0, tk.END)  # Vider l'ancienne entrée
            text_area.insert(tk.END, f"Prénom(s): {row[0]}\nNom(s): {row[1]}\nNationalité: {row[2]}\nAdresse: {row[3]}\nIdentifiant: {row[4]}\nNiveau d'étude: {row[5]}\nGenre: {row[6]}\nSituation matrimoniale: {row[7]}\nDate de naissance: {row[10]}\n\n")
            text_area.config(state='disabled')  # Désactiver l'édition après l'insertion
            
            update_button_colors(info_button)
        else:
            messagebox.showinfo("Information", "Aucun étudiant trouvé avec cet email et mot de passe.")
       
        cursor.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Erreur", f"Erreur lors de la récupération des données : {err}")

def get_student_parcours():
    email = email_entry.get()
    
    try:
        cursor = connexion.cursor()
        query = """
        SELECT p.Niveau_d_études, p.Spécialité, p.UFR, p.Année_de_validation, p.Année_scolaire
        FROM Parcours p
        JOIN InformationsPersonnelles ip ON p.Id = ip.Id
        WHERE ip.Email = %s
        """
        cursor.execute(query, (email,))
        rows = cursor.fetchall()

        if rows:
            text_area.config(state='normal')  # Activer temporairement l'édition
            text_area.delete(1.0, tk.END)  # Vider l'ancienne entrée
            for row in rows:
                text_area.insert(tk.END, f"Niveau d'étude: {row[0]}\nSpécialité: {row[1]}\nUFR: {row[2]}\nAnnée de validation: {row[3]}\nAnnée scolaire: {row[4]}\n\n")
            text_area.config(state='disabled')  # Désactiver l'édition après l'insertion

            update_button_colors(parcours_button)
        else:
            messagebox.showinfo("Information", "Aucun parcours trouvé pour cet étudiant.")

        cursor.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Erreur", f"Erreur lors de la récupération des données : {err}")


# Création de la fenêtre principale
appli = tk.Tk()
appli.title('Plateforme étudiant')
appli.config(bg='#FFFFF0')
appli.geometry('600x800')

# Définir les polices
title_font = font.Font(family="Helvetica", size=16, weight="bold")
text_font = font.Font(family="Verdana", size=12)

# Champs de saisie pour l'email et le mot de passe
email_label = tk.Label(appli, text="Entrez l'email :", bg='#FFFFF0', fg='black', font=title_font)
email_label.pack(pady=5)
email_entry = tk.Entry(appli, width=30, font=text_font)
email_entry.pack(pady=5)

password_label = tk.Label(appli, text="Entrez le mot de passe :", bg='#FFFFF0', fg='black', font=title_font)
password_label.pack(pady=5)
password_entry = tk.Entry(appli, show='*', width=30, font=text_font)
password_entry.pack(pady=10)

# Bouton de connexion
login_button = tk.Button(appli, text="Se connecter", command=get_student_data, font=title_font)
login_button.pack(pady=10)

# Cadre pour le texte d'affichage
text_frame = tk.Frame(appli)
text_area = tk.Text(text_frame, wrap=tk.WORD, height=15, width=70, font=text_font)
text_area.pack()

# Cadre de navigation
nav_frame = tk.Frame(appli)
info_button = tk.Button(nav_frame, text="Information", command=get_student_data, font=title_font)
info_button.pack(side=tk.LEFT, padx=5, pady=5)
parcours_button = tk.Button(nav_frame, text="Parcours", command=get_student_parcours, font=title_font)
parcours_button.pack(side=tk.LEFT, padx=5, pady=5)
autre_button = tk.Button(nav_frame, text="Autre", command=None, font=title_font)  # espace réservé pour une implementation future
autre_button.pack(side=tk.LEFT, padx=5, pady=5)

appli.mainloop()

# Fermer la connexion à la base de données 
if connexion.is_connected():
    connexion.close()
    print("Connexion à la base de données fermée.")
