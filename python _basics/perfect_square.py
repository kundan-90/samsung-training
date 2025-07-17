num=int(input("Enter a positive integer: "))
for i in range(num + 1): # in case you enter 1, we need to make sure 1 is also checked
    pow = i * i
    if pow == num:
        print('%d is a pefect square' % num)
        break
    elif pow > num:
        print('%d is not a pefect square' % num)
        break