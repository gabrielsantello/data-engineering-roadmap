import sqlite3

class SQLiteDatabase:
    def __init__(self, file_name):
        self.file_name = file_name
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.file_name)
            print("Connection established successfully!")
        except sqlite3.Error as e:
            print("Error connecting to the database:", e)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully!")
        except sqlite3.Error as e:
            print("Error executing the query:", e)


# Example usage
if __name__ == "__main__":
    file_name = "example.db"
    db = SQLiteDatabase(file_name)
    db.connect()

    # Creating a table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """
    db.execute_query(create_table_query)

    # Inserting data into the table
    insert_query = """
    INSERT INTO users (name, email) VALUES
    ('João', 'joao@example.com'),
    ('Maria', 'maria@example.com');
    """
    db.execute_query(insert_query)

    db.disconnect()