def conjecture(number):
    ops = 1

    while number is not 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1

        ops += 1

    return ops

if __name__ == "__main__":
    response = raw_input('enter a number > ')
    print conjecture(int(response))
