# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score.
# You are given  scores.
# Store them in a list and find the score of the runner-up.

scoreList =[8,7,6,5,4]
n = len(scoreList)

def findRunnerUp(scoreList,n):
    scoreList.sort()
    winner =scoreList[0]
    runner_up=0
    for i in range(n):
        if scoreList[i] > winner:
            temp = scoreList[i]
            runner_up = winner
            winner = temp
            print("winner",winner)
            print("runner_up",runner_up)
        if scoreList[i] == winner:
            winner = scoreList[i]
            print("winner",winner) 
        if scoreList[i] < winner:
            runner_up = scoreList[i]
            print("runner_up",runner_up)
        print(i)
    return runner_up   

print("n",n)
print(findRunnerUp(scoreList,n))
