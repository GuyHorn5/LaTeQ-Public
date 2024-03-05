# init
import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import pyperclip
from IPython.display import display, Markdown, Latex

import Abs, Add_Vals, Notation, Replace, Subscript, Units

def lateq(milon, var, eq, auto_units=True, units=None, eng=True, phasor=False, two_lines=False, declare=False, fin_ans=False, temp=0, out='Markdown', lie='', copy=False):

	# declare a var (no eq inputted, only declares the var and it's val)
	if declare:
		lateq(milon=milon, var=str(var), eq=str(milon[var]), copy=copy, auto_units=auto_units, units=units, eng=eng, phasor=phasor, two_lines=two_lines, fin_ans=fin_ans, temp=temp, out=out)
		return milon

	# print error if there is no eq
	if eq == '':
		print(f'U no put equation for {{{var}}}')
		return milon
	
	locals().update(milon)
	phasor_bool = phasor

	# temp calcs (answer not saved as var, for show only)
	if temp == 0: # regular calc, saves the answer in the var
		# lie about the actual answer
		if lie == '':
			milon[var] = eval(Replace.JIji(eq))
		else:
			milon[var] = eval(Replace.JIji(lie))
		var = Replace.greek_var(var)
		milon.update(Replace.greek_letters(milon))
		var_name = sp.latex(sp.sympify(var, evaluate=False, convert_xor=True), mul_symbol='dot', imaginary_unit='j', ln_notation=True)
	elif temp == 1: # only calcs, no var at all
		temp_val = eval(Replace.JIji(eq))
		var_name = ''
	elif temp == 2: # shows calc as equal to var, not putting the calc as the var
		temp_val = eval(Replace.JIji(eq))
		var_name = sp.latex(sp.sympify(var, evaluate=False, convert_xor=True), mul_symbol='dot', imaginary_unit='j', ln_notation=True)

	eq = eq.replace('np.', '').replace('sp.', '')
	
	# change var to scientific notation
	if temp == 0:
		ans = str(Notation.sci_not(milon[var], phasor=phasor_bool)).replace('*', '\\cdot')
	else:
		ans = str(Notation.sci_not(temp_val, phasor=phasor_bool)).replace('*', '\\cdot')

	# add units
	if auto_units:
		units = Units.units_check(Replace.JIji(var))
	if units:
		if units == '℧':
			units = 'mho'
		if units == '%':
			perc_ans = str(Notation.sci_not(milon[var]*100)).replace('*', '\\cdot')
		else:
			units = Replace.JIji(sp.latex(sp.sympify(units, evaluate=False, convert_xor=True), mul_symbol='dot', imaginary_unit='j', ln_notation=True))
			if eng:
				ans_eng, units_eng = Notation.eng_not(ans, units)

	# create the sym eq
	sym_eq = Replace.rep_sym_eq(sp.latex(sp.sympify(eq, evaluate=False, convert_xor=True), mul_symbol='dot', imaginary_unit='j', ln_notation=True))
	
	# put the vals in the sym eq
	val_eq = Replace.rep_val_eq(Add_Vals.add_vals_2_latex(milon, sym_eq, phasor_bool=phasor))

	# if there are syms in the eq
	if sym_eq != val_eq:
		final_eq = f'$${var_name} = {sym_eq} = {val_eq} = {ans}$$'
		if two_lines and not fin_ans and not units:
			final_eq = '\\begin{align*}' + f'{var_name} = {sym_eq} =\\\\= {val_eq} = {ans}' + '\\end{align*}'

	# if there are no syms in the eq
	if sym_eq == val_eq:
		final_eq = f'$${var_name} = {sym_eq} = {ans}$$'
		if sym_eq == ans:
			final_eq = f'$${var_name} = {ans}$$'

	if (val_eq == ans) and (sym_eq != val_eq):
		final_eq = f'$${var_name} = {sym_eq} = {ans}$$'

	# add units to the answer
	if units:
		if two_lines and not fin_ans and not (sym_eq == val_eq):
			final_eq = '\\begin{align*}' + f'{var_name} = {sym_eq}= {val_eq} = {ans}$$'
		if units == '%':
			final_eq = final_eq[:-2] + f'= {perc_ans} \\%$$'
		else:
			final_eq = final_eq[:-2] + f' \\left[{units}\\right]$$'
			if two_lines and final_eq[:2] == '$$': final_eq = final_eq.replace('$$', '\\begin{align*}', 1)
			if eng and (units != units_eng):
				final_eq = final_eq[:-2] + f' = {ans_eng} \\left[{units_eng}\\right]$$'
		if two_lines and not fin_ans:
			final_eq = final_eq[:-2] + '\\end{align*}'

	# mark the answer as the final answer
	if fin_ans:
		if two_lines and not (sym_eq == val_eq):
			final_eq = f'$${var_name} = {sym_eq} = {val_eq} = {ans}$$'
		final_eq = '\\begin{align*}' + final_eq[2:-2]
		if units == '%':
			final_eq += f'\\\\ ⇒ & \\boxed{{{var_name} = {perc_ans} \\%}}'
		elif (units and (not eng)) or (units and (units == units_eng)):
			final_eq += f'\\\\ ⇒ & \\boxed{{{var_name} = {ans} \\left[{units}\\right]}}'
		elif units and eng and (units != units_eng):
			final_eq += f'\\\\ ⇒ & \\boxed{{{var_name} = {ans_eng} \\left[{units_eng}\\right]}}'
		else:
			final_eq += f'\\\\ ⇒ & \\boxed{{{var_name} = {ans}}}'
		final_eq += '\\end{align*}'

	final_eq = Replace.rep_final_eq(final_eq)

	if two_lines or fin_ans: final_eq = final_eq.replace('=', '\\\\ & =').replace('\\\\ & =', '& =', 1)
	if fin_ans: final_eq = final_eq[::-1].replace('= & \\\\', '=', 1)[::-1]
	final_eq = final_eq.replace('\\ & =\\\\', '')
	if '\\' not in final_eq: final_eq = final_eq.replace(' &', '')

	# if temp calc remove the first '='
	if temp == 1 and not two_lines:
		final_eq = '$$' + final_eq[4:]
	if temp == 1 and two_lines:
		final_eq = final_eq.replace('\\begin{align*} & = ', '\\begin{align*} & ')

	# output the string
	if out == 'Markdown':
		display(Markdown(final_eq))
	elif out == 'String':
		print(final_eq)
	if copy:
		pyperclip.copy(final_eq[2:-2])
	return milon

''' 
	FIXME:
		fix for sym functions with eng_not?
		number with negative power
		matrices with complex numbers
		matrices in denominator
		matrices with sympy
'''