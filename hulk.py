def feelings(n:int):
    q= "I hate that"
    r= " I love it "
    holder=""
    for i in range(1,n+1):
        if i % 2 == 0:
            holder+= r
        else:
            holder+=q
    return holder

print(feelings(3))