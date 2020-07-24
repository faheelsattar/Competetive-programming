def minProduct(arr):
    checker=False
    productholder=1
    for i in range(0, len(arr)):
        if arr[i] < 0:
            checker = True
    
    if checker == True:
        for i in range(0, len(arr)):
            if arr[i] !=0:
                productholder = productholder*arr[i]
        print(productholder)
    else:
        min =arr[0]
        for i in range(0, len(arr)):
            if arr[i] < min:
                min= arr[i]
        print(min)
            


arr= [-1, -1, -2, 4, 0]

minProduct(arr)