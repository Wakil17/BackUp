# tests/test_backup.py

import unittest
import subprocess
import sys

class TestBackupExecution(unittest.TestCase):

    def test_script_execution(self):
        script_path = "C:\\Python\\Python311\\Projet Backup\\backup.py"

        # Exécutez le script et ne vérifiez pas le code de retour
        subprocess.run([sys.executable, script_path])

if __name__ == '__main__':
    unittest.main()
