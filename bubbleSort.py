#https://github.com/Dan7706

def bubble_sort(mylist):
    length_of = len(mylist)
    for i in range(length_of):
        for j in range(0, length_of - i -1):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
    return mylist
