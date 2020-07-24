def commonElements(a:list, b:list):
    a.sort()
    b.sort()
    arrlength=0
    counter=0
    if len(a) > len(b):
        arrlength = len(a)
    elif len(b) > len(a):
        arrlength = len(b)
    for i in range(0,arrlength):
        if a[i] in b:
            counter = counter+1
    return counter

a=[5,2,8,9,4]
b=[3,2,9,5]
print(commonElements(a,b))
        
    
