import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(ROOT_DIR)
SAVE_FILE_DIR = os.path.join(PARENT_DIR, 'pw.json')

def load_file():
    print(ROOT_DIR)

load_file()