lst = [1, 2, 3, 4, "a", "b", "c", 38.5, "56.7"]
print(lst)
print(type(lst))
print(type(lst[-1])) 


#Example Of A Simple Function That Says Hello

def say_hello():
    """A function that says hello"""
    print("Hello!") 

say_hello()


#Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call
def calculation( a , b):
  add = a + b 
  sous = a - b
  return add , sous
  calculation(12, 6)

  

