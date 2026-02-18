n = int(input("Enter size: "))
arr = []
for i in range(n):
    arr.append(int(input()))
print("original array is ", arr)
def insertion(arr):
    x = len(arr)
    for i in range(1, x):
        key = arr[i] 
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[ j ] 
            j -= 1 
        arr[j + 1] = key 
insertion(arr)
print("sorted array is", arr)

