def insertionSort(list):
    for i in range (1,len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j] :
                list[j+1] = list[j]
                j -=1
        list[j+1] = key
            
    display(list)
           
def display(list):
    print(list)
    
list =[7,4,6,5,12]

insertionSort(list)