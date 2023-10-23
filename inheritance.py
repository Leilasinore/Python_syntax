from abc import ABC, abstractmethod

class Animal:
    def __init__(self):
        self.age=1

    def eat(self):
        print("eat")

class Mammal(Animal):
    def __init__(self,name):
        super().__init__()
        self.name=name
        
         

    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

person=Mammal("leila")
print(person.eat())
print(person.age)
print(person.name)

# for method overiding issues use the super() to get access to the constructor of the parent as illustrated above
class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened=False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        else:
            self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("stream is already closed")
        else:
            self.opened = False

    @abstractmethod
    def read(self):
        pass

class FilesStream(Stream):
    def read(self):
        print("Reading data from file stream")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from network stream")

#stream=Stream(),,,this will result in an error because we cannot create an instance of an abstract class
#to avoid that implement

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

def draw(controls):
    for control in controls:
        control.draw()
     

ddlObject= DropDownList()
textboxObject=TextBox()
draw([ddlObject,textboxObject])

#the above is an example of polymorphism ,our draw method is taking different forms and this is determined at runtime
#however to achieve polymorphic behavour in python we do not always have to have a base class because python is dynamically typed
# but having the abstract base class is good practice because it enforces a common interface across its derivatives 

class Text(str):
    def duplicate(self):
        return self + self
    
myText=Text("java")
print(myText.duplicate())