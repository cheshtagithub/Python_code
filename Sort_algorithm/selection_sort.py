n = int(input("Enter the size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter the data of node {i}: ")))
print("Original array is:", arr)

def Selection(arr):
    length = len(arr)
    for i in range(length - 1):
        min_ind = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_ind]:
                 min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
        
Selection(arr)
print("Sorted array is:", arr)
