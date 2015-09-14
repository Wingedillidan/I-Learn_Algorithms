class Conjecture(object):

    def __init__(self, number):
        self.number = abs(number)
        self.maths = 0

    def calc(self, num):
        if num % 2 == 0:
            return num / 2
        else:
            return num * 3 + 1

    def conject(self):
        whereimat = 0

        for i in xrange(1, self.number+1):
            whereimat = i

            while whereimat is not 1:
                self.maths += 1
                whereimat = self.calc(whereimat)

            self.maths += 1


if __name__ == "__main__":
    print 'enter a number'
    difficulty = raw_input('> ')

    mathamajigz = Conjecture(int(difficulty))
    mathamajigz.conject()

    print 'maths:', mathamajigz.maths
