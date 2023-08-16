def print_table(input_list):
    # Length of table_data (rows)
    num_of_lists = len(input_list)
    # Length of inner lists (columns)
    # Since each inner list is the same length, just find the length of the first list
    items_in_lists = len(input_list[0])

    # Find the longest word in each sublist
    max_length_list = []
    for list in input_list:
        max_length_item = 0
        for item in list:
            if len(item) > max_length_item:
                max_length_item = len(item)
        max_length_list.append(max_length_item)
    print(max_length_list)

    # Example needs 4 rows and 3 columns, swap row and column ranges
    for row in range(items_in_lists):
        for col in range(num_of_lists):
            # Constructs the row number first, continued by column number
            print(input_list[col][row].rjust(max_length_list[col]), end=' ')
        print('')


if __name__ == '__main__':
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']]
    print_table(table_data)
