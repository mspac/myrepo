#function without parameter

#defining the function
def greeting():
    print('welcome to green place')

#calling the function
greeting()   #one time calling - so  1 time execution
greeting()   #again calling - so agian execute the function


# Note: When a function is called once then it will execute once, if called twice then it will be executed twice and so on.



#function with parameter

def sum(a, b):
    print(f'Sum of two values:{a+b}')
sum(10,30)



#Even number or Odd number

#defining the function
def checking(num):
    if num%2 ==0:
        print(f'{num} is even number')
    else:
        print(f'{num} is odd number')

#calling the function
checking(10)


def sum(a,b):
    c=a+b
    return c

d=sum(10,30)
print(f'Sum of two numbers is:{d}')


def m1():
    print('hello ')
m1()
x=m1()
print(x)# x

def m2(a,b):
    c =a+b
    d =a*b
    return c,d
c,d=m2(10,5)
print(f'adition value: {c}')
print(f'subtraction: {d}')


#once function calling another function
def m1():
    print('first function information')
def m2():
    print('second function information')
    m1()
m2()



#Assigning a function to variable in python

# with print
# with reutrn

def m1():
    print('helo')
v=m1
v()

def m2():
    return 10
d=m2()
print(d)


# pass function as a parameter/argument to another function in python

def display(f_p):
    return f_p

def message(a):
    return a


v=display(message('welcome'))
print(v)


#Nested function (one function inside another function in python
def first():
    print('i a outside')
    def second():
        print('i am inside')
    second()

first()


# a function return another function

def first():
    def second():
        print('this fucntion inside')
        return 'hello'
    return second    #don't use () (for return)
a=first()
print(a())


# types of arguments

def sum(a,b):
    c = a+b
    print(c)

#call the function
x =10;y =15
sum(x,y)


#keyword argument (keyword name and paramerer name should be same)
def fun(k):
    print(k)

fun(k='value')

#keyword arguments follow the positionl arguments

def fun(k,k2):
    print(k,k2)
fun('hello',k2='welcome')


def fun(x,*y):  #int ,tuple format
    print(x)
    for i in y:#string,list,tuple,dict,set ,range (but any empty []or values [1,2] )
        print(i)
fun(100)
fun(100,2)

def fun(x,*args,**kwargs):
    print(x)
    for k,v in kwargs.items():
        print(f'{k}-{v}' ,end=' ')
fun(10,one=100,two=200)


# variables are 2 types in python
#
# globals variable : this is general variable we use anywhere
# local variable : which is declared in inside function we can only use inside function only

def fun():
    localvariable =10
    return 10
print(fun())


def fun(c,d):  #local variable c,d
    local_variable ='hello'
    print(c,d)
gl=20
fun(gl,d=10)
# print(d) #not keyword name we can't use to print(d)
print(gl)

one,two =10,[1,2,3,4]
def fun(one,two):   #local variable we can only access inside function
    one = 'hello',   #then  local variable
    print(f'locla vairable {one},gloable vairable:{two}')            # 'hello',[1,2,3,4]
    two[0] =200      # this result will update global variable also because no name with inside function(first loc check) so global will update(last will check)
    print(two)
    #not local variable is creating with same name


# fun('hello','work')
print(one,two)  #first execute this (10,[1,2,3,4]
fun(one,two)
print(one)   # 10
print(two)  #update inside function that new values will refelect

a =10
def fun():
    a=2
    print(a)
    # global a  # we use to update /change the gloable variable inside function  -> but we can't use when local variable also same name
    # a = 300
    print(globals()['a'])  #to use gloable
fun()