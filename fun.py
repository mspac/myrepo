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
    print(globals()['a'])  #to use gloable variable (when locla variable also with same)
m2()
print(a)