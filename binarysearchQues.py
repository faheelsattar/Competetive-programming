import math
def maxElem(arr:list):
    low= 0
    high= len(arr)
    while low <= high:
        mid = math.floor((low+high)/2)
        if arr[mid] > arr[mid-1] and arr[mid]> arr[mid+1]:
            return arr[mid]
        elif arr[mid] < arr[mid+1]:
            low=mid+1
        elif arr[mid] > arr[mid+1]:
            high=mid-1
        
arr=[8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1]
print(maxElem(arr))
