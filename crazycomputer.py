def remainingWords(n, c, seconds:list):
    counter=0
    for i in range(0,n-1):
        if seconds[i+1] - seconds[i] <=c:
            counter = counter+1
        else:
            counter=0
    if counter == 0:
        return 0
    else:
        return counter+1
print(remainingWords(6,1,[1, 3, 5, 7, 9, 10]))