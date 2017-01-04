def reverse_digits(num):
    reverse_list = []

    still_have_digits = True

    while still_have_digits:
        digit = num % 10
        if num <= 0:
            still_have_digits = False
        else:
            reverse_list.append(digit)
            num = num/10

    for digit in reverse_list:
        print digit

if __name__ == '__main__':
    num = int(raw_input("Give me a number, and I'll reverse it for you!"))
    reverse_digits(num)

