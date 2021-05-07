import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='nandhaaku',database='eShop')
mycursor=mydb.cursor()
def sales():
  od = input('View Orders(y/n): ')
  if od == 'y':
    mycursor.execute('select * from orderDetails')
    data = mycursor.fetchall()
    for i in data:
      print(data)
admin()