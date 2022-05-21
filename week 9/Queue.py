from operator import index

from humain import Humain



class Queue:
  #Attribute

  #def __init__
  
  humans = []

  #method to add Person 
  def add_person(self, person):
    if person.age > 60 or person.priority:
      self.humans.insert(0,person)
    else:
      self.humans.append(person)
    


    
  #method to find_in_queue
  def find_in_queue(self, person):
    for i in range(len(self.humans)):
      if self.humans[i] is person:
        return i
    
    return None
    

  # method to swap 
  def swap(self, person1, person2):
    if person1 in self.humans and person2 in self.humans:

      index1 = self.humans.index(person1)
      index2 = self.humans.index(person2)
      self.humans[index1],self.humans[index2] = self.humans[index2],self.humans[index1]

  def get_next(self):
    return self.humans[i]

  def get_next_blood_type(self, blood_type):
    for human in self.humans:
      if human.blood_type == blood_type:
        return human 
         
    return None 

  def sort_by_age(self):
    sorted_humans = [human for human in self.humans if human.priority]
    sorted_humans += [human for human in self.humans if human.age > 60]
    sorted_humans += [human for human in self.humans if human.age <= 60]
  """ def sort_by_age(self):
    new_humans = []
    for human in self.humans:
      if human.priority:
        new_humans.append(human) """
        
    new_humans = [human for human in self.humans if human.priority]

#c'est quoi ce print 
hum1 = Humain('Ramses', 100, 'AB')
hum2 = Humain('Etienne', 10, 'A')
hum3 = Humain('Kevin', 5, '0', True)

q = Queue()

q.add_person(hum1)
q.add_person(hum2)
q.add_person(hum3)

q_name = [human.name for human in q.humans]
print(q_name)