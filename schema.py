import sqlite3
import os

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "company.db"
DBPATH = os.path.join(DIRPATH, DBFILENAME)

def schema(DBPATH):
    with sqlite3.connect(DBPATH) as conn:
        cur = conn.cursor()

        SQL = "DROP TABLE IF EXISTS branches;"
        cur.execute(SQL)

        SQL = """CREATE TABLE branches(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            city VARCHAR(128),
            state VARCHAR (128)
            );"""
        cur.execute(SQL)

        SQL = "DROP TABLE IF EXISTS employees;"
        cur.execute(SQL)

        SQL = """CREATE TABLE employees(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(128),
            last_name VACHAR(128),
            id_num VARCHAR(6),
            is_manager VARCHAR (3),
            branch_pk INTERGER (128),
            FOREIGN KEY (branch_pk) REFERENCES branches(pk)
            );"""
        cur.execute(SQL)


if __name__ == "__main__":
    schema(DBPATH)