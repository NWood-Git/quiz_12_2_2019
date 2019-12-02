# import sqlite3

# def create_branch(city, state):
#     with sqlite3.connect('company.db') as connection:
#         cursor = connection.cursor()
#         sql_data = {"city" : city,
#                     "state" : state}
#         INSERT_SQL = """INSERT INTO branches(city, state)
#                         VALUES (:city, :state)"""
#         cursor.execute(INSERT_SQL, sql_data)
#         return "done"

# def add_employee(first_name, last_name, id_num, is_manager, branch_pk):
#     with sqlite3.connect(company.db) as connection:
#         cursor = connection.cursor()

#####
import sqlite3
import os

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "company.db"
DBPATH = os.path.join(DIRPATH,DBFILENAME)

def seed(dbpath):
    branches = [
        ("Houston","TX"),  # pk 1
        ("Dallas","TX"),   # pk 2
        ("New York","NY")] # pk 3

    employees = [
        ("Sean", "Jarrett", "201", "N", 2),
        ("Gail", "Polk", "101", "N", 1),
        ("Kevin", "Sinha", "102", "N", 1),
        ("Kieth", "Toda", "301", "N", 3),
        ("John", "Nielson", "302", "N", 3),
        ("Ntumwa", "Kisalita", "303", "N", 3)]

    with sqlite3.connect(dbpath) as connection:
        cursor = connection.cursor()
        SQL = """INSERT INTO branches(city, state) VALUES(?,?);"""
        for branch in branches:
            cursor.execute(SQL,branch)

    with sqlite3.connect(dbpath) as connection:
        cursor = connection.cursor()
        SQL = """INSERT INTO employees(first_name, last_name, id_num, is_manager, branch_pk) VALUES(?,?,?,?,?);"""
        for employee in employees:
            cursor.execute(SQL,employee)


if __name__ == "__main__":
    seed(DBPATH)