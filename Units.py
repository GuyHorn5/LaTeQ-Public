# find the name of the units from the name of the var
def units_check(var):
    if var[0] == 'Δ':
        var = var[1]
    else:
        var = var[0]
    if var == 'V' or var == 'v':
        return 'V'
    elif var == 'I' or var == 'i':
        return 'A'
    elif var == 'P':
        return 'W'
    elif var == 'S':
        return 'VA'
    elif var == 'R' or var == 'r':
        return 'Ω'
    elif var == 'Z':
        return 'Ω'
    elif var == 'C':
        return 'F'
    elif var == 'L':
        return 'H'
    elif var == 'f' or var == 'F':
        return 'Hz'
    elif var == 'ω':
        return 'rad'
    elif var == 'g':
        return '℧'
    elif var == 't':
        return 'sec'

# find scale of the units
def units(char):
    if char == 'p':
        num = 10**-12
    elif char == 'n':
        num = 10**-9
    elif char == 'μ' or char == 'u':
        num = 10**-6
    elif char == 'm':
        num = 10**-3
    elif char == 'k':
        num = 10**3
    elif char == 'M':
        num = 10**6
    elif char == 'G':
        num = 10**9
    elif char == 'T':
        num = 10**12
    return num