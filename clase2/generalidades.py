#booleano
x=True
y=False
print(x and y)#dara False, ambos elementos debería ser true para dar true
print(x or y)#dara True
print(not y)#True

print('------ENTEROS------')

n = 10
m = 5
print(n+m)
print(n*m)
print(n-m)
print(n/m)
print(n%m) #resto

print('------FLOAT------')
j=3.1416
k=2.7182
print(j+k)
print(j-k)
print(j*k)
print(j/k)
print(j%k)

print('------COMPLEJOS------')
l=3+2j
m=1-4j
print(l+m)
print(l-m)
print(l*m)
print(l/m)

print('------STRING (CADENA DE TEXTO)------')
p1='Hola'
p2='Mundo'
print(p1 + " " + p2)
print(p1,p2)
print(len(p1))#longitud caracteres
print(p1.upper())#pasar mayuscula
print(p1.lower())#pasar minuscula

print('------TUPLA------')
t1=(1,2,3)
t2=('a','b','c')
print(t1+t2)
print(t1[1])
print(t2.index('c'))

print('------LISTA------')
x=[1,2,3]
y=['a','b','c']
print(x)
print(y)

print('------SET------')
mi_primer_set=set()
mi_primer_set.add(1)
mi_primer_set.add(n)
mi_primer_set.add(p1)
print(mi_primer_set)

mi_lista= list(mi_primer_set)
print(mi_lista[1])

print('------DICCIONARIOS------')
mi_diccionario={'nombre':'Michael','edad':25, 'pais':'Chile'}
print(mi_diccionario['nombre'])

mi_diccionario['profesion']='aviador'
print(mi_diccionario['profesion'])
print(mi_diccionario)
