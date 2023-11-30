import shutil
import getpass
import os
import sys
import ctypes

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

#Chemins Documents
source_documents = 'C:\\Users\\' + username + '\\Documents\\'
destination_documents = 'C:\\ESGI\\Langage C\\Documents_' + username + '_Backup'

#Chemins Favoris
source_favoris = 'C:\\Users\\' + username + '\\Favorites\\'
destination_favoris = 'C:\\ESGI\\Langage C\\Favoris_' + username + '_Backup'

#Chemin Images
source_images = 'C:\\Users\\' + username + '\\Pictures\\'
destination_images = 'C:\\ESGI\\Langage C\\Images_' + username + '_Backup'

#Chemin Téléchargements
source_telechargements = 'C:\\Users\\' + username + '\\Downloads\\'
destination_telechargements = 'C:\\ESGI\\Langage C\\Téléchargements_' + username + '_Backup'


#Chemin Vidéos
source_videos = 'C:\\Users\\' + username + '\\Videos\\'
destination_videos = 'C:\\ESGI\\Langage C\\Téléchargements_' + username + '_Backup'

#Chemin Musique
source_musique = 'C:\\Users\\' + username + '\\Music\\'
destination_musique = 'C:\\ESGI\\Langage C\\Musique_' + username + '_Backup'


# Appel de la fonction pour copier le dossier

if ctypes.windll.shell32.IsUserAnAdmin():
    copy_folder(source_documents, destination_documents)
else:
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, "c:/Python/Python311/copie_dossiers.py", None, 1)