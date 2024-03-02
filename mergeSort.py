#https://github.com/Dan7706


def merge_sort(mylist):
    if len(mylist) > 1:
        mid = len(mylist) // 2
        left_half = mylist[:mid]
        right_half = mylist[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                mylist[k] = left_half[i]
                i += 1
            else:
                mylist[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            mylist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            mylist[k] = right_half[j]
            j += 1
            k += 1

    return mylist



