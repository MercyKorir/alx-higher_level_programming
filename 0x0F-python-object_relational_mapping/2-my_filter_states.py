#!/usr/bin/python3
"""takes in arg and displays value in states table"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
    cursor = db.cursor()
    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(
        state_name)
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
