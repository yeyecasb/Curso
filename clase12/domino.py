a=[0,1,2,3,4,5,6]
b=[0,1,2,3,4,5,6]

for i in a:
    for j in b:
        if i<=j:
            print(i, '|',j," ",end=" ")
    print('')

print('')
print('')
for i in range(7):
    for j in range(i,7):
            print(i, '|',j," ",end=" ")
    print('')