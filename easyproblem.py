def decide(ans: list):
    i=0
    for i in range(0,len(ans)):
        if(ans[i] == 1):
            return "HARD"
    return "EASY"

ans=[0,0,1]

print(decide(ans))


