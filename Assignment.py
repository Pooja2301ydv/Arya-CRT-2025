#Question 1
#How do lists and tuples differ in terms of mutability and 
#performance? When would you choose one over the other?

# Lists are mutable data types meaning the can be changed while tuples are immutable
# meaning they cannot be changed.
# One should choose lists when you need a collection of items that may change during the
# program's execution. They are ideal for scenarios where you need to dynamically add, remove, 
# or modify elements.
# On the other hand tuples should be used when you need a collection of items that should remain 
# constant throughoutthe program's execution. They are useful for fixed data sets, such as
# coordinates, constants, or as keys in dictionaries.

#Question 2
#Explain how Python handles type conversion between different data 
#types, such as between integers and floats or between strings and 
#lists. 
#Python has several built-in functions for type conversion (also known as type casting)
#between different data types.
#(i). Integer to float
n=34
f=float(n)
print(f)

#(ii). Float to integer
f=34.45
n=int(f)
print(n)

#(iii). String to list
string="Pooja Yadav"
lst=list(string)
print(lst)

#(iv). List to tuple
lst=[1,2,3,4,5]
tup=tuple(lst)
print(tup)

#(v). Tuple to list
tup=(1,2,3,4,5)
lst=list(tup)
print(lst)


#Question 3
#Take a number and use the += operator to increase its value by 10. 

n=int(input("Enter the number: "))
n=n+10
print(n)

#Question 4
# Write a Python program to check if a given year is a leap year or not.
year=int(input("Enter the year: "))
if(year%4==0 and(year%100!=0 or year%400==0)):
    print("Is a LEAP YEAR")
else:
    print("Not a LEAP YEAR")  

#Question 5
#Write a program that asks the user to enter their marks and displays 
#their grade: 
# • 80-89: B 
# • 70-79: C 
# • 60-69: D 
# • Below 60: F 
marks=int(input("enter the student marks: "))
if(marks>=90):
    print("Grade A")
elif(marks>=80 and marks<90):
    print("Grade B")
elif(marks>=70 and marks<80):
    print("Grade C")
elif(marks>=60 and marks<70):
    print("Grade D")        
else:
    print("Grade F")

  
