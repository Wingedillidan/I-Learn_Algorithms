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
        return nxt

    def reverse(self, nxt=None):
        current = None

        if nxt is None:
            print "Level down! (a) val:", self.val
            current = self.reverse(self.nxt)
        elif nxt.nxt is None:
            self.val = nxt.val

            print "Level up! (a) Returning val:", nxt.val
            return self.nxt
        else:
            print "Level down! (b) val:", nxt.val, "passing:", nxt.nxt.val
            current = self.reverse(nxt.nxt)

        print "Level up! (b) Returning val:", nxt.val
        return current.add(nxt)


ll = LinkedListNode(1)
nxt = ll.add(2)

for i in xrange(3, 5):
    nxt = nxt.add(i)

ll.display()
ll = ll.reverse()
ll.display()
