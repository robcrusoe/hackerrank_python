""" Python If-Else """
n = int(input())
o = ''
if n % 2 != 0:
    o += 'Weird'
else:
    if n >= 6 and n <= 20:
        o += 'Weird'
    else:
        o += 'Not Weird'

print(o)