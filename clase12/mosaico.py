num=int(input('Ingrese el tamaño del mosaico:'))

for i in range(num):
    for j in range(num):
        if i==j:
            print('X ', end='')
        elif i<j:
            print('D ', end='')
        else:
            print('U ', end='')
    print()