def regresiva(a):#cuenta regresiva: hace una lista que va de atras pa delante a partir del numero
    x=[]
    for i in range(0, a+1):
        x.append(a-i)
        return x
        
regresiva(9)

def printandreturn(lst):
    print (lst[0])
    return lst[1]
printandreturn([1,2,3,4])

def firstpluslength(lst): #devuelve la suma del primer valor y el largo del arreglo
    return lst[0] + len(lst)
firstpluslength([1,2,3,4])

def mayoreskelsegundo(lst):#devuelve una nueva lista solo con los valores que son mayores que el segundo
    lisneu = []
    if len(lst)>2:
        for i in lst:
            if lst[i]>lst[1]:
                lisneu.append(lst[i])
                print (len(lisneu))
                return lisneu
    else:
        return False
mayoreskelsegundo([1,2,3,4,5])    

def esetamañoesevalor(a,b):#una lista cuya longitus es a y cuyos valores simepre son b
    listi=[]
    for i in range(a):
        listi.append(b)
    return listi
esetamañoesevalor(5,7)

