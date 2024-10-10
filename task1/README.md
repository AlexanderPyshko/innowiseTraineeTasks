# Task 1. Python introduction.

## Description
&nbsp;&nbsp;&nbsp;&nbsp;This project allows you to load student and room data from JSON files into a PostgreSQL database, and then extract and format that data in JSON or XML format. The project is organized into several modules, each responsible for specific functionality: database operations, file loading, data formatting, and command-line interface handling.

## Project structure
	
	task1/
	│
	├── config/                     # Configuration files
	│   ├── config.json             # File with data path
	│   └── database_config.json    # Database configuration file
	│
	├── data/                       # Data for loading
	│   ├── rooms.json
	│   └── students.json
	│
	├── src/                        # Source code
	│   ├── python/     
	│   │    ├── cli.py                # Command-line interface module
	│   │    ├── config_loader.py      # Configuration loader module
	│   │    ├── db.py                 # Database module
	│   │    ├── file_loader.py        # File loader module
	│   │    ├── formatter.py          # Data formatting module
	│   │    └── main.py               # Mani program file
	│   └── sql/
	│         ├── create_index.sql              # Create necessary indexes for queries optimization module
	│         ├── create_schema_and_tables.sql  # Create schema and tables module
	│         └── queries.sql                   # Necessary database queries
	├── tests/                    # Tests
	│   ├── test_file_loader.py
	│   └── test_db.py
	│
	├── docker/                   # Docker files
	│   ├── Dockerfile            # Dockerfile for the project
	│   └── docker-compose.yml    # Docker-compose to launch database and app
	├── README.md                 
	├── requirements.txt          
	└── .gitignore

 ## Installation and Setup

Requirements

	•	Python 3.10+
	•	PostgreSQL 13+
	•	Docker (if running via containers)

## Install dependencies
1.	Clone the repository:

    git clone https://github.com/AlexanderPyshko/innowiseTraineeTasks/task1

2.	Navigate to the project directory:
    
    cd task1

3. Install the required dependencies:
    
    
    pip install -r requirements.txt

## Running with docker
1.  Build and start the containers:
    
    
    docker-compose up --build

2.  Application will automatically start.

## Usage example
1.	You can load the data into the database and get it in JSON format:
        
    python src/main.py --db-config config/database_config.json --file-config config/config.json --format json

2.  Or retrieve the data in XML format:
    
    
    python src/main.py --db-config config/database_config.json --file-config config/config.json --format xml

## Modules

[cli.py](./src/python/cli.py)

The command-line interface module manages program execution, data loading, and formatting.

[config_loader.py](./src/python/config_loader.py)

The configuration loader module handles loading files like database settings and data paths.

[db.py](./src/python/db.py)

The database module handles PostgreSQL operations and uses a context manager to manage database connections.

[file_loader.py](./src/python/file_loader.py)

The file loader module loads data from JSON files.

[formatter.py](./src/python/formatter.py)

The data formatting module outputs data in JSON or XML format.

[main.py](./src/python/main.py)

The main program file orchestrates the overall functionality of the application.

[create_schema_and_tables.sql](.src/sql/create_schema_and_tables.sql)

The module with queries to create project schema and tables.

[create_index.sql](./src/sql/create_index.sql)

The create index module handles queries for creating necessary indexes.

[queries.sql](.src/sql/queries.sql)

The file with 5 queries for the database.

## Testing

The project includes tests that can be run with unittest:

    python -m unittest discover -s tests

[test_file_loader.py](./tests/test_file_loade.py)

Test file loader module checks that JSON files are loaded correctly, including error checking.

[test_db.py](./tests/test_db.py)

Test db module tests the connection to the database and execution of queries.

## Logging

Logging is implemented using Python’s built-in logging library. Logs are output to the console, and can be configured to write to a file.

## Docker

The project supports deployment using Docker. With docker-compose, you can quickly set up PostgreSQL and the application:
    
    docker-compose up --build

