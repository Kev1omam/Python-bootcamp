#For example,  
#my_name = "Frank"  this line creates a name variable type: string 
#print("My name is {}".format(my_name))

cars = 100 #this line creates a name variable type: integers
space_in_a_car = 4.0 #this line creates a name variable type: float
drivers = 30 #this line creates a name variable type: integer
passengers = 90#this line creates a name variable type: integer
cars_not_driven = cars - drivers #this line subtracts two variables of type interger
cars_driven = drivers # this line assigns the value of driver to the variable driven_cars
carpool_capacity = cars_driven * space_in_a_car# 

average_passengers_per_car = passengers / cars_driven#


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")

name = input('Please state your name: ')# recuperer une valeur dun input
age = input("How old are you? ")
print("You are {} years old".format(age))
 
a = 33 
b = 200
if a > b :
   print("a is greater than b")
elif a==b:
   print("a is equal b")
else :
   print ("a is less than b")


   nombre = int(input("entrer un nombre compris entre 1 et 100"))
   if nombre%3==0:
     print("Fizz")
   elif nombre%5==0:
     print("Buzz")
   else nombre%3==0 and nombre%5==0
   print("FizzBuzz")



   print("Hello world\n"*4)


  

   