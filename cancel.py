import mysql.connector
import random
mydb=mysql.connector.connect(host='localhost',user='root',password='nandhaaku',database='eShop')
mycursor=mydb.cursor()

def cancel():
  ic = int(input('Enter your order id: '))
  name = input('Username: ')
  mycursor.execute('select * from orderDetails where id=%s and customer_name =%s ',(ic,name))
  data = mycursor.fetchone()
  if data:
    otp=random.randrange(11111,99999)
    print('Generating OTP....')
    import smtplib, ssl

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "nandhaa403@gmail.com"  # Enter your address
    receiver_email = "nandhabalanmarimuthu15@gmail.com"  # Enter receiver address
    password = 'nandhaaku'
    message = '\nYour otp is '+str(otp)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)
    o=int(input('Enter the OTP: '))
    if o == otp:

      item = data[2]
      ty = data[3] 
      qty = data[4]
      if (ty=='e'):
        mycursor.execute('update e set stock = stock+%s where name = %s',(qty,item))
        mydb.commit()
      elif(ty=='l'):
        mycursor.execute('update l set stock = stock+%s where name = %s',(qty,item))
        mydb.commit()
      elif(ty=='p'):
        mycursor.execute('update p set stock = stock+%s where name = %s',(qty,item))
        mydb.commit()
      mycursor.execute('delete from  orderDetails where id = %s and customer_name = %s',(ic,name))
      mydb.commit()
      print('your Order is Cancelled')
      
    else:
      print('Invalid OTP')
  else:
    print('Invalid username/orderid')



