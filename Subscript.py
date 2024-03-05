def subscript_val(num, sub):
    subindex = ''
    for i, val in enumerate(sub[1:]):
        if val == '}':
            break
        elif val == ' ':
            subindex += '_'
        else:
            subindex += val
    var = num + subindex
    length = i - 1
    return var, length
def subscript_sym(string):
    i = 0
    temp_str = ''
    while i<len(string):
        if string[i] == '{' and string[i-1] == '_':
            left = string[:i]
            i += 1
            while(string[i] != '}'):
                temp_str += string[i]
                i += 1
            count = temp_str.count(' ')
            temp_str = temp_str.replace(' ', '_{')
            temp_str = temp_str + count*'}'
            right = string[i+1:]
            string = left + '{' + temp_str + '}' + right
            temp_str = ''
        i += 1
    return string