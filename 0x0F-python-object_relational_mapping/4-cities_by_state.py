#!/usr/bin/python3
"""lists all cities from db hbtn_0e_4_usa"""
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
    curs.execute("SELECT cities.id, cities.name, states.name \
                FROM cities INNER JOIN states ON cities.state_id=states.id \
                ORDER BY cities.id ASC")
    cities = curs.fetchall()
    for city in cities:
        print(city)
    curs.close()
    db.close()
