stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print('Inventory:')
    total_items = 0
    for k, v in inventory.items():
        print(f'{str(v)} {k}')
        total_items += v
    print(f'Total number of items: {str(total_items)}')

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

if __name__ == '__main__':
    inventory = {'gold coin': 42, 'rope': 1}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inventory = add_to_inventory(inventory, dragon_loot)
    display_inventory(inventory)
