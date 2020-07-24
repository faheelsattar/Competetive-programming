def subsequence(word):
    counter=0
    for i in range(0,len(word)):
        if word[i] == "Q":
            for j in range(i+1,len(word)):
                if word[j] == "A":
                    for k in range(j+1,len(word)):
                        if word[k] == "Q":
                            counter= counter+1

    return counter                 
        





print(subsequence("QAQQQZZYNOIWIN"))