#Basics of python To Get you started
#Variables ...note the naming convention
import math
name = "barbie"
my_name = name.title()
print(my_name)

#built in print() method

#functions...blocks of code that perform a specific task...in python scope of a function is defined using identation
def myfunction(name):
    print('Hello  ' + name)


myfunction("Leila")

def decrement(k):
    if (k >0):
        result = k + decrement(k - 1)
        print(result)
    else:
        result =0
    return result
decrement(6)

#formatted strings for concatenation
fname= "Jane"
sname="Vianuella"
message= f'{fname} {sname} is beautiful'
print(message)

#Iterables...iterating over different data structures eg strings,list,tuples,in python using a for loop
for item in fname:
    print(item)
# for loop is used to iterate a collection eg a string or an array
#while loop is used to execute a given code a number of times
num = 1
while num<=5:
    print(num)
    num +=1

#method two of filtering alist...using filter() method
my_items=[
    ("product1",7),
    ("product2",10),
    ("product3",13)
]
def filtering():
    result = filter(lambda my_items:my_items[1]==10 or my_items[1]>10,my_items)
    for item in result:
        print(item)


filtering()

#method three of filtering using list comprehension

# def second_filtering():
#     prices = [my_items[1] >= 10 for item in my_items]
#     print(prices)
#
# second_filtering()


#to swap variables we have to define a third variable
x=10
y=11
z=x

x=y
y=z

print(x)
# print(y)
# class Animal:
#     def feed(self,food):
#         message=f"feeding on {food}"
#         return message
#
#
# cow = Animal()
# print(cow.feed("grass"))


class Animal:
    def __init__(self, name, food):
        self.name = name
        self.food = food

    def feed(self):
        print(f"This is me {self.name} and I eat {self.food}")


cow = Animal("Cow","Grass")
print(cow.name)
cow.feed()

lion = Animal("lion", "meat")
lion.feed()




# Write
# a
# Python
# program
# to
# create
# aclass representing a Circle.Include methods to calculate its area and perimeter.
class Circle:

    def __init__(self,diameter):
        self.diameter= diameter


    def calculate_area(self):
        area=(math.pi*self.diameter*self.diameter)/4
        print(area)

    def calculate_perimeter(self):
        perimeter=(math.pi * self.diameter)
        print(perimeter)

first_circle=Circle(20)
first_circle.calculate_perimeter()

first_circle.calculate_area()


# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        current_year = input("what is the current year ")
        age = (int(current_year)-self.date_of_birth)
        print(f"my name is {self.name}, Iam from {self.country} and Iam {age} years old")

    def __str__(self):
        return f"{self.name} {self.country}"


Caren = Person("Caren", "Kenya", 2007)
Caren.calculate_age()
print(str(Caren))

#magic methods
#equality magic methods

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(10,20)

other =Point(1,2)

print(point == other)
print(point > other)

#making custom containers--for example here we are implementing a dictionary inside
#the class so that we can encapsulate the complexity around the case sensitivity
#of dictionary tags
#the class below also implements the getitem magic tag and the get method to prevent errors incase item is missing
#and the setitem magic method for setting a value of a given key
class TagCloud:
    def __init__(self):
        #set tags to an empty dictionary
        self.tags={}

    def add(self,tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(),0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(),0)

    def __setitem__(self, tag, value):
        self.tags[tag.lower()]=value

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()

cloud.add("Python")
cloud.add("python")
cloud.add("python")



print(cloud["PYTHON"])
print(cloud.tags)
# for tag in cloud.tags:
#     print(cloud[tag])

