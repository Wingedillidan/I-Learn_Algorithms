class LinkedListNode(object):

    def __init__(self, val=None, nxt=None):
        self.val = val
        self.nxt = nxt

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

    def gonxt(self, nxt):
        return nxt.nxt

    def reverse(self):
        stopval = None
        holdval = None
        currentnode = self

        while True:
            nxt = currentnode.nxt

            if stopval is None:
                while nxt.nxt is not None:
                    nxt = nxt.gonxt(nxt)
            else:
                while nxt.nxt.val is not stopval:
                    # print "compared:", nxt.nxt.val, "to stopval:", stopval
                    nxt = self.gonxt(nxt)

            holdval = currentnode.val
            currentnode.val = nxt.val
            stopval = holdval
            nxt.val = holdval

            if currentnode.nxt is None:
                break
            else:
                currentnode = currentnode.nxt

            self.display()


ll = LinkedListNode(1)
nxt = ll.add(2)

for i in xrange(3, 5):
    nxt = nxt.add(i)

# ll.display()
ll = ll.reverse()
ll.display()
