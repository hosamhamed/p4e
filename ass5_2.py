biggest = -9223372036854775807
smallest = 9223372036854775807
while True:
    n = -1
    num = input('Enter a number: ')
    if num == 'done':
        break
    else:
        try:
            n = int(num)
            if n < smallest:
                smallest = n
            if n > biggest:
                biggest = n
        except:
            print('Invalid input')

print('Maximum is', biggest)

print('Minimum is', smallest)
