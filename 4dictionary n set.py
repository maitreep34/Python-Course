# dictionaries are used to store data values in key value pairs
# its unordered ,mutable and dont allow duplicate keys (values)

info = {
    "key": "value",
    "name": "maitree patel",
    "learning": "coding",
    "age": 35,            # in dictionary we adding string and values 
    "is_adult" : True,
    "marks": 94.3
}

print(info)


info = {
    "key": "value",      
    "name": "maitree patel",
    "subject": ["python","java","c"],   #add our list in sub
    "topics" : ("dict","set"),     #add like tupple form
    "age": 35,              # in dictionary we adding string and values 
    "is_adult" : True,
    "marks": 94.3    #our key can be any values it not mutables like tupple
    
}
print(type(info))
print(info["name"])
print(info["subject"])
print(info["topics"])
print(info["age"])
info["name"] = "dhruv" 
info["surname"] = "vaghela"  #we can add assigned operators
print(info)

#add null dict

null_dict = {}
null_dict["name"] = "maitree patel"
print(null_dict)

#nested dictionary
student = {
    "name": "rahul",
    "subject": {
        "phy": 56,
        "chem": 58,
        "math": 69,
    }
}
print(student["subject"]["chem"])
#add list and len
print(len(student.keys()))   #return all keys by .keys
print(list(student.keys()))

print(student.values())   #return all values
print(student.items())   # return all val and keys
print(student["name"])
print(student.get("name"))    #error not exits in list like name2 
print("hellow")
print("welcome buddy")
print("coding")

new_dict = {"city" : "delhi"}
student.update(new_dict)

# set in python
#set is collection of the unordered items 
#each ele is must be unique & immutable 


collection = {1,2,2,2,"hello","world","world"}

print(collection)
print(type(collection))  
print(len(collection))

collection = set()   #empty dic ; syntax 
print(type(collection))

#set method    
    
#set.add( el )     adds an ele 
#set.remove(el)    removes the ele 
#set.clear()       empties the set 
#set.pop()         removes a random value


collection = {"hello","apnacollege","college","coding","python"}

print(collection.pop())
print(collection.pop())

#set methods 
#set.union(set2)           combines both set value & return new 
#set.imtersection(set2)    combines common values & return new

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1)
print(set2)

#enter 3 sub from user and store them in dic. start empty dic nd add one by one 
#use sub name as key and marks as value 

marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter math: "))
marks.update({"math" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

print(marks)

#figure out way to store 9 & 9.0 as seprate values in set 

values = { 9,"9.0"}
print(values)


values = {
    ("float", 9.0),
    ("int", 9 )
}

print(values)



