def lcm(num1, num2):
    arr=[]
    max=0
    product=1
    if num1 > num2:
        max = num1
    else:
        max= num2
    for i in range(1,max):
        if (num1 % i == 0 or num2 % i == 0) and num1 != i and num2 != i:
            arr.append(i)
    print(arr)

    for i in range(0, len(arr)):
        product= product* arr[i]
    print(product)

    

lcm(761457, 614573 )