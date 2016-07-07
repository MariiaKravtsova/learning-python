def bubbleSort(array):
    """Implementation of a bubble sort"""
    isSorted = False
    i = 0
    length = len(array) - 1
    while not isSorted:
        isSorted = True
        for i in range(0, length):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                isSorted = False
                i = i + 1

myArray = [1, 2, 5, 3, 4]
bubbleSort(myArray)
print(myArray)
