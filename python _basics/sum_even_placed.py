input_number = input('Enter the number :')
length = len(input_number)
sum = 0
for i in range(length):
    count_digits = int(input_number[length-i-1])
    if (i+1) % 2 == 0:  
     sum = sum + count_digits
print(sum)