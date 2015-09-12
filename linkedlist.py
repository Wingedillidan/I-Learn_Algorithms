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


def reverse(linkedlist):
    theguybefore = linkedlist
    nextinline = linkedlist.nxt
    savemyspot = None

    while True:
        if nextinline is not None:
            savemyspot = nextinline.nxt
            nextinline.nxt = theguybefore
            theguybefore = nextinline

        if savemyspot is None:
            linkedlist.nxt = None
            return nextinline
        else:
            nextinline = savemyspot


ll = LinkedListNode(1)
nxt = ll.add(2)

for i in xrange(3, 101):
    nxt = nxt.add(i)

ll.display()
ll = reverse(ll)
ll.display()
