import mysql.connector

def conect():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Myhealth"
  )
    return mydb