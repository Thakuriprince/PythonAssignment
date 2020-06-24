def add_string(str):
    l = len(str)

    if l >2:
        if str[-3:] == 'ing':
            str += 'ly'
        else:
            str += 'ing'

    return str

print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))