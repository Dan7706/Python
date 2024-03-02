#https://github.com/Dan7706

def insertion_sort(mylist):
    length_of = len(mylist)
    for i in range(1, length_of):
        key = mylist[i]
        j = i - 1
        while j >= 0 and key < mylist[j]:
            mylist[j + 1] = mylist[j]
            j -= 1
        mylist[j + 1] = key
    return mylist



