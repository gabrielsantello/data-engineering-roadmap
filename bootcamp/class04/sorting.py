# Implementation of the selection sort algorithm
list = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]

# Sorting the list
print("List sorted with custom function:", list)