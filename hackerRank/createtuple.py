# Given an integer,n ,n and  space-separated integers as input,
# create a tuple, , of those  integers. Then compute and print the result of .

print("enter the value of n integer");
n  = int(input());

print("enter number of interger");
integer_list = map(int ,input().split(" "));

newTuple = tuple(integer_list);

print(hash(newTuple));

