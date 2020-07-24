def checker(words, word, letter,i, n):
    print(letter, i)
    wordholder=""
    for k in  range(letter,i):
        wordholder = wordholder+word[k]

    print(wordholder)
    if wordholder in words:
        return True
    return False
            
def wordBreak(words, word, letter, n,answer):
    if letter < n:
        for i in range(0, n):
            if checker(words, word, letter,i, n):
                answer.append(word)
                wordBreak(words, word, letter+1, n, answer)
                answer.pop()
    else:
        for i in range(0, len(answer)):
            print(answer[i])
        
    




word= "ilikesamsungmobile"
n= len(word)
word2= "ilikeicecreamandmango"
words=["mobile","samsung","sam","sung", "man","mango", "icecream","and", "go","i","love","ice","cream"]

wordBreak(words, word, 0, n, [])