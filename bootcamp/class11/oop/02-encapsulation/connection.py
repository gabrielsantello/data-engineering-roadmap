from .sqlite import SQLiteDatabase
from .postgre import PostgresDatabase
from .encaps import Database

########## SQLITE #############

file_name = "example.db"
sql_db = SQLiteDatabase(file_name)
sql_db.connect()

# Inserting data into the table
insert_query = """
INSERT INTO users (name, email) VALUES
('João', 'joao@example.com'),
('Maria', 'maria@example.com');
"""
sql_db.execute_query(insert_query)

sql_db.disconnect()

########## POSTGRE #############

host = 'localhost'
port = '5432'
database_name = 'your_database_name'
user = 'your_user'
password = 'your_password'

postgre_db = PostgresDatabase(host, port, database_name, user, password)
postgre_db.connect()

insert_query = """
INSERT INTO users (name, email) VALUES
('João', 'joao@example.com'),
('Maria', 'maria@example.com');
"""
postgre_db.execute_query(insert_query)

postgre_db.disconnect()

########## ENCAPSULATED #############
db = Database("database_type")
db.connect()

insert_query = """
INSERT INTO users (name, email) VALUES
('João', 'joao@example.com'),
('Maria', 'maria@example.com');
"""
db.execute_query(insert_query)

db.disconnect()