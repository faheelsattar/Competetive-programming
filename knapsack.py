import operator
def maxValue(wholelist, capacity):
    maxprofit=0
    wholeList.sort(reverse=True, key=operator.itemgetter(2))
    for i in range(0,len(wholelist)):
        if wholelist[i][0] <= capacity:
            capacity = capacity - wholelist[i][0]
            maxprofit =maxprofit + wholelist[i][1]
        else:
            maxprofit =maxprofit+(wholelist[i][1] * (capacity/wholelist[i][0]))
            capacity = capacity - (wholelist[i][0]* (capacity/wholelist[i][0]) )
            break
        
    print(capacity, maxprofit)
val = [60, 40, 100, 120]
wt = [10, 40, 20, 30] 
capacity = 50
wholeList=[]

for i in range(0, len(val)):
    wholeList.append([wt[i], val[i], val[i] / wt[i] ])

maxValue(wholeList, capacity)
