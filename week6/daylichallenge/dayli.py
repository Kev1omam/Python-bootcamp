a = input("entrer une phrase: ")
if len(a) < 10 : 
  print("string not long enough")
else:
  print("string too long")  
  print(a[0])
  print(a[len(a)-1])



  for i in list(range(0,len(a))):
    print(a[0:i+1])


