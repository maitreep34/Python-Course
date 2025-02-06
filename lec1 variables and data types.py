
print("Hellow Maitree")
print("Maitree is my name. ", " My age is 20.")

#assign operator 

name = "Maitree"
age = 20 
price = 27.33

age2 = age 
print (age2)

print(type(name))      # python automatically find datatype of variables.
print(type(age))       # integers(+,-,0) , string("name") , float(3.99,2.5,9.0) , boolean(True,False) , none
print(type(price))

age = 20
old= False
a = None
print(type(old))
print(type(a))

#arithmetic operators (+,-,*,/,%)
a=5
b=2

sum = a + b
print(sum)     # or print(a+b)
print(a*b)
print ( a-b)
print( a / b)
print ( a % b ) #remainder 
print( a ** b ) #a^b

#relational operator (==,!=,>=)
a = 50 
b = 20 

print( a == b ) #False 
print( a != b ) #true 
print( a >= b ) #true 
print( a > b ) #true 

#assignment operator (=,+=,*=,/=)
num = 10 
num = num + 10   #10+10 
num += 10 
print("num :", num) 

num = 10 
num **= 5
print("num :", num )  #1,00,000

# logical operators (not,and,or)
a= 30
b= 20
print(not False)  #ture
print(not (a>b))  #false

val1 = True
val2  = False
print(" and operator:", val1 and val2 )
print(" or operator:", val1 and val2 )

#type conversion it's one type of variable convert automatically into other vaiable.
# type casting   it's covert manually 
a,b = 1,2.0
sum = a + b
print(sum)

#type casting 
a,b = 1,"2"
c = int(b)   
print( type(a))

#input in py 
#name = input("enter your name: ")
age = input("enter age: ")
marks = input("enter marks: ")
print("welcome", name)#

#prac que 
#input 2 num nd print thier sum 
input("enter first : ")
input ("enter second: ")

print("sum = ", first + second )


#wap to input  side of square nd print its area 
side = float(input("enter square side : "))
print ("area =", side **2)




