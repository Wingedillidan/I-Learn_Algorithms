class LinkedListNode(object):

    def __init__(self, val=None, nxt=None):
        self.val = val
        self.nxt = nxt

    def add(self, val):
        self.nxt = LinkedListNode(val)

        return self.nxt

    def _ds(self):
        print self.val
        return self.nxt

    def display(self):
        nxt = self._ds()

        while True:
            if nxt is None:
                break
            nxt = nxt._ds()

ll = LinkedListNode(1)
nxt = ll.add(2)

for i in xrange(3, 6):
    nxt = nxt.add(i)

ll.display()
