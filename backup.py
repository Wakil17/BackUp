import shutil
import getpass
import os
import ctypes
import subprocess
import sys

def start():
    for i in range(len(sources) - 1):
        copy_folder(sources[i], destinations[i])

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

# Chemins Documents
sources.append('C:\\Users\\' + username + '\\Documents\\')
destinations.append('C:\\' + username + '_BackUp\\Documents_' + username + '_Baaackup')

# Chemin Images
sources.append('C:\\Users\\' + username + '\\Pictures\\')
destinations.append('C:\\' + username + '_BackUp\\Images_' + username + '_Backup')

# Chemin Vidéos
sources.append('C:\\Users\\' + username + '\\Videos\\')
destinations.append('C:\\' + username + '_BackUp\\Vidéos_' + username + '_Backup')

# Chemin Musique
sources.append('C:\\Users\\' + username + '\\Music\\')
destinations.append('C:\\' + username + '_BackUp\\Musique_' + username + '_Backup')

# Chemins Favoris
sources.append('C:\\Users\\' + username + '\\Favorites\\')
destinations.append('C:\\' + username + '_BackUp\\Favoris_' + username + '_Backup')

# Chemin Téléchargements
sources.append('C:\\Users\\' + username + '\\Downloads\\')
destinations.append('C:\\' + username + '_BackUp\\Téléchargements_' + username + '_Backup')

# Exécutez le script en tant qu'administrateur avec subprocess
script_path = "c:/Python/Python311/Projet Backup/backup.py"
subprocess.run(["runas", "/user:Administrator", sys.executable, script_path])

# Lancez la copie des dossiers si l'exécution ci-dessus est en mode administrateur
start()
