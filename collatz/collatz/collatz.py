library = {}


def conjecture(number):
    ops = 1
    holdnum = number

    while number is not 1:
        if library.get(number, None):
            ops += library.get(number) - 1
            break

        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1

        ops += 1

    library[holdnum] = ops

    return ops

if __name__ == "__main__":
    response = raw_input('enter a number > ')
    response = int(response)
    ops = 0

    for i in xrange(1, response+1):
        ops += conjecture(i)

    print ops

