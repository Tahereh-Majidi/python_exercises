import mysql.connector

def create_or_connect_to_db():
    # Define the database configuration
    config = {
      'user': input('Enter your MySQL username: '),
      'password': input('Enter your MySQL password: '),
      'host': input('Enter your MySQL host (usually "localhost"): '),
      'raise_on_warnings': True
    }

    # Connect to the MySQL server
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # Define the name of the database you want to create or connect to
    database_name = input('Enter your database name: ')

    # Check if the database already exists
    cursor.execute("SHOW DATABASES LIKE '{}'".format(database_name))
    result = cursor.fetchone()

    # If the database doesn't exist, create it
    if not result:
        cursor.execute("CREATE DATABASE {}".format(database_name))
        print("Database created successfully.")
    else:
        print("Database already exists.")

    # Connect to the database
    cnx.database = database_name
    print("Connected to database: {}".format(database_name))

    # Close the cursor and return the connection object
    cursor.close()
    return cnx