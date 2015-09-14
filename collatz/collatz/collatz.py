library = {}


def conjecture(number):
    ops = 1
    unrec_ops = []
    unrec_nums = []

    while number is not 1:
        if library.get(number, None):
            ops += library.get(number) - 1
            break
        else:
            unrec_ops.append(ops)
            unrec_nums.append(number)

        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1

        ops += 1

    for i in xrange(0, len(unrec_nums)):
        rev_i = len(unrec_nums) - i - 1
        library[unrec_nums[i]] = unrec_ops[rev_i]

    return ops

if __name__ == "__main__":
    response = raw_input('enter a number > ')
    response = int(response)

    thresh = int(response * 0.05)

    for i in xrange(response-thresh, response):
        conjecture(i)

    print library
    ops = 0

    for i in xrange(1, response):
        ops += conjecture(i)

    print ops

