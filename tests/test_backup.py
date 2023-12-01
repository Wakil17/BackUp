
import unittest
import subprocess
import sys
import os

class TestBackupExecution(unittest.TestCase):

    def test_script_execution(self):
        script_path = "C:\\Python\\Python311\\Projet Backup\\backup.py"

        try:
            subprocess.run([sys.executable, script_path], check=True)
        except subprocess.CalledProcessError as e:
            self.fail(f"Script execution failed with return code {e.returncode}")

if __name__ == '__main__':
    unittest.main()
