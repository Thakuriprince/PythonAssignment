def remove_char(str, n):
    first= str[:n]
    last= str[n+1:]
    return first + last

print(remove_char('python', 1))
print(remove_char('python', 4))