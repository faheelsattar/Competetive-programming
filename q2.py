def mul(a, b):
    checker=False
    if b <0:
        b=abs(b)
        checker= True
    if b == 0:
        return 0   
    if checker == True:
        return -a + mul(-a, b-1)
    else:
        return a + mul(a, b-1) 
        


print(mul(1,-4))