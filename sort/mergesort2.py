def mergeSort(aList):
    if len(aList)>1:
        mid = len(aList)//2

        leftL = aList[:mid]
        rightL = aList[mid:]

        leftL = mergeSort(leftL)
        rightL = mergeSort(rightL)

        i, j = 0, 0
        out = []
        while i<len(leftL) and j<len(rightL):
            if leftL[i] < rightL[j]:
                out.append(leftL[i])
                i+=1
            else:
                out.append(rightL[j])
                j+=1
    
        return out+leftL[i:]+rightL[j:]
    else:
        return aList

number_list = [3, 2, 3, 6, 7, 10, 23, 1, 0]
print(mergeSort(number_list))

        
