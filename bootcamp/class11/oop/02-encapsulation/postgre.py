import psycopg2

class PostgresDatabase:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connection established successfully!")
        except psycopg2.Error as e:
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
        except psycopg2.Error as e:
            print("Error executing the query:", e)


# Example usage
if __name__ == "__main__":
    host = 'localhost'
    port = '5432'
    database_name = 'your_database_name'
    user = 'your_user'
    password = 'your_password'
    
    db = PostgresDatabase(host, port, database_name, user, password)
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