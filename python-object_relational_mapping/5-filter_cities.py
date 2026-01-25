#!/usr/bin/python3
"""List all cities of a given state (SQL injection safe)."""

import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    # Safe from SQL injection using parameterized query
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()
    # Extract city names and join with comma + space
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    cursor.close()
    db.close()
