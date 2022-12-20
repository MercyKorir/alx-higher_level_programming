#!/usr/bin/python3
#list states from hbtn_oe_0_usa
#Usage: ./0select_states.py <mysql username> \
#                           <mysql password> \
#                           <database name>
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM `states`")
    states = curs.fetchall()
    for state in states:
        print(state)
