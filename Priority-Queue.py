def heapify(arr , n ,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if ( l < n and arr[i] < arr[l]):
        largest = l
    if (r < n and arr[largest] < arr[r]):
        largest = r

    if (largest != i):
        arr[i] , arr[largest] = arr[largest] , arr[i]
        heapify(arr , n , largest)

def insert(arr , newNum):
    size = len(arr)
    if size == 0:
        arr.append(newNum)
    else:
        arr.append(newNum)
        for i in range((size // 2) - 1, -1, -1):
            heapify(arr, size , i)

def deleteNode(arr , num):
    size = len(arr)
    i = 0
    for i in range(0 , size):
        if num == arr[i]:
            break

    arr[i] , arr[size - 1] = arr[size - 1], arr[i]

    arr.pop()

    for i in range((len(arr) // 2) - 1 , -1, -1):
        heapify(arr , len(arr) , i)

arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))