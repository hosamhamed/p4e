def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')

ninja_dict = {}

while True:
    name = input('Enter ninja name: ')
    belt = input('Enter belt color: ')
    ninja_dict[name] = belt
    another = input('add another? (y/n)')
    if another == 'n':
        break
    else:
        continue

belt_count(ninja_dict)
