def bubbleSort(list):
    for i in range(len(list)):
      for j in range(len(list)-1-i):
          if list[j] > list[j+1]:
              list[j],list[j+1]  = list[j+1],list[j]
    display(list)          
                       

def display(list):
    print(list)
list=[7,2,12,8,3]
bubbleSort(list)