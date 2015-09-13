class Conjecture(object):
    """Based on Collatz's Conjecture, an optimization challenge!"""

    def __init__(self, number):
        self.number = number
        self.lib = {}
        self.maths = 0

    def calc(self, number):
        """Performs the basic comparison/operations for
        the sequence."""

        if number % 2 == 0:
            return number / 2
        else:
            return number * 3 + 1

    def inner(self, number):
        """Runs through the operations for a given position in the
        sequence. If the operation results were already recorded in the lib
        for that position, than the given operations will be skipped. If not,
        that position will be saved as well as the current amount of ops, to
        be recorded at the end of the loop."""

        holdme = number
        maths = 1
        jump = 0
        needlib = []
        needlib_maths = []

        while holdme is not 1:
            # if we hit the lib, then we need to add the missing
            # operations (jump) to the newly recorded values at the end
            if self.lib.get(holdme, None):
                jump = self.lib[holdme] - 1
                maths += jump
                break
            else:
                needlib.append(holdme)

            maths += 1
            holdme = self.calc(holdme)
            needlib_maths.append(maths)

        # since maths is recorded end to start, or inversed in relation
        # to the order numbers are received, we write num to accommodate.
        for i in xrange(len(needlib)):
            num = len(needlib_maths) - i - 1

            self.lib[needlib[i]] = needlib_maths[num] + jump

        return maths

    def proc(self):
        for i in xrange(1, self.number+1):
            self.maths += self.inner(i)


if __name__ == "__main__":
    number = raw_input('input a number >')
    collatz = Conjecture(int(number))
    collatz.proc()
    # print collatz.lib
    print collatz.maths
