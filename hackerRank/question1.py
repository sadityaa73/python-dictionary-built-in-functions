# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
n = int(input("enter number:"));
print(n);
def check(n):
    if (n%2)==1:
        print("Weird")
        return 
    if (n%2)==0 and n in range(2,5):
        return print("Not Weird") 
    if (n%2)==0 and n in range(6,20):
        return print("Weird")
    if (n%2)==0 and n > 20:
        return print("Not Weird")
        
check(n)   