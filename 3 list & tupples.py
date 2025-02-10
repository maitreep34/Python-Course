marks0 = 94.5
marks1 = 54.4
marks2 = 87.4
marks3 = 95.5
marks4 = 66.4
marks5 = 45.4

marks = [ 94.5, 54.4,87.4,95.5,66.4,45.4]
print(marks)
print(type(marks))
print(marks[1])
print(len(marks))
print(marks[2])

student = ["maitree", 94.5 , "karjan"]
print(student)
student[0] = "mansi"
print(student)

#list methods , list.append(4)  ,  sorting is ascending and desending 
# list.sort()  ,  list.reverse()


list = [2,1,3]
list.append(4)
print(list)
print(list.sort()) #for ascending order   1,2,3
# print(list.sort(reverse=True)) #for desending order 3,2,1
print(list)
 
list= [ 1,2,3,4]
list.reverse()
print(list)


list=[2,1,3]        # [2,5,3,1]
list.insert(1,5)
print(list)

list= [2,1,3,1]     #removes first occurence of elements[2,3,1]
list.remove(1)
print(list)


list=[2,1,3,1]    #python documentation for diff methods 
list.pop(2)       #removes element at idx 
print(list)



#tupples in python 
# a built in data type that lets us create immutable sequence of value.
# not changing values 

tup = (2,1,3,1,)
print(tup.count(2))
print(type(tup))

tup= (1,)
print(tup)
print(type(tup))

tup = (1,2,3,1,)
print(tup[1:3])


# tuple method  
# 1 tup.index(el) return index of 1st ele 
# 2 tup.count(el) counts total occurrence

tup = (1,2,3,4,2,2,1,)
print(tup.count(2))

#wap to ask user to enter names of their 3 fav movies nd store them in list
movies = []
mov1 = input("enter 1st movie :")
mov2 = input("enter 2nd movie :")
mov3 = input("enter 3rd movie :")

movies.append(mov1)
movies.append(mov2)      #movies.append(input("enter 1st movie:"))
movies.append(mov3)

print(movies)


#wap to check if list contains a palindrome of elements. (hint : use copy()method )
list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("palindrome")
else:
    print(not palindrome )



