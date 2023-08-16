def collatz(number):
    # Even number
    if number % 2 == 0:
        result = number // 2
        return result
    # Odd number
    elif number % 2 == 1:
        result = 3 * number + 1
        return result

"""
Alternative way:
def collatz(number):
    return number // 2 if number % 2 == 0 else number % 2 == 1
"""

if __name__ == '__main__':
    number = int(input('Enter number:\n'))
    try:
        while True:
            if number != 1:
                number = collatz(number)
                print(number)
            else:
                break
    except ValueError:
        print('Please enter an integer.')
