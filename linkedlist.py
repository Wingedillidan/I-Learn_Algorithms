class LinkedListNode(object):

    def __init__(self, val=None, nxt=None):
        self.val = val
        self.nxt = nxt
        self.hold = None

    def add(self, val):
        self.nxt = LinkedListNode(val)

        return self.nxt

    def _displaynode(self):
        print self.val
        return self.nxt

    def display(self):
        nxt = self._displaynode()

        while nxt is not None:
            nxt = nxt._displaynode()

    def setnxt(self, nxt):
        self.nxt = nxt

        return self.nxt

    def reverse(self, nxt=None):
        current = None

        if nxt is None:
            current = self.reverse(self.nxt)
        elif nxt.nxt is None:
            self.hold = self.val
            self.val = nxt.val
            self.nxt = None

            return self
        else:
            current = self.reverse(nxt.nxt)

        if nxt is not None:
            return current.setnxt(nxt)
        else:
            return current.add(self.hold)


ll = LinkedListNode(1)
nxt = ll.add(2)

for i in xrange(3, 101):
    nxt = nxt.add(i)

ll.display()
ll.reverse()
ll.display()
