a ='string python'   #global variable
def m1():
    global a
    a =1000
    print(a)   #1000
print(a)       #'string'
a =10          #gloabl variable value changed
print(a)       # 10
m1()
print(a)       # 1000

a=20
def m2():
    a=10
    print(a)
    print(globals()['a'])  #to use gloable variable (when locla variable also with same name)
m2()
print(a)

##recursive function
def factorial(n):
    if n ==0:      #always base condition required for recursive function
        return 1
    else:
        return n*factorial(n-1)
x=factorial(4)
print(f'Facorial of 4 is {x}')

def f2(n):
    fact =1
    while (n>0):
        fact =fact*n
        n-=1               # - + *((for Numbers)  local variable    : n
    print(fact)
a=4
f2(a)
print(a)

d=10
c=[2,3,4,5]
def f2(m,n):
    m-=10
    print(m)
    n[0]=300             # [] [ ::] (for sequen of elements/group of elements )  gloabl variable (until if not created local variable with same name(parameter name)
    print(n)
f2(d,c)
print(d)
print(c)

d=10
c=[2,3,4,5]
def f2(m,n):
    m-=10
    print(m)
    n=['apple','book','cat']                 #Note : i am creating local variable with same name(parameter name)
    n[0]=300             # [] [ ::] (for sequen of elements/group of elements )  gloabl variable (until if not created local variable with same name(parameter name)
    print(n)
f2(d,c)
print(d)
print(c)