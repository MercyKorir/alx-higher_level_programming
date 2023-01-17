#!/usr/bin/python3
""" Lists all states from database hbtn_0e_0_usa."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM `states`")
    states = curs.fetchall()
    for state in states:
        print(state)
