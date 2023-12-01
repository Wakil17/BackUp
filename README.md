### Objectif du Projet

Ce projet a été mis en place pour effectuer une sauvegarde des données utilisateur des dossiers non partagés des postes utilisateurs sur une clé USB afin de les restorer sur un autre poste. 

Il évite de copier/coller les dossiers à la main dans la clef  USB et permet d'automatiser une tâche répétitive et fréquament réalisée en support informatique par un script. 

### Guide d'utilisation 

Le script backup.py est le script à executer en premier il copie les données du poste vers la clef USB.

Pour le dévelopement les dossiers sont copier dans un dossier à la racine de C nommé *username_backup*.

Vous pouvez modifier les chemins destinations pour vos tests en local mais lorsque vous pushez sur la branche principale il faudra que les chemins soient identique à ceux de la branche main pour facilité la prise en main des autres collaborateurs.  

Le script restoreBackup.py sert à copier les données de la clef vers les bons dossiers du nouveau poste.

Idéalement il faudrait transformer les script .py en executables .exe pour qu'ils puissent se lancer sur n'importe quel poste depuis la clef USB sans avoir besoin d'installer python. 

Libre à vous d'ajouter des améliorations et de remonter/résoudre les bugs rencontrés. 

### Adapter et lancer les scripts sur vôtre machine. 

N'oubliez pas de modifier le chemin de la variable script_path à la ligne 55 du scrpit backup.py pour que le code puisse s'executer avec les droits administrateurs et créer/déplacer des dossiers/fichiers.

Pour pouvoir exécuter les scripts, vous devrez installer Python et saisir la ligne de commande ci-dessous dans votre terminal en l'adaptant le chemin à votre arborescence :

```
c:/Python/Python311/python.exe "c:/Python/Python311/Projet Backup/backup.py"
```
