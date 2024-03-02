#https://github.com/Dan7706


def selection_sort(mylist):
    length_of = len(mylist)
    for i in range(length_of):
        min_index = i
        for j in range(i+1, length_of):
            if mylist[j] < mylist[min_index]:
                min_index = j
        mylist[i], mylist[min_index] = mylist[min_index], mylist[i]
    return mylist
