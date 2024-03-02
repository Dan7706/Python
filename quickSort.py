#https://github.com/Dan7706


def quick_sort(mylist):
    if len(mylist) <= 1:
        return mylist
    else:
        pivot = mylist[0]
        less_than_pivot = [x for x in mylist[1:] if x <= pivot]
        greater_than_pivot = [x for x in mylist[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)





