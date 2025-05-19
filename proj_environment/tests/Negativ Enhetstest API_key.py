import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'src')))

from api_key_manager_class import APIKeyManager

class TestAPIKeyManager(unittest.TestCase):
    def test_get_api_key_non_existent_key(self):
        """
        Test that requesting a non-existent API key raises a KeyError.
        """
        manager = APIKeyManager()
        with self.assertRaises(KeyError) as context:
            manager.get_api_key("NonExistentKey")
        self.assertEqual(str(context.exception), "API key for 'NonExistentKey' not found.")

if __name__ == "__main__":
    unittest.main()