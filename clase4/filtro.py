# Filtro de elementos: Escribe un programa que tome una lista de números como entrada
# y muestre solo los elementos que son mayores que 5.
numeros=[5,7,1,6,4,2,9,3,8]
filtrados=[]
for numero in numeros:
    if numero > 5:
        filtrados.append(numero)

print(filtrados)