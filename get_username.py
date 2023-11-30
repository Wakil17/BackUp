import shutil
import getpass
import os
import sys
import ctypes
import tkinter as tk
import subprocess


def start():

    # Appel de la fonction pour copier le dossier
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, "c:/Python/Python311/get_username.py", None, 1)
    else:
    #for i in range(len(sources)):
        #copy_folder(sources[i], destinations[i])

        for i in range(len(sources) - 1):
            copy_folder(sources[i], destinations[i])


# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Interface de lancement")

# Créer un bouton pour lancer le script
bouton_lancer = tk.Button(fenetre, text="Lancer le script", command=start)
bouton_lancer.pack(padx=20, pady=20)

def copy_folder(source_folder, destination_folder):

    try:
        # Créez le dossier de destination
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            print(f"Le dossier '{destination_folder}' a été créé.")

        # Utilisez la fonction shutil.copytree() pour copier le dossier source dans le dossier de destination
        shutil.copytree(source_folder, destination_folder, dirs_exist_ok=True)
        print(f"Le dossier '{source_folder}' a été copié dans '{destination_folder}'.")
    except Exception as e:
        print("Une erreur s'est produite lors de la copie du dossier :", str(e))


# Spécifiez les chemins complets des dossiers source et de destination
username = getpass.getuser()
sources = []
destinations = []

#Chemins Documents
sources.append('C:\\Users\\' + username + '\\Documents\\')
destinations.append('C:\\' + username + '_BackUp\\Documents_' + username + '_Baaackup')


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
destinations.append('D:\\' + username + '_BackUp\\Téléchargements_' + username + '_Backup')


fenetre.mainloop()