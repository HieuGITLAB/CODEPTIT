t = int(input())

def phanloai(d):
    if d >= 3 and d <= 4:
        d = 2.5
    elif d >= 5 and d <= 6:
        d = 3.0
    elif d >= 7 and d <= 9:
        d = 3.5
    elif d >= 10 and d <= 12:
        d = 4.0
    elif d >= 13  and d <= 15:
        d = 4.5
    elif d >= 16 and d <= 19:
        d = 5.0
    elif d >= 20 and d <= 22:
        d = 5.5
    elif d >= 23 and d <= 26:
        d = 6.0
    elif d >= 27 and d <= 29:
        d = 6.5
    elif d >= 30 and d <= 32:
        d = 7.0
    elif d >= 33 and d <= 34:
        d = 7.5
    elif d >= 35 and d <= 36:
        d = 8.0
    elif d >= 37 and d <= 38:
        d = 8.5
    else:
        d = 9.0
    return d
while t > 0:
    a = [float(i) for i in input().split()]
    d1 = phanloai(a[0])
    d2 = phanloai(a[1])
    d3 = a[2]
    d4 = a[3]
    tb = (d1 + d2 + d3 + d4) / 4
    tb1 = tb - int(tb)
    if tb1 >= 0.25 and tb1 < 0.75:
        tb1 = 0.5
    elif tb1 >= 0.75:
        tb1 = 1.0
    else:
        tb1 = 0.0
    tb = int(tb) +  tb1
    print('%.1f'%tb)

    t -= 1