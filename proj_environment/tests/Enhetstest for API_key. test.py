import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'src')))

from API_Key_Manager_class import APIKeyManager

class TestAPIKeyManager(unittest.TestCase):

    def setUp(self):
        """Set up a fresh instance of APIKeyManager before each test."""
        self.manager = APIKeyManager()
   
    def test_get_key_valid(self):
        """Test that a valid API key is returned."""
        frost_key = self.manager.get_api_key("Frost")
        self.assertEqual(frost_key, "2e243d34-57bc-42b4-8095-239991af5353")
        opencage_key = self.manager.get_api_key("Opencage")
        self.assertEqual(opencage_key, "e9a6e9b1b9be44fab4720c2c96ae9c48")
    
    def test_get_key_not_valid(self):
        """Test that a KeyError is raised for an invalid key."""
        with self.assertRaises(KeyError):
            self.manager.get_api_key("InvalidKey")

if __name__ == '__main__':
    unittest.main()