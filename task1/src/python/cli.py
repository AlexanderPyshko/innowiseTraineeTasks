import argparse
import logging
from db import Database
from file_loader import FileLoader
from formatter import DataFormatter
from datetime import datetime

class CommandLineInterface:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Process student and room data.')
        self.parser.add_argument('--db-config', type=str, required=True, help='Path to database configuration file')
        self.parser.add_argument('--file-config', type=str, required=True, help='Path to file paths configuration file')
        self.parser.add_argument('--format', type=str, choices=['json', 'xml'], required=True, help='Output format')

    def run(self):
        args = self.parser.parse_args()

        db_config = FileLoader.load_json(args.db_config)
        file_config = FileLoader.load_json(args.file_config)

        students_file = file_config['paths']['students']
        rooms_file = file_config['paths']['rooms']

        self.load_data(db_config, students_file, rooms_file)
        self.retrieve_and_format_data(db_config, args.format)

    def load_data(self, db_config, students_file, rooms_file):
        with Database(host=db_config['host'], database=db_config['database'], user=db_config['user'], password=db_config['password']) as cursor:
            rooms = FileLoader.load_json(rooms_file)
            students = FileLoader.load_json(students_file)

            try:
                for room in rooms:
                    cursor.execute(
                        "INSERT INTO schematask1.rooms (id, name) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING",
                        (room['id'], room['name'])
                    )

                for student in students:
                    cursor.execute(
                        """
                        INSERT INTO schematask1.students (id, name, birthday, sex, room_id) 
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (id) DO NOTHING
                        """,
                        (
                            student['id'],
                            student['name'],
                            datetime.strptime(student['birthday'][:10], '%Y-%m-%d'),
                            student['sex'],
                            student['room']
                        )
                    )

                logging.info("Loaded data successfully")
            except Exception as e:
                logging.error(f'Failed to load data: {e}')

    def retrieve_and_format_data(self, db_config, output_format):
        with Database(host=db_config['host'], database=db_config['database'], user=db_config['user'], password=db_config['password']) as cursor:
            try:
                cursor.execute("SELECT * FROM schematask1.rooms")
                rooms = cursor.fetchall()

                cursor.execute("SELECT * FROM schematask1.students")
                students = cursor.fetchall()

                room_columns = [desc[0] for desc in cursor.description]
                room_data = [dict(zip(room_columns, row)) for row in rooms]

                student_columns = [desc[0] for desc in cursor.description]
                student_data = [dict(zip(student_columns, row)) for row in students]

                data = {
                    'rooms': room_data,
                    'students': student_data
                }

                if output_format == 'json':
                    print(DataFormatter.format_as_json(data))
                elif output_format == 'xml':
                    print(DataFormatter.format_as_xml(data))
            except Exception as e:
                logging.error(f'Failed to retrieve data: {e}')