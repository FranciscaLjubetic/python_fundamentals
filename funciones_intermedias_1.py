import random
def randInt(min=0, max=100):
    if max<min:
        print('Error')
        return 'error'
    num= round(random.random()*(max-min)+min)
    print(num)
    return num
#print(randInt()) 		    # debería imprimir un número aleatorio entre 0 a 100
#print(randInt(max=50)) 	    # debería imprimir un número aleatorio entre 0 a 50
#print(randInt(min=50)) 	    # debería imprimir un número aleatorio entre 50 a 100
#print(randInt(min=50, max=500))    # debería imprimir un número aleatorio entre 50 y 500

randInt(50, 150)  

def loto():
    cartilla=[]
    bolita= randInt(0,36)
    for i in range(6):
        cartilla[i]=bolita
        for j in range(6):
            if cartilla[i]== cartilla[j+1]:
                cartilla[j+1]=bolita
            elif cartilla[i]!= cartilla[j+1]:
                break
    print (cartilla)
    return cartilla

loto()


