def print_picnic(dict_items, left_width, right_width):
    print('PICNIC ITEMS'.center(left_width + right_width, '-'))
    for k, v in dict_items.items():
        print(str(k).ljust(left_width, '.') + str(v).rjust(right_width))

picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
print_picnic(picnic_items, 12, 4)
