class Conjecture(object):

    def __init__(self, number, thresh=10):
        self.number = abs(number)
        self.maths = 0
        self.thresh = thresh
        self.dictman = {}

    def calc(self, num):
        if num % 2 == 0:
            return num / 2
        else:
            return num * 3 + 1

    def calc2(self, start, end=0, buildalistman=False):
        """Electric Boogaloo"""

        # initial declarations for use in loops
        whereimat = 0
        endforsuperrealsies = 0
        dictman = {}
        localmaths = 0

        # end specification optional
        if not end:
            endforsuperrealsies = start
        else:
            endforsuperrealsies = end

        for i in xrange(start, endforsuperrealsies+1):
            localmaths = 0
            whereimat = i

            while whereimat is not 1:
                localmaths += 1

                if buildalistman:
                    dictman[whereimat] = localmaths

                whereimat = self.calc(whereimat)

        if buildalistman:
            return dictman
        else:
            return localmaths + 1

    def calc3(self):
        """Not as good as the original"""

        whereimat = 0
        localmaths = 0

        for i in xrange(1, self.number+1):
            localmaths = 0
            whereimat = i

            while whereimat is not 1:
                localmaths += 1

                if self.dictman.get(whereimat, None):
                    localmaths += self.dictman[whereimat]
                    break
                else:
                    whereimat = self.calc(whereimat)

            self.maths += localmaths + 1

    def conject(self):
        # intoruleall maintains the int position and how many maths it does
        inttoruleall = (0, 0)
        holdmetight = 0
        start = self.number - self.thresh
        end = self.number + self.thresh

        for i in xrange(start, end+1):
            holdmetight = self.calc2(i)

            if holdmetight > inttoruleall[1]:
                inttoruleall = (i, holdmetight)

        self.dictman = self.calc2(inttoruleall[0], buildalistman=True)

        self.calc3()

if __name__ == "__main__":
    print 'enter a number'
    difficulty = raw_input('> ')

    mathamajigz = Conjecture(int(difficulty))
    mathamajigz.conject()

    print 'maths:', mathamajigz.maths
