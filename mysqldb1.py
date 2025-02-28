import mysql.connector
from mysql.connector import Error

class DatabaseConfig:
    def __init__(self):
        self.host = 'localhost'        # Change to your MySQL server address if remote
        self.database = 'your_database_name'
        self.user = 'your_username'
        self.password = 'your_password'

    def create_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if connection.is_connected():
                print("Connection to MySQL database successful")
        except Error as e:
            print(f"Error: '{e}' occurred")
        return connection

# Usage example
if __name__ == "__main__":
    db_config = DatabaseConfig()
    connection = db_config.create_connection()
    if connection:
        connection.close()
        print("Connection closed")
