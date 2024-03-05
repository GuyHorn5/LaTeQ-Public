import numpy as np

import Abs, Notation, Subscript, Replace

# replace english greek to greek chars
def rep_sym(str):
	str = str.replace('\\Rightarrow ', '⇒')
	str = str.replace('\\Rightarrow', '⇒')
	str = str.replace('\\alpha ', 'α')
	str = str.replace('\\alpha', 'α')
	str = str.replace('\\beta ', 'β')
	str = str.replace('\\beta', 'β')
	str = str.replace('\\gamma ', 'γ')
	str = str.replace('\\gamma', 'γ')
	str = str.replace('\\Gamma ', 'Γ')
	str = str.replace('\\Gamma', 'Γ')
	str = str.replace('\\delta ', 'δ')
	str = str.replace('\\delta', 'δ')
	str = str.replace('\\Delta ', 'Δ')
	str = str.replace('\\Delta', 'Δ')
	str = str.replace('\\varepsilon ', 'ε')
	str = str.replace('\\varepsilon', 'ε')
	str = str.replace('\\eta ', 'η')
	str = str.replace('\\eta', 'η')
	str = str.replace('\\theta ', 'θ')
	str = str.replace('\\theta', 'θ')
	str = str.replace('\\lambda ', 'λ')
	str = str.replace('\\lambda', 'λ')
	str = str.replace('\\Lambda ', 'Λ')
	str = str.replace('\\Lambda', 'Λ')
	str = str.replace('\\mu ', 'μ')
	str = str.replace('\\mu', 'μ')
	str = str.replace('\\xi ', 'ξ')
	str = str.replace('\\xi', 'ξ')
	str = str.replace('\\rho ', 'ρ')
	str = str.replace('\\rho', 'ρ')
	str = str.replace('\\sigma ', 'σ')
	str = str.replace('\\sigma', 'σ')
	str = str.replace('\\tau ', 'τ')
	str = str.replace('\\tau', 'τ')
	str = str.replace('\\phi ', 'ϕ')
	str = str.replace('\\phi', 'ϕ')
	str = str.replace('\\varphi ', 'φ')
	str = str.replace('\\varphi', 'φ')
	str = str.replace('\\chi ', 'χ')
	str = str.replace('\\chi', 'χ')
	str = str.replace('\\psi ', 'ψ')
	str = str.replace('\\psi', 'ψ')
	str = str.replace('\\omega ', 'ω')
	str = str.replace('\\omega', 'ω')
	str = str.replace('\\Omega ', 'Ω')
	str = str.replace('\\Omega', 'Ω')
	return str

# replace greek name var to greek char
def greek_var(str):
	str = str.replace('alpha', 'α')
	str = str.replace('beta', 'β')
	str = str.replace('gamma', 'γ')
	str = str.replace('Gamma', 'Γ')
	str = str.replace('delta', 'δ')
	str = str.replace('Delta', 'Δ')
	str = str.replace('varepsilon', 'ε')
	str = str.replace('eta', 'η')
	str = str.replace('theta', 'θ')
	str = str.replace('lambda', 'λ')
	str = str.replace('Lambda', 'Λ')
	str = str.replace('mu', 'μ')
	str = str.replace('xi', 'ξ')
	str = str.replace('rho', 'ρ')
	str = str.replace('sigma', 'σ')
	str = str.replace('tau', 'τ')
	str = str.replace('phi', 'ϕ')
	str = str.replace('varphi', 'φ')
	str = str.replace('chi', 'χ')
	str = str.replace('psi', 'ψ')
	str = str.replace('omega', 'ω')
	str = str.replace('Omega', 'Ω')
	return str

# replace single letter chars
def JIji(string):
	string = string.replace('JJ', 'J')
	string = string.replace('II', 'I')
	string = string.replace('jj', 'j')
	string = string.replace('ii', 'i')
	string = string.replace('EEE', 'E')
	string = string.replace('QQQ', 'Q')
	string = string.replace('NN', 'N')
	string = string.replace('OOO', 'O')
	string = string.replace('SSS', 'S')
	string = string.replace('ssec', 'sec')
	string = string.replace('rrad', 'rad')
	return string

# replace phi <=> varphi
def replace_phi(string):
	new_str = ''
	for char in string:
		if char == 'φ':
			char = 'ϕ'
		elif char == 'ϕ':
			char = 'φ'
		new_str += char
	return new_str

# add greek letters vars to vals
def greek_letters(milon):
	greek = ['α', 'β', 'γ', 'Γ', 'δ', 'Δ', 'ε', 'η', 'θ', 'λ', 'Λ', 'μ', 'ξ', 'ρ', 'σ', 'τ', 'ϕ', 'φ', 'χ', 'ψ', 'ω', 'Ω']
	engreek = ['alpha', 'beta', 'gamma', 'Gamma', 'delta', 'Delta', 'epsilon', 'eta', 'theta', 'lambda', 'Lambda', 'mu', 'xi', 'rho', 'sigma', 'tau', 'Phi', 'phi', 'chi', 'psi', 'omega', 'Omega']
	for index, letter in enumerate(engreek):
		if letter in milon:
			milon[greek[index]] = milon[letter]
	return milon

# remove '1 \cdot'
def rem_1_cdot(string):
	string = string.replace('= 1 \\cdot \\frac', '= \\frac')
	string = string.replace('+ 1 \\cdot \\frac', '+ \\frac')
	string = string.replace('- 1 \\cdot \\frac', '- \\frac')
	string = string.replace('(1 \\cdot \\frac', '(\\frac')
	string = string.replace(' \\cdot 1 \\cdot', ' \\cdot')
	string = string.replace('{1 \\cdot \\frac', '{\\frac')
	return string

def rem_before_add_vals(string):
	old_str = string
	old_str = old_str.replace('np.', '')
	old_str = old_str.replace('sp.', '')
	old_str = Replace.rep_sym(old_str)
	old_str = old_str.replace("\\", "\\\\")
	old_str = old_str.replace("{", "{{")
	old_str = old_str.replace("}", "}}")
	return old_str

def rem_after_add_vals(string):
	string = string.replace("\\\\", "\\")
	string = string.replace("{{{{{{", "{")
	string = string.replace("{{", "{")
	string = string.replace("}}", "}")
	string = string.replace("*", "\\cdot")
	return string

def rep_sym_eq(string):
	string = JIji(string)
	string = string.replace('abs', '\\abs')
	string = string.replace('real', '\\real')
	string = string.replace('imag', '\\imag')
	return string

def rep_val_eq(string):
	string = string.replace(r'{\left\{', r'{')
	string = string.replace(r'\right\}}', r'}')
	string = string.replace('\\pi', Notation.sci_not(np.pi))
	return string

def rep_final_eq(string):
	string = Subscript.subscript_sym(string)
	string = Abs.abs_val(string)
	string = Replace.replace_phi(string)
	string = Replace.rem_1_cdot(string)
	string = string.replace('{}', '')
	string = string.replace('+ -', '-')
	string = string.replace('- -', '+')
	string = string.replace('\\left(0\\right)', '')
	# string = string.replace('\\left(\\left(', '\\left(')
	# string = string.replace('\\left( \\left(', '\\left(')
	# string = string.replace('\\right)\\right)', '\\right)')
	# string = string.replace('\\right) \\right)', '\\right)')
	return string