# python variables and collections
print("I am a print statement")

# use input to get data from console
#someData = input("Enter some data: ")
#print(someData)

# lists are used to store data
a = []
a.append(1)
a.append("a")
a.pop()
b = [2]
print a
print a + b

c = (1,"a",True)
print(type(c))
print(len(c))

# tuples assigned to variables
guitar3,guitar4,guitar5 = ("fender","gibson","ibanez")
print(guitar3,guitar4,guitar5)

# dictionary creation 
dict1 = {"one": 1, "two": 2, "three": 3}
print(dict1["one"])

print(dict1.keys())
print(dict1.values())
