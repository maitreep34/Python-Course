str1="this is a string."
str2='maitree'
str3="""this is string"""


str1="this is string.\n we are creating it" #escape seq character \n \t for combining and next line tab


#for lenght of string


len1=len(str1)
len2=len(str2)
len3=len(str3)
print(str1)
final_str =str1+str2+str3
print(len(final_str))


str="maitree patel"   #it cant add blank spaces
ch = str[2]
print(str[3])

str = "maitree patel" #accesing part of string
print(str[1:4])        #strt index : ending index
print(str[3:len(str)])


#slicing negative index


str = 'apple'
print(str[-3:-1])          #pl


#string function
str= "i am studing python with apnacollege"       #check endingstring
print(str.endswith("ege"))                        #true

str = str.capitalize()
print(str)

print(str.replace("python","javascript"))         #replacing words

print(str.find("i"))

print(str.count("with"))

name = input("enter your name:")               #lenght for str
print("lenght of your name is",len(name))

str = " hi, $iam the $ symbol $788.4"
print(str.count("$"))


#conditional statements


age = 21

if(age >= 18):
    print("can vote & apply for license")
    print("can drive and can vote")


light = "GREEN"
if(light == "red"):
    print("stop")
elif(light=="GREEN"):
    print("go")
elif(light == "yellow"):
    print("look")

#print("enf of code")

age=14

if(age>=18):
    print("can vote")
else:
    print("can not vote")

#grade conditions

marks = 74

if (marks>=90):
    grade = "a"
elif(marks>= 80 and marks < 90):
    grade = "b"
elif(marks>= 70 and marks< 80):
    grade="c"
else:
    grade="d"

print("grade of students ->",grade)



