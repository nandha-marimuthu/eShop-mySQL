#electronics shop with mysql
while True:
  i = int(input("1 For Order\n2 For Cancel\n3 For Admin\n4 For Exit\nEnter: "))
  if i==1:
    from login import login
    login()
  elif i==2:
    from cancel import cancel
    cancel()
  elif i==3:
    from login import admin
    admin()
  elif i==4:
    break
  else:
    print('Invalid code')