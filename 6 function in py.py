a =5
b=10
sum = a +b
print(sum)        #15


#more lines of code 

a=2
b=10

sum = a+b        #12
print(sum)

#calc_sum(2,10)    
           #use for less redundancy
#calc_sum(13,56)


#fuction in python 
#  block of statements that perform  a specific task
#  Functions are reusable blocks of code.
#  Functions can take arguments and return values.
#  Functions can be defined inside other functions.
#  Functions can be defined inside classes.
#  Parameters are optional in function.
#  Return statments can be optional in function.


def calc_sum(a,b):
    return a + b

sum = calc_sum(178,2)         #180
print(sum)


def print_hello():
    print("hello")

#average of 3 numbers 


def calc_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg
calc_avg( 98, 97, 95)


print("abc", end="$" ) 
print("abc")   #sep = ""
print("maitree patel") # end ="\n"

#...................Types of functions..........

#--->1. Built-in functions : These are functions that are already defined in python.
#--->2. User-defined functions : These are functions that are defined by the user.

#..............Default Parameters.............
#---> Assigning a default value to parameters , which is used when no arguement is passed.



#default paeameters
def cal_prod(a=1,b=2):
    print(a*b)
    return a + b
           
cal_prod(1)          #o/p 2


#q.1 print the length of list 

cities = ["delhi","gurgaon","noida","pune","mumbai","chennai"]
heroes = ["thor","ironman","captain","america","shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)    


#print elements og list in single line 

cities = ["delhi","gurgaon","noida","pune","mumbai","chennai"]
heroes = ["thor","ironman","captain","america","shaktiman"]

def print_len(list):
    print(len(list))

def print_len(list):
    for item in list:
        print(item,end="")  # end=""is used to print elements in a single line


print_len(heroes)
print()


#print(heroes[0],end="")
#print(heroes[1],end="")
#o/p:  thorironmancaptainamericashaktiman

#find the factorial of n 


n = 5

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(5)    


#convert usd to INR

def converter(usd_val):
    inr_val = usd_val * 86
    print(usd_val ,"USD = ", inr_val," INR" )

converter(100) 

#o/p 100 USD =  8600  INR