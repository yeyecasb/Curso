a=int(input('Ingrese el Primer Número '))
b=int(input('Ingrese el Segundo Número '))

print('Usted ingresó los números ', a,' y ',b)
print('La suma de los números es: '+ str(a+b))
print('La resta de los números es: '+ str(a-b))
print('La multiplicación de los números es: '+ str(a*b))
print('La división de los números es: '+ str(a/b))
resultado_division=a/b
if resultado_division.is_integer():
    print('El resulatdo de la división es un entero')
else:
    print('El resultado de la división es un decimal')