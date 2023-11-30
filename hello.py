import shutil
import getpass
import os
import sys
import ctypes
from tkinter import messagebox

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

def start():
    # Spécifiez les chemins complets des dossiers source et de destination
    username = getpass.getuser()
    sources = [
        'C:\\Users\\' + username + '\\Documents\\',
        'C:\\Users\\' + username + '\\Pictures\\',
        'C:\\Users\\' + username + '\\Videos\\',
        'C:\\Users\\' + username + '\\Music\\',
        'C:\\Users\\' + username + '\\Favorites\\',
        'C:\\Users\\' + username + '\\Downloads\\',
    ]
    destinations = [
        'C:\\' + username + '_BackUp\\Documents_' + username + '_Backup',
        'C:\\' + username + '_BackUp\\Images_' + username + '_Backup',
        'C:\\' + username + '_BackUp\\Vidéos_' + username + '_Backup',
        'D:\\' + username + '_BackUp\\Musique_' + username + '_Backup',
        'D:\\' + username + '_BackUp\\Favoris_' + username + '_Backup',
        'D:\\' + username + '_BackUp\\Téléchargements_' + username + '_Backup',
    ]

    for i in range(len(sources)):
        copy_folder(sources[i], destinations[i])

    messagebox.showinfo("Info", "La copie des fichiers est terminée.")

if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, "c:/Python/Python311/Projet Backup/hello.py", None, 1)
else:
    start()
