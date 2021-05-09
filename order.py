import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='nandhaaku',database='eShop')
mycursor=mydb.cursor()

def order(n):
  name = n
  place = str(input("Enter where are you from: "))

  print('----------------------------------------------------------------')
  o = int(input("1 For Electronics\n2 For Laptops\n3 For Phones\nEnter: "))
  if (o==1):
    mycursor.execute('select * from e')
    ty = 'e'
  elif(o==2):
    mycursor.execute('select * from l')
    ty = 'l'
  elif(o==3):
    mycursor.execute('select * from p')
    ty = 'p'
  else:
    print('Invalid code')

  data = mycursor.fetchall()
  print("id     name    price    stock")
  print('----------------------------------------------------------------')
  for i in data:
    print(i[0],'   ',i[1],'   ',i[2],'   ',i[3])
  print('----------------------------------------------------------------')

  ic = int(input('Enter name of the appliance: '))
  qty = int(input('Number of item you want: '))
  for i in data:
    if i[0]==ic:
        item = i[1]
        avil = i[3]-qty
        bill = qty*i[2]
  # print(item,qty,bill,avil)
  if avil>0:
    if (o==1):
      mycursor.execute(' update e set stock = %s where id = %s',(avil,ic))
      mydb.commit()
    elif(o==2):
      mycursor.execute(' update l set stock = %s where id = %s',(avil,ic))
      mydb.commit()
    elif(o==3):
      mycursor.execute(' update p set stock = %s where id = %s',(avil,ic))
      mydb.commit()
    off=input('Enter the offer Code: ')
    offer=['FAN50','LIGHT10','MOTOR25']
    if off in offer:
      bill-=bill/10
    else:
      print("invalid code")

    print('Order placed')
    print('\nItem :'+item +'\nQuantity :'+str(qty) + '\nBill:'+str(bill) +'\nYour order will reach you soon!')
    import smtplib, ssl

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "nandhaa403@gmail.com"  # Enter your address
    receiver_email = "nandhabalanmarimuthu15@gmail.com"  # Enter receiver address
    password = 'nandhaaku'
    message = '\nItem :'+item +'\nQuantity :'+str(qty) + '\nBill:'+str(bill) +'\nYour order will reach you soon!'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)
    od = (name,item,ty,qty,place,bill)
    qu = 'insert into orderDetails(customer_name,item,type,qty,place,bill) values(%s,%s,%s,%s,%s,%s)'
    mycursor.execute(qu,od)
    mydb.commit()
    mycursor.execute('select id from orderDetails order by id desc limit 1')
    oi = mycursor.fetchone()
    print('Your order id is: ',oi[0])
    print('Thanks For Choosing us')


