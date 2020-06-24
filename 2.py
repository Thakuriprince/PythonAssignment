def string(str):
    if len(str)<2:
        return'Empty String'
    else:
        return str[0:2] + str[-2:]

print(string('Python'))
print(string('Py'))
print(string('w'))