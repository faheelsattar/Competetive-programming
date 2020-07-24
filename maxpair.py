def maxPair(arr:list):
    ## calc highest num
    holdermax1 = arr[0]
    holdermax2 = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > holdermax1:
            holdermax1 = arr[i]
    
    for i in range(0, len(arr)):
        if arr[i]> holdermax2 and arr[i] < holdermax1:
            holdermax2 = arr[i]
    
    return holdermax1 * holdermax2
            

n = int(input("Enter the length of an array"))
arr = [int(x) for x in input().split()]
print(maxPair(arr))
