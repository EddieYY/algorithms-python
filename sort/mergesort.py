def Lsplit(List):
    mid = len(List)//2
    RightL = List[mid:]
    LeftL = List[:mid]
    return LeftL, RightL


def LSort(LeftL, RightL):
    result = []
    i, j = 0, 0

    while len(LeftL)>i and len(RightL)>j:
        if LeftL[i] > RightL[j]:
            result.append(RightL[j])
            j+=1
        else:
            result.append(LeftL[i])
            i+=1
    while len(LeftL)>i:
        result.append(LeftL[i])
        i+=1

    while len(RightL)>j:
        result.append(RightL[j])
        j+=1

    return(result)


def merge_sort(input_list):
    #if list contains only 1 element return it
    if len(input_list) <= 1:
        return input_list
    else:
        #split the lists into two sublists and recursively split sublists
        Left, Right = Lsplit(input_list)
        left_sublist = merge_sort(Left)
        right_sublist = merge_sort(Right)
        #return the merged list using the merge_list function above
        return LSort(left_sublist,right_sublist)


#test run
number_list = [3, 2, 3, 6, 7, 10, 23, 1, 0]
print(merge_sort(number_list))
#[0, 1, 2, 3, 3, 6, 7, 10, 23]
