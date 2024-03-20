from customStack import Stack

def infixToPostfix (infixToken):
    #create a disctonary to store operator's according their precedence:
    precdence ={}
    
    precdence["-"] = 2
    precdence["+"] = 2
    precdence["/"] = 3
    precdence["*"] = 3
    precdence[")"] = 1
    precdence["("] = 1
    
    #create a list to store postfix expressions after conversion from infix :
    postfixEpression = []
    
    #invoke stack object to evaluate operator precedence:    
    openStack = Stack()
    
    token = infixToken.split()
    
    for token in infixToken:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789" :
            postfixEpression.append(token)
        elif token == "(" :
            openStack.push(token)
        elif token == ")" :
            topToken = openStack.pop()
            while topToken != "(" :
                postfixEpression.append(topToken)
                topToken = openStack.pop()
        else :
            while not(openStack.isEmpty()) and (precdence[openStack.top()] >= precdence[token]):
                    postfixEpression.append(openStack.pop())
            openStack.push(token)
            
    while not(openStack.isEmpty()):
        postfixEpression.append(openStack.pop())
    return " ".join(postfixEpression)
    
print("input string :- A*B+C*D ",end='\n')    
print(infixToPostfix("A*B+C*D"))
print("input string :- (A+B)*C-(D-E)*(F+G)",end='\n')  
print(infixToPostfix("(A+B)*C-(D-E)*(F+G)"))