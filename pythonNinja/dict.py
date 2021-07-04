#simple dictionary example
def ninja_intro(dictionary):
    for key, value in dictionary.items():
        print(f'I am {key} and I am {value} belt')

dict = {}

while True:
    name = input('Enter name: ')
    color = input('Enter belt color: ')
    dict[name] = color
    another = input('add another? (y/n)')
    if another == 'y':
        continue
    else:
        break

ninja_intro(dict)
