import json
import os
import unittest

from src.Definitions.definitions import ANNOUNCEMENTS_PATH


class TestAnnouncementFiles(unittest.TestCase):

    def test_daily_announcements_file(self):
        file_path = f'{ANNOUNCEMENTS_PATH}/daily_announcements.json'
        self.assertTrue(os.path.exists(file_path), "File does not exist")

        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                self.assertIsInstance(data, list, "Data is not a list")
                self.assertTrue(all(isinstance(item, str) for item in data), "Not all items in the list are strings")
                for item in data:
                    self.assertEqual(item.count("{"), 3, "String does not contain three placeholders")
            except json.JSONDecodeError:
                self.fail("File is not valid JSON")

    def test_add_announcements_file(self):
        file_path = f'{ANNOUNCEMENTS_PATH}/add_announcements.json'
        self.assertTrue(os.path.exists(file_path), "File does not exist")

        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                self.assertIsInstance(data, list, "Data is not a list")
                self.assertTrue(all(isinstance(item, str) for item in data), "Not all items in the list are strings")
                for item in data:
                    self.assertEqual(item.count("{"), 2, "String does not contain two placeholders")
            except json.JSONDecodeError:
                self.fail("File is not valid JSON")

    def test_remove_announcements_file(self):
        file_path = f'{ANNOUNCEMENTS_PATH}/remove_announcements.json'
        self.assertTrue(os.path.exists(file_path), "File does not exist")

        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                self.assertIsInstance(data, list, "Data is not a list")
                self.assertTrue(all(isinstance(item, str) for item in data), "Not all items in the list are strings")
                for item in data:
                    self.assertEqual(item.count("{"), 1, "String does not contain two placeholders")
            except json.JSONDecodeError:
                self.fail("File is not valid JSON")


if __name__ == '__main__':
    unittest.main()
