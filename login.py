import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='nandhaaku',database='eShop')
mycursor=mydb.cursor()
from order import order

def login():
  n = input('Username: ')
  p = input('Password: ')
  mycursor.execute('SELECT * FROM customers WHERE name = %s AND password = %s', (n, p))
  data=mycursor.fetchone()
  if data:
    print("Welcome to eShop !")
    order(n)

  else:
    print('Invalid id or password')

def admin():
  n = input('Username: ')
  p = input('Password: ')
  mycursor.execute('SELECT * FROM admin WHERE name = %s AND pass = %s', (n, p))
  data=mycursor.fetchone()
  if data:
    print("Welcome admin !")
    from admin import ad
    ad()
  else:
    print('Invalid id or password')



