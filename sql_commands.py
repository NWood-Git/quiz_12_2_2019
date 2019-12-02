
# * Write a python script that runs the following SQL commands:

#     * Write SQL to look up Ntumwa's employee number

#     * Write SQL to make Kieth Toda the manager of New York.

#     * Write SQL to select all employees in Texas. You should use the branch's state 
# value and a JOIN. You may use known foreign key values in the employees table
# for partial credit.

#     * Write SQL to delete John.

import sqlite3


def select_id(first_name):
    with sqlite3.connect('company.db') as connection: 
        cursor = connection.cursor()
        cursor.execute("SELECT id_num FROM employees WHERE first_name = ?",(first_name,))
        result = cursor.fetchone() #for jsut one row use this
        for item in result:
            print(item)

def make_manager(id_num):
        with sqlite3.connect('company.db') as connection: 
            cursor = connection.cursor()
            cursor.execute("UPDATE employees SET is_manager='Y' WHERE id_num=?",(id_num,))
            return "done"

def delete_account(id_num):
    with sqlite3.connect('company.db') as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM employees WHERE id_num=?",(id_num,))
        return "done"


def select_emp_state(state):
    with sqlite3.connect('company.db') as connection: 
        cursor = connection.cursor()
        cursor.execute("SELECT * from employees JOIN branches ON employees.branch_pk = branches.pk WHERE branches.state =?;",(state,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)


#select_id("Ntumwa")
#print(make_manager('301')) #keith's is number
#print(delete_account("302")) #302 is John's ID number
#select_emp_state('TX')
