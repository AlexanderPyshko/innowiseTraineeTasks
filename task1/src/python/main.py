import logging
from cli import CommandLineInterface

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    cli = CommandLineInterface()
    cli.run()