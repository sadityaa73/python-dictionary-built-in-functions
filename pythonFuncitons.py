# demo how to declear and use function in python:
def sum(a,b):
    c = a+b;
    return c;


a = int(input("enter value of a:-\t"));
b = int(input("enter value of b:-\t"));

finalSum = sum(a,b);

print("finalSum:\t",finalSum);