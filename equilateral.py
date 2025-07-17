num = int(input('Enter number'))
for i in range(num):
    for j in range(i):
        if i == j:
         print('*', end='')
    print()