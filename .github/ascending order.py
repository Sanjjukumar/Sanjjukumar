list1=[]
def input_list():
    for i in range (1,6):
        a=int(input("Enter the value:"))
        list1.append(a)

def bubblesort(array):
    for i in range (len(array)):
        for j in range (0,len(array)-i-1):
            if array[j]>array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

data =list1
input_list()
bubblesort(list1)
print('Sorted Array in Ascending Order:')
print(data)
