def print_list(list):
    for i in range(len(list) - 1):
        print(f'{list[i]}, ', end='')
    print(f'and {list[i+1]}')


if __name__ == '__main__':
    spam = []
    while True:
        item = input('Please enter an item.\n')
        if item != '':
            spam.append(item)
        else:
            break

print_list(spam)
