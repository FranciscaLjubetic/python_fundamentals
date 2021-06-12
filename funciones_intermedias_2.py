x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
##Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
#En el directorio sports_directory, cambia 'Messi' a 'Andres'
#Camba el valor 20 en z a 30

x[1][0]=15
print(x)

students[0]['last_name']='Bryant'
print(students)

sports_directory['soccer'][0]='Andres'
print(sports_directory)

z[0]['y']= 30
print(z)


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(lst):
    for dicc in lst:
        str_dicc=[]
        for value, key in dicc.lst():
            str_dicc.append(f'{value},-{key}')
            print(', '.join(str_dicc))

iterateDictionary(students)

# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# Bonus: Hacer que aparezcan exactamente así!
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

def iterateDictionary2(keyname, some_list):
    for i in range(len(some_list)):
        print(some_list[f'{keyname}'])
        
iterateDictionary2 ('first_name', students)