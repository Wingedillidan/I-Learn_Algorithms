class LinkedListNode(object):

    def __init__(self, val=None, nxt=None):
        self.val = val
        self.nxt = nxt

    def add(self, val):
        self.nxt = LinkedListNode(val)

        return self.nxt

ll = LinkedListNode(1)
next = ll.add(2)

for i in xrange(3, 6):
    next = next.add(i)

print ll.nxt.nxt.nxt.nxt.val
