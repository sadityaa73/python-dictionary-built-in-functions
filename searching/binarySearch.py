import math

def binarySearch (key,list,low,high):
    
    if high >= low :
        
        mid = low + (high - low)//2
        print("mid",mid)
        
        if key == list[mid] :
            return print("key is found!!")
        elif key > list[mid] :
            binarySearch(key,list,mid+1,len(list)-1)
        elif key < list[mid] :
            binarySearch(key,list,low,mid-1)
        else:
            return -1
        
list = [2,3,4,10,40]

binarySearch(2,list,0,len(list)-1)