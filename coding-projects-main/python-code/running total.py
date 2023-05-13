#This code provides a running total of the sum of a series of numbers

total = 0

print('Beginning', total)

for num in [2, 1, 7, 5, 12, 16, 99, 69, 4, 20, 66,]:
    total += num
    print(total, num)
    
print('End', total)
