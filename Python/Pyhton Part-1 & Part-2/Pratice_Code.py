var1 = "Hello Everone"
var2 = 20
var3 = 22.07

var4 = "25"
var5 = "36"

print ( str ( var2 + var2 ) )
print ( "*" * 40 )
print ( type ( var1 ) )
print ( "*" * 40 )
print ( type ( var3 ) )
print ( "*" * 40 )
print ( type ( var2 ) )
print ( "*" * 40 )

# Type Casting
# Strings to Integer
print ( int ( var4 ) + int ( var5 ) )

# Enter Your Name
print ( "Enter Your Name" )

# name=input()
# print("Your Name is " + name)
print ( "*" * 40 )

# STRING MANIPULATION
mystr = "Hello Everyone good Morning"
print ( mystr[5] )
print ( "*" * 40 )

# String length
print ( len ( mystr ) )
print ( "*" * 40 )

# String Slicing
print ( mystr[0:5] )
print ( "*" * 40 )

# Skipking of character in string slicing
print ( mystr[0:19:2] )
print ( "*" * 40 )

#String Muting
phrase = "many moons"
phrase_expanded = phrase + " and many stars"
phrase_larger = phrase_expanded + " litter"
phrase_complete = "M" + phrase_larger[1:] + " the night sky."
excited_phrase_complete = phrase_complete[:-1] + "!"


print(excited_phrase_complete)



# negative indexing
print ( mystr[-4:] )
print ( "*" * 40 )

print ( mystr.count ( "o" ) )
print ( "*" * 40 )

print ( mystr.find ( "is" ) )
print ( "*" * 40 )

print ( mystr.lower () )
print ( "*" * 40 )

print ( mystr.upper () )
print ( "*" * 40 )

print ( mystr.replace ( "Morning", "night" ) )
print ( "*" * 40 )
print ( "*" * 40 )
print ( "*" * 40 )

# LIST

grocery = ["milk", "pasta", "egg"]
print ( grocery )
print ( grocery[2] )

# sorting of list
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number.sort ()
print ( number )
print ( "*" * 40 )

# reversing Of List
number.reverse ()
print ( number )
print ( "*" * 40 )

# slicing Of list
print ( number[:51] )
print ( number[1:5] )
print ( "*" * 100 )

# appending of list
# add add the end of list
number.append ( 11 )
print ( number )
print ( "*" * 100 )

# inserting in to the list
# insert function insert the element at any place in the list
number.insert ( 2, 15 )
print ( "*" * 100 )

# remove function
number.pop ()
print ( number )
print ( "*" * 100 )

number[2] = 82
print ( number )
print ( "*" * 100 )
print ()


mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)
print()
print()


# Printing Of List
Shopping_list = ["milk", "Eggs", "Pasta"]
for iteam in Shopping_list:
    print ( "Buy" + iteam )
print ()

# Using Continue In List
for iteam in Shopping_list:
    if iteam == "eggs":
        continue
    print ( "Buy" + iteam )
print ()

# Using Of break in list
for iteam in Shopping_list:
    if iteam == "Egss":
        break
    print ( "Buy" + iteam )
print ()

print ( "*" * 100 )

# DICTIONARY

fruit = {"orange": "A sweet",
         "apple": "Good for cidar",
         "grape": "A samll",
         "lemon": "a sour",
         "lime": "Green citrus"}

print ( fruit )
print ()

# printing element using key
print ( fruit["lemon"] )
print ()

# to add to dictionary
fruit["pear"] = "An odd shaped apple"
print ( fruit )
print ()

fruit.update ( {"banana": "Great for health"} )
print ( fruit )

# to change entry
fruit["pear"] = "Great Fruit"
fruit["lime"] = "Great with tequila"

print ( fruit )
print ()

# to delete the entry
del fruit["lemon"]
print ( "fruit" )
print ()

# to iterate through the list
for snack in fruit:
    print ( snack )
print ()

# to get the orderded list or sort the list
ordered_keys = list ( fruit.keys () )
print ( ordered_keys )
ordered_keys.sort ()

for f in ordered_keys:
    print ( f + " " + fruit[f] )

print ( fruit.keys () )
print ( fruit.values () )
print ()

# to convert the list to tuple
# f_tuple=tuple(fruit.items)


# for snack1 in f_tuple:
# item,description=snack1


# print(item+" is" +description)

bike = {"make": "Honda",
        "model": "250 Dream",
        "color": "Red",
        "engine": 250}

print ( bike )

# To clear the list
bike.clear ()

color = {"c1": "Red",
         "c2": "black",
         "c3": "orange",
         "c4": "white"}
print ( color )
print ()
print ( "Enter the key for displaying color" )
key1 = input ( "Enter" )

if key1 in color:
    description1 = color.get ( key1 )
    print ( description1 )
else:
    print ( "Sorry Please Valid color key" )

print ()
print ()
print ( "*" * 100 )
print ( "*" * 100 )

# SET
farm_animals = {"sheep", "cow", "goat", "horse"}
print ( farm_animals )

for animal in farm_animals:
    print ( animal )
print ()

# to add to the set
farm_animals.add ( "hen" )
print ()

# to convert range to the tuple
even = set ( range ( 0, 40, 2 ) )
print ( even )
print ()

# To convert tuple to set
Square_tuple = (4, 9, 16, 25)
Square_set = set ( Square_tuple )
print ( Square_set )
print ()

# Set Functions
print ( even.union ( Square_set ) )
print ()
print ( even.intersection ( Square_set ) )
print ()
print ( even & Square_set )
print ()
print ( sorted ( even ) )
print ()
print ( even - Square_set )
print ()

# To remove element
even.discard ( 4 )
Square_set.remove ( 16 )

print ( even )
print ( Square_set )
print ()

print ()
print ()
print ( "*" * 100 )

# WHILE

i = 0

while i < 10:
    print ( "Good Morning" )
    i += 1

print ()
print ( "* " * 100 )

# BREAK AND CONTINUE
while True:

    in1 = int ( input ( "Enter the number" ) )

    if in1 > 100:
        print ( "You have enter valid number" )
        break
    else:
        print ( "Try Again" )
        continue
print ()
print ( "* " * 100 )

# IN AND NOT IN 

print('p' in 'apple')
print('i' in 'apple')
print('ap' in 'apple')
print('pa' in 'apple')
print('a' in 'a')
print('apple' in 'apple')
print('' in 'a')
print('' in 'apple')
print('x' not in 'apple')
print("a" in ["a", "b", "c", "d"])
print(9 in [3, 2, 9, 10, 9.0])
print('wow' not in ['gee wiz', 'gosh golly', 'wow', 'amazing'])
print("a" in ["apple", "absolutely", "application", "nope"])

# FUNCTION

def python_fun():
    print ( "Using Function" )


# calling Function
python_fun ()
print ( python_fun () )


def python_fun1(text):
    print ( "Hello " + text )


def python_fun2(int1, int2):
    summ = int1 + int2
    return summ


python_fun1 ( "Good Morning" )

var1 = int ( input ( "Enter int1= " ) )
var2 = int ( input ( "Enter int2= " ) )
var3 = python_fun2 ( var1, var2 )
print ( "Sum of interger", var3 )
print ()


# Function with multiple arguments

def multi_args_function(*args):
    for arg in args:
        print ( arg )


multi_args_function ( "hello", "everyone", "happy", 2, 3 )
print ()
print ()
print ( "* " * 100 )

# TRY AND EXCEPT

int5 = input ( "Enter Number" )
int6 = input ( "Enter Number" )

try:
    print ( "Sum Of Number", int ( int5 ) + int ( int6 ) )

except Exception as e:
    print ( e )

print ( "Line to be printed at the end " )
print ()
print ()
print ( "* " * 100 )

# FILE I/O
"""
"r"- open file read mode default mode
"w"-open file in write mode
"x"-Create file if not exists
"a"-Add more content to a file
"t"-text mode
"b"-binary file
"+"-read and write mode

"""

f = open ( "sample.txt" )
content = f.read ()
print ( content )

f.close ()
print ()
print ()

f1 = open ( "sample.txt", "rt" )

# tell() function print the current location of pointer
# seek() function used to reset the pointer the location mentioned

print ( "Location Of pointer given by tell() function" )
print ( f1.tell () )
print ( f1.readline () )
print ( f1.tell () )
print ( f1.readline () )
print ( f1.tell () )
print ()
f1.seek ( 0 )
print ( f1.readlines () )
print ()
print ()
print ( "*" * 100 )

imelda = "more mayhem", "imelda may", 2000, ((1, "Pulling the rug"), (2, "psycho"), (3, "mayhem"))
# print(imelda)

with open ( "imelda.txt", "w" ) as imelda_f:
    print ( imelda, file=imelda_f )

with open ( "imelda.txt", "rt" ) as imelda_f1:
    content1 = imelda_f1.read ()

imelda1 = eval ( content1 )
print ( imelda1 )
title, artist, year, tracks = imelda1
print ( title )
print ( year )
print ( artist )

for track in tracks:
    print ( track )

print ()
print ()
print ( "*" * 100 )

# LOCAL AND GOBAL VARIABLES

# Global Variable
l = 10


def fun_3(n):
    print ( "Printing the local varible" )
    l = 5  # local variable
    m = 8
    print ( m, n )
    print ( l )

    # printing the global varible
    # global l
    l += 5
    print ( "gobal variable", l )


fun_3 ( 10 )

x = 89


def fun_4():
    x = 40
    print ( x )

    def fun_inner():
        global x
        x = 88

    fun_inner ()
    print ( "after calling function", x )


fun_4 ()
print ( x )

print ()
print ()
print ( "*" * 100 )


# RECURSIVE FUNCTION
def fact_recurvsive(n):
    if n == 1:
        return 1
    else:
        return n * fact_recurvsive(n - 1)


f_1 = fact_recurvsive(5)
print(f_1)
print()
print()
print("*"*100)


# MODULE AND IMPORT

import turtle

turtle.forward(100)
turtle.back(100)
turtle.forward(100)
turtle.circle(100)

turtle.done()
print()
print()
print("*"*100)


# Launch The Deafult browser of Computer using module
   
import webbrowser
webbrowser.open("https://explaningtechnology.blogspot.com/")

# F-STRING
age=25
print(age)

age_in_words="25 Years"
print("name" + f"is {age} year old")
print("name" +f"is {age_in_words} year old")

pi=22/7
print(f"pi is appr. {pi}")
print()
print()
print("*"*100)


# PASSING THE MULTIPLE ARGUMENTS USING ARGS AND KWARGS

def function_args(*args):
  print(args[2])


var_13 = ["Ahemdabad", "Surat", "Bhuj", "Visnagar"]
function_args(*var_13)


def function_args1(a1,*args,**kwargs):
  print(normal)

  for item_1 in args:
    print(item_1)

  for key,value in kwargs:
    print(f"{key} is {value}")
  

normal = "Good Morning"
var_14 = ["Ahemdabad", "Surat", "Bhuj", "Visnagar"]
kw={"k1":"HII","k2":"hello","k3":"HHHHHHHHHHHHHH"}
function_args1(normal,*var_14,**kw)   
print()
print()
print("*"*100)



# ENUMERATE FUNCTION
list_1 = ["lemon", "Tomato", "eggs"]

for item,index in enumerate(list_1):
  print(f"{item} to buy {index}")

print()
print()
print("*"*100)

import sys
print(sys.path)

import Demo_2

print(Demo_2.function_math(10,20))
print(Demo_2.function_1())
print(Demo_2.a)
print("*"*100)

# USUNG MAIN IN THE CODE WHEN IMOPRTING THE DATA OF ANOTHER MODULE SO THAT UNREQUIRED DATA IS NOT PRINTED 

import Demo_3
print(Demo_3.a)
print("*"*100)


# .JOIN() METHOD TO CONCATE TO STRING

my_list1 = ["a","b","c","d"]
new_string = " "

for item in my_list1:
  new_string = " , ".join(my_list1)

print(new_string)

my_list2 = ["Ahemdabad", "Surat", "Visnagar", "Bhuj"]

a = " , ".join(my_list2)
print(a,"other cities of gujarat")
print()
print()
print("*"*100)

# MAP() FUNCTION

number_n1 = ["3", "4", "5", "6", "7"]
print(map(int,number_n1))

num_00 = list(map(int,number_n1))
print(num_00)


def fun_square1(a):
  return a*a

square_1=list(map(fun_square1,num_00))
print(square_1)


def fun_cube1(a):
  return a*a*a

cube_1=list(map(fun_cube1,num_00))
print(cube_1)


def func_1(i): 
   val=(fun_square1(i),fun_cube1(i))
   print(val)


for i in range(10):
  val_1=list(map(func_1,num_00))
  print(val_1)


print()
print()
print("*"*100)

# LIST FUNCTION

list_01 = [1, 2 , 3, 4, 5, 6, 7, 8, 9]


def greater_than(num):
   if num>5:
      return num


num_1 = list(filter(greater_than,list_01))
print(num_1)

print()
print()
print("*"*100)

# REDUCE
 
from functools import reduce

list_10 = [1,2,3,4,5,6,7,8,9]

num_17 = reduce(lambda x,y:x+y,list_10)

print(num_17)
print()
print()
print("*"*100)

# DECORATORS
def fun_sum1():
   return 5


def func_12(num):
   if num==0:
      return fun_sum1()

   if num==1:
      return int 


a = func_12(0)
print(a)

# Example-2

def hello():
   print("hello() fun execution")

   def greet():
      return("greet() function executed")

   def welcome():
      return("welcome() function executed")

   print(greet())
   print(welcome())


print(hello())            

# Example-3

def hello_1(name="jose"):
   print("hello() fun execution")

   def greet_1():
      print("greet() function executed")

   def welcome_1():
      print("welcome() function executed")

   print("Returing Function")

   if name == "jose":
      return greet_1()
   else:
      return welcome_1()

func_return1 = hello_1("jose")
print(func_return1)

# Example-3

def dec_1(func_16):
   def now_exec():
      print("Executing now")
      func_16()
      print("Executed")

   return now_exec   
   

@dec_1
def fun_16():
   print("hello good morning")


print(fun_16())

print()
print()
print("*"*100)

# this works
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{}!' she yelled. '{}! {}, {}!'".format(n,n,n,"say hello"))

# but this also works!
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{0}!' she yelled. '{0}! {0}, {1}!'".format(n,"say hello"))


names = ["Alexey", "Catalina", "Misuki", "Pablo"]
print("'{first}!' she yelled. 'Come here, {first}! {f_one}, {f_two}, and {f_three} are here!'".format(first = names[1], f_one = names[0], f_two = names[2], f_three = names[3]))


L2 = ["Cherry", "Apple", "Blueberry"]

L3 = sorted(L2)
print(L3)
print(sorted(L2))
print(L2) # unchanged

print("----")

L2.sort()
print(L2)
print(L2.sort())  #return value is None


L2 = ["Cherry", "Apple", "Blueberry"]
print(sorted(L2, reverse=True))


L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

print(absolute(3))
print(absolute(-119))

for y in L1:
    print(absolute(y))
