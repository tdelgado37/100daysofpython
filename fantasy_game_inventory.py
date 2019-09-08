import pprint

inventory = { 'rope':1, 'torch': 6, 'gold coin': 42, 'dagger': 1}



def displayInventory(invtry):
    pprint.pprint(invtry)
    total_count = 0
    for key in invtry:
        total_count += invtry[key]
    pprint.pprint('Total inventory count: ' + str(total_count))


displayInventory(inventory)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(invtry, items):
    for item in items:
        invtry.setdefault(item, 0)
        invtry[item] +=1
    return invtry
inventory = addToInventory(inventory, dragonLoot)
displayInventory(inventory)
