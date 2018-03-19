def binarySearch(aList, item):
    '''
    @type aList[int]
    @type item int
    @rtype int (None)

    '''
    s = 0
    e = len(aList)-1
    while s <= e:
        mid = (s+e)//2
        if aList[mid] < item:
            s = mid + 1
        elif aList[mid] > item:
            e = mid -1
        else:
            return mid + 1
    return None

print(binarySearch([1, 4, 6, 7, 10, 11], 7))
