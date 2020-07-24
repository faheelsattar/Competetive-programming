def sumCalculation(arr: list):
    best =0 
    sum=0
    for k in range(0, len(arr)):
        sum = max(arr[k], sum+arr[k])
        best = max(best, sum)
    return best


## [-1,-2,1,4,2,3,-6,0,2]  [-2,2,1,0]

arr= [-1,-2,1,4,2,3,-6,0,2]

print(sumCalculation(arr))


    
