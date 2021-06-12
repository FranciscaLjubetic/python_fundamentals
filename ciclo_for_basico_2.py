def tamanogrande(lst):
    for i in range(len(lst)):
        if lst[i]>0:
            lst[i]= 'Big'
    print(lst)
    return lst
tamanogrande([1,2,0,-4,5,6])

def contpositivosw(lst):
    x=0
    for i in range(len(lst)-1):
        if lst[i]>0:
            x= x+i
    print(x)
    return x

contpositivosw([1,2,0,-4,5,6])

def sumatotal(lst):
    sum=0
    for i in range(len(lst)):
        sum= sum+ lst[i]
    print(sum)
    return sum
sumatotal([1,2,0,-4,5,6])

def promedio(lst):
    pr=0
    for i in range(len(lst)):
        pr= pr+ lst[i]
    print(pr/len(lst))
    return pr/len(lst)
promedio([1,2,0,-4,5,6])

def longitud(lst):
    print(len(lst))
    return len(lst)
longitud([1,2,0,-4,5,6])

def minimor(lst):
    min=0
    for i in range(len(lst)):
        if lst[i]<min:
            min= lst[i]
    print(min)
    return min
    
minimor([1,2,0,-4,5,6])

def maximor(lst):
    max=0
    for i in range(len(lst)):
        if lst[i]>max:
            max= lst[i]
    print(max)
    return max
    
maximor([1,2,0,-4,5,6])

def analisisfinal(lst):
    mn=0
    mx=0
    sm=0
    dcc={}
    for i in range(len(lst)):
        sm= sm + lst[i]
        dcc[i]=lst[i]
        if lst[i]>mx:
            mx= lst[i]
        elif lst[i]<mn:
            mn= lst[i]
    print(f'Mínimo: {mn}')
    print(f'Máximo: {mx}')
    print(f'Longitud de lista:{len(lst)}')
    print(f'Promedio: {sm/len(lst)}')
    print(dcc)
    return max
    
analisisfinal([1,2,0,-4,5,6])

def listainversa(lst):
    alm=0
    for i in range(len(lst)):
        alm= lst[i]
        lst[i]=lst[len(lst)-1-i]
        lst[len(lst)-1-i]= alm
    print(lst)
    return lst
    
listainversa([1,2,0,-4,5,6])