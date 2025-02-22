#loops in py
count = 1
while count <= 5 :
    print("hello")
    count += 1


i = 1
while i <= 5 :
  print("naruto")
  i+=1


#print num 1 to 5
i = 1 
while i <= 5:
   print(i)
   i += 1

print("loop ended ")

#reverse number 

i = 10
while i>= 1:   #stopping cond
   print(i)
   i -= 1


#multiplication table of num n 
n = int(input("enter number :"))
i = 1
while i <= 10:
   print(n*i)
   i += 1

#element of following list using loop 
#[1,4,9,16,25,36,49,64,81,100]

#print(nums[0])  .....print(nums[len(nums)])

nums = [1,4,9,16,25,36,49,64,81,100]
heroes = ["ironman", "thor", "batman"]

i = 0                         #travers
while i < len(heroes):
   print(heroes[i])
   i += 1 


#search for a number x in this tuple using loop
#[1,4,9,16,25,36,49,64,81,100]

nums = (1,4,9,16,25,36,49,64,81,100)

x = 36 

i = 0   
while i < len(nums):
   if(nums[i] == x):
     print("found at idx", i )
   i += 1

#breack and continue 

i = 1 
while i <= 5:
   print(i)
   if (i==3):
      break
   i += 1

print( "end of loop" )


#contine 

i = 0 
while i <= 5:
   if(i == 4):
     i += 1
     continue           #skip num
   print(i)
   i += 1

#for loop in python  
#for list
nums = [ 18,2,3,4,5]

for val in nums:
   print(val)

tup = (1,2,3,4,2,8,9)

#for tuple

for num in tup :
   print(num)

str = "maitree patel"

#for string
for char in str:
   if(char == 'p'):
      print("p found")
      break
   print(char)
else:
   print("END")

#element of following list using loop
#[1,4,9,25,36,55,81,100]

nums = [1,4,9,25,36,55,81,100,25]
x = 25
idx = 0
for el in nums:
   if(el == x):
      print("number found at idx", idx)
      break
   idx += 1

# range()  returns seq of num , star by 0 by default and increments by 1
seq = range(15)

for i in seq:         #for i in range(15)
  print(i)

# range( start?, stop,step?)
for i in range(100,55):     #range(stop)
   print(i)


for i in range(2,101,3):     #range(start,stop)
   print(i)

#pass statement   ,null

for i in range(5):
   pass

if i > 5:
   pass

print("some usefull work")
