n = int(input("Enter the length of array: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter the data for node {i}: ")))
    
print("The original array is: ",arr)

def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len - 1):
        for j in range(arr_len - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    

bubble_sort(arr)
print("The sorted array is: ",arr)
