def minSteps(friendspos, steps):
    if (friendspos == 0):
        return steps
    elif (friendspos >= 5):
        steps = steps+1
        friendspos= friendspos -5
        return minSteps(friendspos, steps)
    elif (friendspos >= 4):
        steps = steps+1
        friendspos= friendspos - 4
        return minSteps(friendspos, steps)
    elif (friendspos >= 3):
        steps = steps+1
        friendspos= friendspos - 3
        return minSteps(friendspos, steps)
    elif (friendspos >= 2):
        steps = steps+1
        friendspos= friendspos - 2
        return minSteps(friendspos, steps)
    elif (friendspos >= 1):
        steps = steps+1
        friendspos= friendspos - 1
        return minSteps(friendspos, steps)
        
print(minSteps(5,0))
