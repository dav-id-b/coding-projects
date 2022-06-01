#This code will determine the number of int values in a list
#Additionally, it will detemine the total sum of the list values
#Lastly, it will determine the average of the values in the list & print all three

count = 0
total = 0

print('Beginning', count, total)

for num in [3, 5, 12, 23, 54, 7, 56, 23, 6, 1]:
    count += 1
    total = total + num 
    print(count, total, num)

print('End', count, total, total / count)
