import unittest
from src.python.file_loader import FileLoader
import json
import os


class TestFileLoader(unittest.TestCase):

    def setUp(self):
        self.test_data = {
            "id": 1,
            "name": "Test Room"
        }
        self.test_file = 'test_rooms.json'
        with open(self.test_file, 'w') as f:
            json.dump([self.test_data], f)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_json_success(self):
        data = FileLoader.load_json(self.test_file)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], 1)
        self.assertEqual(data[0]['name'], 'Test Room')

    def test_load_json_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            FileLoader.load_json('non_existent_file.json')

    def test_load_json_invalid_format(self):
        invalid_file = 'invalid.json'
        with open(invalid_file, 'w') as f:
            f.write("This is not a valid JSON")

        with self.assertRaises(json.JSONDecodeError):
            FileLoader.load_json(invalid_file)

        os.remove(invalid_file)


if __name__ == '__main__':
    unittest.main()