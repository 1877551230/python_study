def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 1:
        print('error')
        return -1

    while (n-2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1

    return n3

result = fab(20)
if result != -1:
    print('总共有%d对小兔子诞生' % result)

---------------------------------------------------------------------

def fab(n):
    if n < 1:
        print('error')
        return -1

    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)

result = fab(20)
if result != -1:
    print('共有%d对小兔子诞生' % result)
