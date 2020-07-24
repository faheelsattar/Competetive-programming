def fibonacci(max):
    prev= 0 
    next= 1
    i=1
    while i<= max:
        sum = next+prev
        prev = next
        next = sum
        i= i+1
    ## print sum of fibo series
    print(prev)
    prevholder = str(prev)
    ## print last digit of fibo sunm
    print(prevholder[len(prevholder)-1])
fibonacci(331)

#0 1 1 2 3 5 8 13 21 34 55 