#!/usr/bin/python3
"""This script takes in name of state as arg and
lists all cities of that state using db hbtn_0e_4_usa
"""
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
    curs = db.cursor()
    state_name = sys.argv[4]
    query = "SELECT cities.name FROM cities JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY cities.id ASC;"
    curs.execute(query, (state_name,))
    cities = curs.fetchall()
    if cities:
        for i, city in enumerate(cities):
            if i == len(cities) - 1:
                print(city[0], end="\n")
            else:
                print(city[0], end=", ")
    else:
        print()
    curs.close()
    db.close()
