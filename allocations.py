def allocations(arr, B):
    counter=0
    if len(arr) > 0:
        for i in range(0, len(arr)):
            if arr[i] <= B:
                B = B - arr[i]
                counter = counter+1
    return counter
        

cases = int(input())
for i in range(1, cases+1):
    N,B = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    print("Case #", i ,":", allocations(arr, B))
