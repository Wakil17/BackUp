import unittest
import os
from backup import sources, destinations  # Import des chemins

class TestPaths(unittest.TestCase):

    def test_paths_match_main_branch(self):
        expected_sources = [
            'C:\\Users\\username\\Documents\\',
            'C:\\Users\\username\\Pictures\\',
            'C:\\Users\\username\\Videos\\',
            'C:\\Users\\username\\Music\\',
            'C:\\Users\\username\\Favorites\\',
            'C:\\Users\\username\\Downloads\\',
        ]

        expected_destinations = [
            'C:\\username_BackUp\\Documents_username_Baaackup',
            'C:\\username_BackUp\\Images_username_Backup',
            'C:\\username_BackUp\\Vidéos_username_Backup',
            'C:\\username_BackUp\\Musique_username_Backup',
            'C:\\username_BackUp\\Favoris_username_Backup',
            'C:\\username_BackUp\\Téléchargements_username_Backup',
        ]

        # Vérifier que les chemins correspondent à ceux de la branche main
        self.assertEqual(sources, expected_sources)
        self.assertEqual(destinations, expected_destinations)

if __name__ == '__main__':
    unittest.main()
