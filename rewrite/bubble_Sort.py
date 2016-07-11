def bubbleSort(array):
    i = 0
    length = len(array) - 1
    isSorted = True
    while isSorted:
        isSorted = False
        for i in range(0, length):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                i = i + 1
                isSorted = True

myArray = [1, 3, 4, 2, 0]
bubbleSort(myArray)
print(myArray)