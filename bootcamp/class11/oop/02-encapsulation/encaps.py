import os
import sqlite3
import psycopg2

class Database:
    def __init__(self, db_type):
        self.db_type = db_type
        self.connection = None

    def connect(self):
        if self.db_type == 'sqlite':
            try:
                file_name = os.getenv('SQLITE_FILE_NAME')
                self.connection = sqlite3.connect(file_name)
                print("SQLite connection established successfully!")
            except sqlite3.Error as e:
                print("Error connecting to SQLite database:", e)
        elif self.db_type == 'postgres':
            try:
                host = os.getenv('PG_HOST')
                port = os.getenv('PG_PORT')
                database = os.getenv('PG_DATABASE')
                user = os.getenv('PG_USER')
                password = os.getenv('PG_PASSWORD')
                self.connection = psycopg2.connect(
                    host=host,
                    port=port,
                    database=database,
                    user=user,
                    password=password
                )
                print("PostgreSQL connection established successfully!")
            except psycopg2.Error as e:
                print("Error connecting to PostgreSQL database:", e)
        else:
            print("Unsupported database type.")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            if self.db_type == 'sqlite':
                print("SQLite connection closed.")
            elif self.db_type == 'postgres':
                print("PostgreSQL connection closed.")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully!")
        except (sqlite3.Error, psycopg2.Error) as e:
            print("Error executing the query:", e)

# Example usage
if __name__ == "__main__":
    db_type = os.getenv('DB_TYPE')  # 'sqlite' or 'postgres'
    
    db = Database(db_type)
    db.connect()

    # Example table creation
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """
    db.execute_query(create_table_query)

    # Example data insertion
    insert_query = """
    INSERT INTO users (name, email) VALUES
    ('João', 'joao@example.com'),
    ('Maria', 'maria@example.com');
    """
    db.execute_query(insert_query)

    db.disconnect()
