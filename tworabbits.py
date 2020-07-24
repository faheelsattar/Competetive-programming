def moment(x,y,a, b, counter):
    if x==y:
        return counter
    elif x>y:
        return -1
    else:
        x=x+a
        y=y-b
        counter=counter+1
        return moment(x,y,a,b, counter)

print(moment(1, 3, 1, 1,0))