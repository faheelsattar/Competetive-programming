def wrongsub(n:int, k: int):
    i=0
    for i in range(0,k):
        if (n % 10 == 0):
            n = n/10
        else:
            n=n-1
    return n

print(wrongsub(512, 4)) 