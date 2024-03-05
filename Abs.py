def abs_val(string):
    string = string.replace('\\operatorname{abs}{\\left(', '\\operatorname{\\abs}{\\left(')
    if '\\operatorname{\\abs}{\\left(' in string:
        string = string.replace('\\operatorname{\\abs}{\\left(', '\\left|')
        for i, val in enumerate(string):
            if string[i-6:i] == '\\left|':
                left = string[:i]
                right = string[i:].replace(' \\right)}', '\\right|', 1)
                string = left + right
    if '\\operatorname{\\abs}{\\left(' in string:
        abs_val(string)
    return string