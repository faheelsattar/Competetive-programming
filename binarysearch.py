import math
def binarySearch(arr:list, val:int):
    mid = 0
    low=0
    high =len(arr)
    while low <= high:
        print(low, high, mid)
        mid = math.floor((low + high) / 2)
        if val == arr[mid]:
            return val
        elif val < arr[mid]:
            high= mid-1
        elif val > arr[mid]:
            low= mid+1
    return 0        

arr = [1,5,6,7,20,23,45,54,56,76,87]

print(binarySearch(arr, 1))
            
            
