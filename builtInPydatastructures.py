#Lists and List operations
numbers=[1,8,3,15,2,3,4]

#using list() method which takes an iterable

evenNums= list(range(0,20,2))
print(evenNums)

#use the len() method to get the length
print(len(evenNums))
#use [] to get or modify items at a given index
evenNums[2]
#using two indexes to slice a list of letters,or pass a step [::2],reverse [::-1]
print(evenNums[0:5])

#unpacking lists
# first,second,third =numbers
first,second,*others=numbers

#looping over lists
for x in range(5):
    for y in range(3):
        print(f'{x},{y}')
#sorting lists
numbers.sort(reverse=True)
print(numbers)
#sorting by passing the lambda function as a key to the sort() method

items=[
    ("product1",23),
    ("product1",11),
    ("product1",1),
    ("product1",8),
]
#to sort the above items list we can use a sort() method in which we pass a sort function we have defined elsewhere as a key

# def sortItems(item):
#     return item[1]

# items.sort(key=sortItems)

# print(items)

#However the above implementation is a bit complex and a better way to implement the sorting is using a lambda function
items.sort(key=lambda item:item[1])
print(items)

#transforming a given list using the map() method that takes 2 parameters, a lambda function and an iterable

x=map(lambda item:item[1],items)
print(list(x))

#lets say you want to filter the items and return only those with a price above a certain value

# y=list(filter(lambda item:item[1]>10,items))
# print(y)

#filtering using a list comprehension
flitered=[item for item in items if item[1]>=10]
print(flitered)