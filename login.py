import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='nandhaaku',database='eShop')
mycursor=mydb.cursor()


def login():
  n = input('Username: ')
  p = input('Password: ')
  mycursor.execute('SELECT * FROM customers WHERE name = %s AND password = %s', (n, p))
  data=mycursor.fetchone()
  if data:
    print("Welcome to eShop !")
    from order import order
    order(n)

  else:
    print('Invalid id or password')
    e = input('Press y to register: ')
    if e == 'y':
      mycursor.execute('insert into customers(name,password) values(%s,%s)',(n,p))
      mydb.commit()
      print('Your Id and password is registered !')
      from order import order
      order(n)
    else:
      print('Have a nice day!')

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




