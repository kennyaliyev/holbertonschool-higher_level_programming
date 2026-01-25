#!/usr/bin/env python3
"""List all states from the database hbtn_0e_0_usa."""

import sys
import MySQLdb


if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor and execute query
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch and display results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Clean up
    cursor.close()
    db.close()
