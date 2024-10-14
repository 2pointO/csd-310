# Hector Lara Module 7.2
# Table Queries

import mysql.connector
from mysql.connector import errorcode


config = {
    'user': 'root',  # Replace with your MySQL username
    'password': 'Danratherisaturnip12',  # Replace with your MySQL password
    'host': 'localhost',  # Hostname or IP address
    'database': 'movies',  # Replace with your database name
    'raise_on_warnings': True
}

def main():
    # Establish connection to the database
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Query to select all fields from the studio table
        print("-- DISPLAYING Studio RECORDS --")
        cursor.execute("SELECT studio_id, studio_name FROM studio;")
        studios = cursor.fetchall()
        for studio in studios:
            print(f"Studio ID: {studio[0]}")
            print(f"Studio Name: {studio[1]}")
            print()  # Blank line for formatting

        # Query to select all fields from the genre table
        print("-- DISPLAYING Genre RECORDS --")
        cursor.execute("SELECT genre_id, genre_name FROM genre;")
        genres = cursor.fetchall()
        for genre in genres:
            print(f"Genre ID: {genre[0]}")
            print(f"Genre Name: {genre[1]}")
            print()  # Blank line for formatting

        # Query to select movie names with a runtime of less than two hours
        print("-- DISPLAYING Movies with Runtime Less Than 2 Hours --")
        cursor.execute("SELECT film_name FROM film WHERE film_runtime < 120;")  # Updated to use 'film_name'
        short_movies = cursor.fetchall()
        for movie in short_movies:
            print(f"Movie Name: {movie[0]}")
            print()  # Blank line for formatting

        # 4. Query to get a list of film names, and directors grouped by director
        print("-- DISPLAYING Films Grouped by Director --")
        cursor.execute("SELECT film_director, GROUP_CONCAT(film_name SEPARATOR ', ') FROM film GROUP BY film_director;")
        films_by_director = cursor.fetchall()
        for director in films_by_director:
            print(f"Director: {director[0]}")
            print(f"Films: {director[1]}")
            print()  # Blank line for formatting

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    main()