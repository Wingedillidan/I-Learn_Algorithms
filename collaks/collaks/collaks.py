class Conjecture(object):

    def __init__(self, number):
        self.number = number
        self.lib = {}
        self.maths = 0

    def calc(self, number):
        if number % 2 == 0:
            return number / 2
        else:
            return number * 3 + 1

    def inner(self, number):
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
        innermaths = 0

        for i in xrange(1, self.number+1):
            innermaths = self.inner(i)

            if not self.lib.get(i, None):
                self.lib[i] = innermaths

            self.maths += innermaths

if __name__ == "__main__":
    number = raw_input('input a number >')
    collaks = Conjecture(int(number))
    collaks.proc()
    # print collaks.lib
    print collaks.maths
