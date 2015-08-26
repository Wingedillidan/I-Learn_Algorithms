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

    def reverse(self):
        result = None
        ondeck = None

        while self.nxt is not None:
            nxt = self._displaynode()

            if nxt.nxt is not None:
                while nxt.nxt.nxt is not None:
                    nxt = nxt._displaynode()
            else:
                break

            if result is None:
                result = LinkedListNode(nxt.nxt.val)
                ondeck = result
            else:
                ondeck = ondeck.setnxt(nxt.nxt)

            nxt.nxt = None

        ondeck = ondeck.setnxt(self.nxt)
        ondeck = ondeck.setnxt(LinkedListNode(self.val))

        return result


ll = LinkedListNode(1)
nxt = ll.add(2)

for i in xrange(3, 6):
    nxt = nxt.add(i)

ll.display()
ll = ll.reverse()
ll.display()
