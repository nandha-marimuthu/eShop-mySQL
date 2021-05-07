import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='nandhaaku',database='eShop')
mycursor=mydb.cursor()
import pandas as pd

def orderDetails():
  od = input('View Orders(y/n): ')
  if od == 'y':
    mycursor.execute('select * from orderDetails')
    data = mycursor.fetchall()
    a = pd.DataFrame(data)
    a.columns = ['id','name','item','type','qty','place','bill']
    print(a)

def place():
  mycursor.execute('select * from orderDetails')
  data = mycursor.fetchall()
  a = pd.DataFrame(data)
  a.columns = ['id','name','item','type','qty','place','bill']
  print(a['place'].value_counts())

def type():
  print('No of item sold Categorywise:')
  mycursor.execute('select sum(qty) from orderDetails group by type')
  d = mycursor.fetchall()
  print('Electronics - %d\nPhones - %d\nLaptops - %d'%(d[0][0],d[1][0],d[2][0]))

def item():
  print('No of items sold: ')
  mycursor.execute('select item,sum(qty) from orderDetails group by item')
  data = mycursor.fetchall()
  a = pd.DataFrame(data)
  a.columns = ['item','sold']
  print(a)

def add():
  print('Enter what appliance stock you gonna refill')
  o = int(input("1 For Electronics\n2 For Laptops\n3 For Phones\nEnter: "))
  if (o==1):
    mycursor.execute('update e set stock = 100')
    mydb.commit()
  elif(o==2):
    mycursor.execute('update l set stock = 100')
    mydb.commit()
  elif(o==3):
    mycursor.execute('update p set stock = 100')
    mydb.commit()
  else:
    print('Invalid code')
  print('stock refilled')

def ad():
  while True:
    a = int(input('1 For total order details\n2 For Categorywise sales\n3 For Itemwise sale\n4 For region wise sales\n5 for Refill stock\n6 For exit '))
    if a==1:
      orderDetails()
    elif a==2:
      type()
    elif a==3:
      item()
    elif a==4:
      place()
    elif a==5:
      add()
    elif a==6:
      break
    else:
      break



