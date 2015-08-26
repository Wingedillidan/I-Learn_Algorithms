"""
Receive a number on stdin. For every number from 1 to the number received
(inclusive), print "fizz" if the number is divisible by 3, "buzz" if it's
divisible by 5, "fizzbuzz" if it's divisible by both, or the number if it's
not divisible by either.
"""

i = raw_input('> ')


for j in xrange(1, i):
    result = ""

    if i % 3 == 0:
        result += "fizz"
    if i % 5 == 0:
        result += "buzz"

    if result == "":
        print i
    else:
        print result
