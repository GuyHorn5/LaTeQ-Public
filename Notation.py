import numpy as np
import sympy as sp

# scientific notation
def sci_not(num, decimal_digits=3, pow=False, phasor=False, precision=None, exponent=None):
    if isinstance(num, np.ndarray) or isinstance(num, np.matrix) or isinstance(num, sp.Matrix):
        return mat_not(num)
    if not phasor:
        was_int = None
        if num == 0:
            return '0'
        if isinstance(num, sp.Expr):
            num = sp.latex(sp.sympify(num, evaluate=False, convert_xor=True), mul_symbol='dot', imaginary_unit='j', ln_notation=True)
            temp_num = ''
            new_str = ''
            for char in num:
                if char.isdigit():
                    temp_num += char
                if not char.isdigit() and temp_num != '':
                    if (float(temp_num) < 1000 and float(temp_num) >= 0.01) or (float(temp_num) > -1000 and float(temp_num) <= -0.01):
                        char = sci_not(float(temp_num))
                    else:
                        char = '\\left(' + sci_not(float(temp_num)) + '\\right)'
                    temp_num = ''
                if temp_num == '':
                    new_str += char
            if temp_num != '':
                char = sci_not(float(temp_num))
                new_str += char
            return new_str
        if np.iscomplex(num):
            return com_not(num)
        if float(np.imag(num)) == 0:
            num = float(np.real(num))
        if isinstance(num, np.int32):
            num = float(num)
        if (isinstance(num, int) or num.is_integer()):
            was_int = True
        num = float(num)
        if (num < 1000 and num >= 0.01) or (num > -1000 and num <= -0.01):
            num = '{:.4}'.format(num)
            if was_int == True:
                num = num.replace(".0", "")
            return num
        if exponent is None:
            exponent = int(np.floor(np.log10(abs(num))))
        coeff = round(num / float(10**exponent), decimal_digits)
        if precision is None:
            precision = decimal_digits
        if coeff.is_integer():
            coeff = int(coeff)
        if coeff == 10:
            coeff = 1
            exponent += 1
        num = f'{coeff}*10^{{{exponent}}}'
        if coeff == 1:
            num = f'10^{{{exponent}}}'
    else:
        # num = f'\\left({com_2_phas(num)[0]}∢{{{com_2_phas(num)[1]}}}°\\right)'
        num = f'{com_2_phas(num)[0]}∢{{{com_2_phas(num)[1]}}}°'
    if pow and not phasor:
        num = '\\left(' + num + '\\right)'
    return num

# matrix notation
def mat_not(mat):
    new_mat = '\\begin{pmatrix} '
    mat = mat.tolist()
    for row, row_val in enumerate(mat):
        for col, col_val in enumerate(row_val):
            new_mat = new_mat + sci_not(col_val) + ' & '
        new_mat = new_mat[:-3] + ' \\\\\\\\ '
    new_mat = new_mat[:-6] + ' \\end{pmatrix}'
    return new_mat
def com_not(num):
    real = float(np.real(num))
    imag = float(np.imag(num))
    comps = [real, imag]
    comp_num = []
    for comp in comps:
        comp_num.append(sci_not(comp))
    if comp_num[0] == '0':
        return f'{comp_num[1]}j'
    if comp_num[1][0] == '-':
        return f'\\left({comp_num[0]}{comp_num[1]}j\\right)'
    else:
        return f'\\left({comp_num[0]}+{comp_num[1]}j\\right)'

# complex to phasor
def com_2_phas(num):
    real = sci_not(np.sqrt(np.real(num)**2+np.imag(num)**2))
    imag = sci_not(np.angle(num)*180/np.pi)
    phasor = [real, imag]
    return phasor

# engineering notation
def eng_not(num, units=None):
    if units == None:
        return num, units
    deg = None
    pico = [-13,-12,-11]
    nano = [-10,-9,-8]
    micro = [-7,-6,-5]
    milli = [-4,-3,-2]
    kilo = [2,3,4]
    mega = [5,6,7]
    giga = [8,9,10]
    tera = [11,12,13]
    mat = [pico, nano, micro, milli, kilo, mega, giga, tera]
    for i,char in enumerate(num):
        if char=='{':
            deg = int(num[i+1:-1])
            coeff = float(num[:i-8])
            if coeff.is_integer():
                coeff = int(coeff)
            if deg in pico:
                units = 'p' + units
                div = -12
            elif deg in nano:
                units = 'n' + units
                div = -9
            elif deg in micro:
                units = 'μ' + units
                div = -6
            elif deg in milli:
                units = 'm' + units
                div = -3
            elif deg in kilo:
                units = 'k' + units
                div = 3
            elif deg in mega:
                units = 'M' + units
                div = 6
            elif deg in giga:
                units = 'G' + units
                div = 9
            elif deg in tera:
                units = 'T' + units
                div = 12
            else:
                return num, units
            break
    if not deg:
        return num, units
    for i in range(3):
        for j in mat:
            if j[i] == deg:
                mul = i
                break
    if mul == 0:
        mul = 0.1
    elif mul == 1:
        mul = 1
    elif mul == 2:
        mul = 10
    else:
        return num, units
    if coeff != 10:
        num = coeff*mul
    else:
        num = mul
    count = 0
    if isinstance(num, float):
        if num.is_integer():
            num = int(num)
        else:
            num = str(num)[:10]
            for char in reversed(num):
                if char == '0':
                    count += 1
            num = num[:11-count]
    return num, units