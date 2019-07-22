import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

database_path = os.path.join(BASE_DIR, "database")

school_db_file = os.path.join(database_path, "school")