def swap_str(a,b):
    i = b[:2]+a[2:]
    j = a[:2]+b[2:]
    return i + ' ' + j

print(swap_str('abc','xyz'))
