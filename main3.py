l = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List:", l)

#variable to store the sum of the list
count = 0

#Finding the sum
for i in l:
    count += i

#divide the total number of elements
avg = count/len(l)

print("sum = ", count)
print("average = ", avg)

#Sorting the list elements
l.sort()

#printing the first element
print("Smallest element is:", l[0])

#printing the last element
print("Largest element is:", l[-1])