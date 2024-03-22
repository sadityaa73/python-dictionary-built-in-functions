
def selectionSort (list) :
    for i in range(0,len(list)):
        min = list[i]
        j=i+1
        while j < len(list) :
            if min > list[j] :
               temp = min
               min = list[j]
               list[j] = temp
            j = j+1
        list[i] = min
    display(list)

        
def display(list):
    print(list)
        
newList = [7,12,8,4,2]
selectionSort(newList)