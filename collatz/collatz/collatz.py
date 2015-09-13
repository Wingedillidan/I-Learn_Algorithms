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
        for that position, than the given operations will be skipped."""

        holdme = number
        maths = 1

        while holdme is not 1:
            if self.lib.get(holdme, None):
                maths += self.lib[holdme] - 1
                break

            maths += 1
            holdme = self.calc(holdme)

        return maths

    def proc(self):
        """Loops through every number between 1 and the attribute supplied
        and records how many times calc was called, the operation results
        will be saved for each number."""
        # TODO: An operational pattern can arise for a number greater than
        # the current position, thus adding a bit of redundancy which stacks
        # up as the supplied attribute gets larger

        innermaths = 0

        for i in xrange(1, self.number+1):
            innermaths = self.inner(i)

            if not self.lib.get(i, None):
                self.lib[i] = innermaths

            self.maths += innermaths


if __name__ == "__main__":
    number = raw_input('input a number >')
    collatz = Conjecture(int(number))
    collatz.proc()
    # print collatz.lib
    print collatz.maths
