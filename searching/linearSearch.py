def linearSearch(list,key):
    for i in range(len(list)):
        print("values",list[i],"at index", i)
        if key == list[i] :
            return print("key",key,"is found at index",i)
    return print("not found")
        
list = [12,32,5,32,2,4]

linearSearch(list,5)