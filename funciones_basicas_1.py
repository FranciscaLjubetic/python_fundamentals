#5
def a():
    return 5
print(a())

def a():
    return 5
print(a()+a()) #10

#3
def a():
    return 5
    return 10
print(a()) #5,10...es solo 5.no devuelve mas que un return


#4
def a():
    return 5
    print(10)
print(a()) # 5, 10 es solo 5, si la invocaramos, imprimiria 10

#5
def a():
    print(5)
x = a()
print(x) #no tiene return, asi que capaz que nada. en verdad es 5 del print y nada para x

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3)) #8

def a(b,c):
    return str(b)+str(c)
print(a(2,5)) # 2 5


#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a()) #100 10 check

def z(b,c):
    if b < c:
        return 7
    else:
        return 14
    return 3
print(z(2,3)) #7
print(z(5,3)) #14
print(z(2,3) + z(5,3)) #21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5)) #8


#11
b = 500
print(b)
def W():
    b = 300
    print(b)
print(b)
W()
print(b)# 500 500 300 500

#12
b = 500
print(b)
def a():
    b = 300
    print(b) 
    return b 
print(b) #500
a() #300
print(b) #500

#13
b = 500
print(b)#500
def a():
    b = 300
    print(b)
    return b
print(b) #500
b=a() #print 300 guarda 300
print(b) #300, 500 500 300 300 CHECK

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a() #1 #3 #2 CHECK

def a():
    print(1)
    x = b()
    print(x)
    return 10 
def b():
    print(3)
    return 5
y = a() #1 3 5 10 CHECK
print(y) 