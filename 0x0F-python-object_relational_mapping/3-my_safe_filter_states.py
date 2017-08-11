#!/usr/bin/python3
"""
lists all states from a database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.Connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    cur = db.cursor()
    cur.execute("""
    SELECT * FROM states
    WHERE BINARY states.name = %s
    ORDER BY states.id ASC
    """, (argv[4].split("'")[0], ))

    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
