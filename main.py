# This is one of the excellent python projects for beginners.
# Everyone uses a contact book to save contact details, including name, address, phone number,
# and even email address. This is a command-line project where you will design a contact book application
# that users can use to save and find contact details. The application should also allow users to update contact information,
#  delete contacts, and list saved contacts. The SQLite database is the ideal platform for saving contacts.
# To handle a project with Python for beginners can be helpful to build your career with a good start.
import os
import json
import sqlite3

con = sqlite3.connect('contact.db')
cur = con.cursor()


def createTable():
    cur.execute('''CREATE TABLE contact
               (name text, addres text, phone text, email text)''')


def createUser(name, addres, phone, email):

    cur.execute("insert into contact (name, addres, phone, email) values (?, ?, ?, ?)",
                (name, addres, phone, email))
    con.commit()


def showAllTable():
    cur.execute("SELECT * FROM contact")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def deleteUser(name):
    sql_update_query = """DELETE from contact where name= ?"""
    cur.execute(sql_update_query, (name,))
    con.commit()


def updateUser(name, addres, phone, email):
    sql_update_query = """UPDATE contact SET addres = ? ,
                  phone = ? ,
                  email = ?
              WHERE name = ?"""
    cur.execute(sql_update_query, (addres, phone, email, name))


def closeConnection():
    con.close()


def menu():
    print("1 Create User\n2 Delete User\n3 Update user\n4 Show all table")
    choice = int(input("Enter your value: "))
    print(choice)
    if(choice == 1):
        name = input("Enter name: ")
        addres = input("Enter address: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        createUser(name, addres, phone, email)
    elif (choice == 2):
        name = input("Enter name: ")
        deleteUser(name)
    elif (choice == 3):
        name = input("Enter name: ")
        addres = input("Enter address: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        updateUser(name, addres, phone, email)
    elif (choice == 4):
        showAllTable()

        # createUser("John", "Tokyo", "3333", "johny@gmail.com")
        # deleteUser("John")
        #updateUser("Jürgen", "homeless", "3333", "homelessgermannotexist@gmail.com")
menu()
closeConnection()
