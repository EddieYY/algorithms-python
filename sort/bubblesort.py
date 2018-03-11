def BubSort(aL):
    passnum = len(aL)-1
    exchange = True
    while exchange and passnum>0:
        exchange = False
        for i in range(passnum):
            if aL[i]> aL[i+1]:
                tmp = aL[i]
                aL[i] = aL[i+1]
                aL[i+1] = tmp
                exchange = True
        passnum = passnum-1

alist=[10000, 2, 5, 20,30,40,90,50,60,70,80,100,110]
BubSort(alist)
print(alist)
