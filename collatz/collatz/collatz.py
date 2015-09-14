def conjecture(number):
    current = number
    ops = 1

    while current is not 1:
        if current % 2 == 0:
            current = current / 2
        else:
            current = current * 3 + 1

        ops += 1

    return ops

if __name__ == "__main__":
    response = raw_input('enter a number > ')
    print conjecture(int(response))
