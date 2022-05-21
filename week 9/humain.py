
class Humain:
  next_id = 1
  
  def __init__(self, name, age, blood_type,priority = False):
    self.id_number = Humain.next_id
    self.name = str(name)
    self.age = int(age)
    self.priority = priority
    self.blood_type = blood_type
    self.family = []
    Humain.next_id += 1

""" hum = Humain('ramses', 100, 'AB')
print(hum.id_number)
print(Humain.next_id) """

def test(number):
  if(number%2 == 0):
    return True

  print("OHHH ",number, 'est impair')
  return False

a = [i for i in range(101)]
print(a)