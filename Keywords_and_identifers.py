# true or  false
print(5==5)
print(5>5)

#comparing two elements
print(None==None) #true
print(None==10) #false

#void 
class a_void():
    a=10
    b=20
    c=a+b
x=a_void()
print(x)

#and or not
print(True and False) #false
print(True or False) #true
print(not True) #false 

#as
import math as mymath
print(mymath.pi) #3.141592653589793

#break 
for i in range(1,11):
    if i==10:
        break
    print(i)

#continue
for i in range(1,8):
    if i == 5:
        continue
print(i)

#class
class Myclass:
    def mymethod1(parameters):
        print("method 1")
    def mymethod2(parameters):
        print("method 2")

ab1=Myclass()
ab1.mymethod1() 
ab1.mymethod2()

#def
def function_name(parameters):
    pass #function with no body
function_name(10)

#if elif else
num =10
if num ==10:
    print("its 10")
elif num == 5:
    print("its 5")
else:
    print('invalid')

#try raise except finnaly
#try:
   # x = 10
   # raise ZeroDivisionError
#except ZeroDivisionError:
   # print("no division")
# finally:
   # print("sucess")

#global 
globvar=10
def read1():
    print(globvar)
def write1():
    global globvar
    globvar=5
def write3():
    globvar=50
read1()
write1()
read1()
write3()
read1()

#lambda
a = lambda x:x*5
for i in range(1,10):
    print(a(i))

#nonlocal
def Outer_function():
    a=5
    def inner_function():
        nonlocal a
        a=10
        print("inner function",a)
    inner_function()
    print("Outer function ",a)
Outer_function()


#while
i=5
while(i>0):
    print(i)
    i-=1
#with
with open('example.txt','w')as my_file:
    my_file.write('hello worl')

#yield
def gen():
    for i in range(6):
        yield i*i
g=gen()
for i in gen():
    print(i)