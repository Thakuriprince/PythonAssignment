def string_length(str):
    if len(str)<2:
        return'Empty String'
    else:
        return str[0:2] + str[-2:]

print(string_length('Python'))
print(string_length('Py'))
print(string_length('w'))