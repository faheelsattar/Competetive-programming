def paranthesisGenerator(open ,close, n, s=[]):
    if close == n:
        print(s)
        return
    else: 
        if open > close :
            s.append(")")
            paranthesisGenerator(open, close+1, n, s)
            s.pop()

        if open < n :
            s.append("(")
            paranthesisGenerator(open+1, close, n, s)
            s.pop()


paranthesisGenerator(0,0,3)
        
