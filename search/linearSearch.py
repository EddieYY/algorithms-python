def linearSearch(aList, Target):
    '''
    @ type aList[int]
    @ type Targe int
    @ rtype int

    '''
    for i in range(len(aList)):
        if Target == aList[i]:
            return i
    return "not in scope"

aL=[1, 3, 1, 2, 10, 5, 111]

print(linearSearch(aL, 111))
