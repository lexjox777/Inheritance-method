class Animal:
 def __init__(self,name,age):
   self.name = name
   self.age = age

 def speak(self):
   return f"my name is {self.name}"

class Dog(Animal):
 def __init__(self,name,age):
  #  self.name = name
  #  self.age = age
   super().__init__(name,age)

 def speak(self):
   return "Whoof Whoof"


class Cat(Animal):
 def __init__(self,name,age):
  #  self.name = name
  #  self.age = age
   super().__init__(name,age)
