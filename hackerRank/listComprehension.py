# Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer .
# Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to .
# Here,0<=i<=x;o<=j<=y;0<=k<=z.Please use list comprehensions rather than multiple loops, as a learning exercise.

x = int(input("enter the value of x:"))
y = int(input("enter the value of y:"))
z = int(input("enter the value of z:"))
n = int(input("enter the value of n:"))


def possibleCordinated(valX,valY,valZ,valN):
    print([[i,j,k] for i in range(valX+1) for j in range(valY+1) for k in range(valZ+1) if i+j+k != valN])


possibleCordinated(x,y,z,n)