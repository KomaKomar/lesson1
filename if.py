a=''
c = abs(int(input()))
if 7 < c <= 14:
    a = 'школьник'
elif 0 < c <= 7:
    a = 'сопляк'
elif 14 < c <= 18:
    a = 'пту'
elif 18 < c <= 25:
    a = 'студота'
else:
    a = 'старпер'

print(a)
