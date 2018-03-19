def qsort(aList):
    '''
    @type aList list[int]
    @rtype alist list[int]
    '''
    if len(aList)<=1 :
        return aList
    else:
        pivot = aList[0]
        less = [x for x in aList if x < pivot]
        more = [x for x in aList if x>pivot]
        return qsort(less) + [pivot] + qsort(more)



print(qsort([3, 5, 8, 1, 2, 9, 4, 7, 6]))
