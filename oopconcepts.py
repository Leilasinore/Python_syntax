def greeting(name):
    print(f'hello {name}')


greeting("leila")
greeting("Sam")

class HumanBeing:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the print name method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
    #the __init__() magic method,,
    def __init__(self,course,registration_number,year):
        self.course=course
        self.registration_number=registration_number
        self.year=year
        Person. __init__(self,fname,lname)

    def __str__(self):
        return f"hello ,I am a {self.course} student in {self.year} year"
        


Leila= Student("mechanical","mpe/41/19",5)
print([Leila.course,Leila.registration_number,Leila.year])
print(str(Leila))
