cat_names = []

while True:
    name = input(f'Enter the name of cat {str(len(cat_names) + 1)} or enter nothing to stop:\n')
    if name == '':
        break
    # List concatenation
    cat_names = cat_names + [name]
print('The cat names are:')
for name in cat_names:
    print(' ' + name)


