
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyList:
    def __init__(self):
        self.head = None

    def append(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            self._append(val, self.head)

    def _append(self, val, node):
        if node.next == None:
            node.next = Node(val)
        else:
            self._append(val, node.next)

    def get(self, k):
        node = self.head
        if k > 0:
            for i in range(1, k+1):
                node = node.next
        if node!= None:
            return node.val
        else:
            return "list index out of range"

    def llen(self):
        k=0
        node = self.head
        while node:
            k +=1
            node = node.next
        return k


    def lprint(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next

def revList(aMyList):
    l = aMyList.llen()
    rl = MyList()
    for i in range(l):
        rl.append(aMyList.get(l-i-1))
    return rl
