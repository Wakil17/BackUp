import shutil
import getpass
import os
import sys
import ctypes
import tkinter as tk
import subprocess

#Si le script n'est pas lancé en tant qu'admin, on demande les autorisation nécessaires
if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, "c:/Python/Python311/executable.py", None, 1)
    

#Fonction pricipale: Pour chaque éléments de la liste on copie le dossier source dans le dossier destination
def main():
    for i in range(len(sources) - 1):
        copy_folder(sources[i], destinations[i])

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.grid()
fenetre.title("Transfert des dossiers du répertoire personnel")
fenetre.configure(padx=50, pady=50)
# Bouton pour lancer le script
bouton_lancer = tk.Button(fenetre, text="Lancer le transfert", command=main)


# Lance le script en tant qu'administrateur si ce n'est pas déjà le cas


            



def copy_folder(source_folder, destination_folder):

    try:
        # Création du dossier destination 
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            print(f"Le dossier '{destination_folder}' a été créé.")

        # Copie des dossiers sources dans les dossiers de destinations
        shutil.copytree(source_folder, destination_folder, dirs_exist_ok=True)
        print(f"Le dossier '{source_folder}' a été copié dans '{destination_folder}'.")
    except Exception as e:
        print("Une erreur s'est produite lors de la copie du dossier :", str(e))












# Récupération du nom utilisateur et création de listes sources et destination
username = getpass.getuser()
sources = []
destinations = []

#Chemins Documents
sources.append('C:\\Users\\' + username + '\\Documents\\')
destinations.append('C:\\' + username + '_BackUp\\Documents_' + username + '_Backup')


#Chemin Images
sources.append('C:\\Users\\' + username + '\\Pictures\\')
destinations.append('C:\\' + username + '_BackUp\\Images_' + username + '_Backup')


#Chemin Vidéos
sources.append('C:\\Users\\' + username + '\\Videos\\')
destinations.append('C:\\' + username + '_BackUp\\Vidéos_' + username + '_Backup')

#Chemin Musique
sources.append('C:\\Users\\' + username + '\\Music\\')
destinations.append('C:\\' + username + '_BackUp\\Musique_' + username + '_Backup')

#Chemins Favoris
sources.append('C:\\Users\\' + username + '\\Favorites\\')
destinations.append('C:\\' + username + '_BackUp\\Favoris_' + username + '_Backup')

#Chemin Téléchargements
sources.append('C:\\Users\\' + username + '\\Downloads\\')
destinations.append('C:\\' + username + '_BackUp\\Téléchargements_' + username + '_Backup')


fenetre.mainloop
