# Hector Lara Module 8.2

import mysql.connector

config = {
    'user': 'root',
    'password': 'Danratherisaturnip12',
    'host': 'localhost',
    'database': 'movies',
    'raise_on_warnings': True
}


def show_films(cursor, title):
    """
    Function to execute an INNER JOIN on the film, genre, and studio tables,
    then display the results with formatted output.
    """
    # INNER JOIN query to fetch film details with genre and studio names
    query = """
        SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id;
    """

    cursor.execute(query)
    films = cursor.fetchall()

    print("\n-- {} --".format(title))

    # Iterate over the film data set and display the results
    for film in films:
        print(f"Film Name: {film[0]}")
        print(f"Director: {film[1]}")
        print(f"Genre: {film[2]}")
        print(f"Studio Name: {film[3]}\n")


def main():
    try:
        # Establish connection to database
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Display the films before any changes
        show_films(cursor, "DISPLAYING FILMS BEFORE INSERT")

        # Insert a new film record into the film table (make sure the studio and genre exist)
        add_film_query = """
                    INSERT INTO film (film_name, film_director, genre_id, studio_id, film_runtime, film_releaseDate)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """
        new_film = ("Inception", "Christopher Nolan", 1, 3, 148,
                    '2010-07-16')
        cursor.execute(add_film_query, new_film)
        connection.commit()

        # Display films after the insertion
        show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

        # Update the genre of the film "Alien" to be a Horror film
        update_film_query = """
            UPDATE film
            SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
            WHERE film_name = 'Alien';
        """
        cursor.execute(update_film_query)
        connection.commit()

        # Display the films after updating Alien's genre
        show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

        # Delete the film "Gladiator"
        delete_film_query = """
            DELETE FROM film
            WHERE film_name = 'Gladiator';
        """
        cursor.execute(delete_film_query)
        connection.commit()

        # Display films after deletion
        show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

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
