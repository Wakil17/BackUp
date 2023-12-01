# tests/test_backup.py

import unittest
import os

class TestBackupExecution(unittest.TestCase):

    def test_script_not_empty(self):
        # Chemin vers le fichier backup.py
        script_file_path = r"C:\Python\Python311\Projet Backup\backup.py"

        # Vérifiez que le fichier backup.py existe
        self.assertTrue(os.path.exists(script_file_path), "Le fichier backup.py n'existe pas.")

        # Vérifiez que le fichier backup.py n'est pas vide
        file_size = os.path.getsize(script_file_path)
        self.assertGreater(file_size, 0, "Le fichier backup.py est vide.")

if __name__ == '__main__':
    unittest.main()
