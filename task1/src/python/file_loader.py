import json
import logging

class FileLoader:
    @staticmethod
    def load_json(file_path):
        try:
            with open(file_path, 'r') as file:
                logging.info(f"Loading JSON file from {file_path}")
                return json.load(file)
        except FileNotFoundError:
            logging.error(f"File {file_path} not found")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode JSON from {file_path}: {e}")
            raise