class Conjecture(object):

    def __init__(self, number):
        self.number = abs(number)
        self.maths = 0
        self.whereivebeen = {}

    def conject(self):
        whereimat = 0

        for i in xrange(1, self.number+1):
            whereimat = i
            localmaths = 0

            while whereimat is not 1:
                if self.whereivebeen.get(whereimat, None):
                    self.maths += self.whereivebeen[whereimat]
                    break
                else:
                    localmaths += 1

                whereimat = self.calc(whereimat)

            self.whereivebeen[i] = localmaths
            self.maths += localmaths + 1

    def calc(self, num):
        if num % 2 == 0:
            return num / 2
        else:
            return num * 3 + 1


print 'enter a number'
difficulty = raw_input('> ')

mathamajigz = Conjecture(int(difficulty))
mathamajigz.conject()

print mathamajigz.whereivebeen
print 'maths:', mathamajigz.maths
