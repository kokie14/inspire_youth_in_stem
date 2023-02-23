#mutable vs immutable

#mutable -data types that can be edited /chnged during life cycle
#add/remove elements
#immutable - data types that can not be edited during life cycle

#1 List-(mutable)
friends=["mark","samantha","precious"]
# or friends=[]for empty lists
#add elements - append()
#pop-
#delete

students=["dove","skolof","sophia"]

friends.extend(students)#joins both the lists of names
friends.append("aurius")#adds the name at  the end of the list
#2 Tuples -(immutable)
#type of lists that are immutable 
#used to store multiple items in a single variable
stationaries=("pens","ink","sharpener","stapler","pencils")
#replace the whole  tuple
stationaries=("ruler","clipboard","files")

for stationary in stationaries:
    print(stationary)
numbers=(1,2,3,4,5,6,7,8,9)

#3 Dictionaries aka dict
#uses a key and a value pair

student={"name":"kokie" ,"age": 21,"gender":"female"}

print(student["name"])
print(student["age"])
print(student["gender"])
print(student.values())
print(student.keys())

friends= {"fav_colour":"red","hobby":"swimming","course":"mechatronics engineering","weight":65 ,"height":125}

print(friends["fav_colour"])
print(friends["course"])
print(friends["height"])
print(friends["hobby"])
print(friends["weight"])
print(friends.keys())
print(friends.values())

#4 Sets