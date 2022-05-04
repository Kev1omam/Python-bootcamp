list1 = [5, 10, 15, 20, 25, 50, 20]

list1.index(20) # position de lindexe
list1.insert(3,200)# insert un element a lindice 3
list1.pop(3)#supprimer une valeur a lindice indiquee
list1[3]=200# modifier un element par son index





aTuple = (10, 20, 30, 40)
a,b,c,d =aTuple
print(a) # should print 10
print(b) # should print 20
print(c) # should print 30
print(d) # should print 40


numbers = range(4, 19)

for number in numbers:
  print(number)