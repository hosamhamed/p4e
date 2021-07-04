def computepay(hrs, rate):
    pay = 0
    if hrs <= 40:
        pay = hrs * rate
    else:
        pay = 40 * rate
        pay += (hrs - 40) * (rate * 1.5)
    return pay
hrs = float(input('Enter hours: '))
rate = float(input('Enter rate: '))
print('Pay', computepay(hrs, rate))
