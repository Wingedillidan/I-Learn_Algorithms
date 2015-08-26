class LinkedListNode(object):

    def __init__(self, val=None, nxt=None):
        self.val = val
        self.nxt = nxt

    def add(self, val):
        self.nxt = LinkedListNode(val)

        return self.nxt

i = raw_input('> ')
ll = LinkedListNode()
last = ll

for j in xrange(0, int(i)):
    last = last.add(j)

print ll.val
print ll.nxt.nxt.nxt.nxt.val
