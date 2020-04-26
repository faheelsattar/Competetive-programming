def yearCalc(a, b, count):
    counter = count
    if a > b:
        return counter
    else:
        a=a*3
        b=b*2
        counter=counter+1
        return yearCalc(a,b, counter)

print(yearCalc(1,1,0))