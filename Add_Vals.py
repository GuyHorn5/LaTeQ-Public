import Notation, Subscript, Replace

def add_vals_2_latex(milon, str, phasor_bool=False):
	locals().update(milon)
	pow_bool = False
	old_str = str
	new_str = ""
	brackets = ["{", "(", ")", " ", "|"]
	operators = ["+", "-", "/", "*", "⋅"]
	greek = ['α', 'β', 'γ', 'Γ', 'δ', 'Δ', 'ε', 'η', 'θ', 'λ', 'Λ', 'μ', 'ξ', 'ρ', 'σ', 'τ', 'ϕ', 'φ', 'χ', 'ψ', 'ω', 'Ω']
	milon.update(Replace.greek_letters(milon))
	
	old_str = Replace.rem_before_add_vals(old_str)

	i = 0
	while(i+1 <= len(old_str)):
		val = old_str[i]
		if val.isalpha() or val=="_":
			temp_var = ""

			while(i+1 <= len(old_str) and (val.isalnum() or val=='_' or (val in greek) or (val == '{' and (old_str[i-1] == '_')))):
				if val == '{' and old_str[i-1] == '_':
					temp_var, length = Subscript.subscript_val(temp_var, old_str[i+1:])
					i = i + length + 2
					break
				if val != "{":
					temp_var += val
				if i+1 < len(old_str):
					val = old_str[i+1]
				i += 1

			temp_var = temp_var.replace("{", "").replace("}", "")

			if i+1 <= len(old_str):
				if old_str[i] == '^':
					pow_bool = True
			temp_var = Notation.sci_not(milon[temp_var], pow=pow_bool, phasor = phasor_bool)
			pow_bool = False
			new_str += f'\\left( {temp_var} \\right)'

		if val=="\\" and old_str[i+1] == "\\":
			while(i+1 <= len(old_str) and val not in brackets and val not in operators):
				new_str += val
				if i+1 < len(old_str):
					val = old_str[i+1]
				i += 1
			continue
		elif not val.isalpha():
			new_str += val
		i += 1

	new_str = Replace.rem_after_add_vals(new_str)
	
	return new_str