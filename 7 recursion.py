# RECURSION
#when function calls itself repeatedly
n=6
def show(n):
    if(n == 0):       #base case
        return
    print(n)
    show(n-1)
    print("END")
show(5)    #5,4,3,2,1,end


# return n!
def fact(n):
    if(n == 1 or n ==0):
        return 1
    
    return n * fact(n-1)
print(fact(4))                 #24


#let's practice

#q-1 recursive function to calculate the sum of first n natural numbers 

def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(10)
print(sum)               #55
           


#recursive function to print all elements in list 

def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx + 1)

fruits = ["mango","banana","apple","kiwi"]

print_list(fruits)

#o/p: mango,banana,apple,kiwi
