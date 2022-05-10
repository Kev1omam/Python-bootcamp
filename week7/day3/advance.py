from email import message_from_binary_file


def check_arguments(*args):
    print(f"These are the arguments {args}")
check_arguments(1, 2, 'hey')




def double(*args):
  return map(lambda n : n*2, list,args)
  print(list(double(1,2,3,4,5,6,7,8,9,)))  


 
 
 
 
 
 
def check_keywordedarguments(**kwargs):
    return kwargs

print(check_keywordedarguments(fruit='apple', ordered= 2))



def check(a, b, c):
    print(a, b, c)

a = [1,2,3,4]
check(**a)

#Given a list of numbers, write a function that returns the sum of every number. BUT you can have a malicious string inside the list.


my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

def liste(liste):
  somme = 0
 
for item in liste:
   try:
  somme += item
  except:
  continue
    print(somme)

    

    

 