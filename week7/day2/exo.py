# #EXO 1.1
# def display_message():
#   print(" i learn pyhon ")
# #1.2
# display_message()
 
#   #exo 2
  
# def favorite_book(title):
#   print("One of my favorite books is Alice in Wonderland")
# favorite_book(title="One of my favorite books is Alice in Wonderlan")

# # #exo 3
#  def describe_city(name , country ="cameroun"):
#   print( name ,"is in", country)
#  describe_city("douala", "country")

# # #Exo 4

from cgitb import small
from locale import textdomain
import random
def random_number(number):
  num = int(random.random()*100)
  if number==num:
    print("success")
  else:
    print("echec")  

random_number(2)

#exo 5 

def make_shirt(size ="small", text):
  print("je me nomme" ,text , "je fais du ", size) 

  make_shirt(44 , "omam kevin")











