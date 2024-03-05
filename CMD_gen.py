import tkinter as tk
from tkinter import ttk

def copy_to_clipboard():
	# Implement the functionality to copy to clipboard here
	# For example, you can use the 'pyperclip' module:
	import pyperclip

	# Access the variables and use them as needed
	variable_value = entries["Variable"].get()
	equation_value = entries["Equation"].get()
	manual_units_value = entries["Manual Units"].get()
	lie_value = entries["Lie"].get()

	auto_units_value = checkbox_vars[0].get()
	engineering_units_value = checkbox_vars[1].get()
	phasor_value = checkbox_vars[2].get()
	two_lines_value = checkbox_vars[3].get()
	declaration_value = checkbox_vars[4].get()
	final_answer_value = checkbox_vars[5].get()
	copy_value = checkbox_vars[6].get()

	format_value = format_var.get()  
	temp_calc_value = temp_calc_var.get()

	if manual_units_value == '': manual_units_value = 'None'

	data = f"locals().update(LaTeQ.lateq(milon=locals(), var=f'{variable_value}', eq=f'{equation_value}', auto_units={auto_units_value}, units={manual_units_value}, eng={engineering_units_value}, phasor={phasor_value}, two_lines={two_lines_value}, declare={declaration_value}, fin_ans={final_answer_value}, temp={temp_calc_value}, out='{format_value}', lie='{lie_value}', copy={copy_value}))"

	# Copy the data to the clipboard
	pyperclip.copy(data)

def save_and_close():
	copy_to_clipboard()
	root.destroy()

root = tk.Tk()
root.title("Input Form")
root.configure(bg='#1E1E1E')

# Create labels and entry fields with custom colors
labels = ["Variable", "Equation", "Temp Calc", "Manual Units", "Lie"]
entries = {label: tk.Entry(root, bg='#2E2E2E', fg='#FFFFFF') for label in labels}

for label, entry in entries.items():
	entry_label = tk.Label(root, text=label, bg='#1E1E1E', fg='#FFFFFF')
	entry_label.pack()
	entry.pack(pady=5, padx=10)

# Create checkboxes with custom colors using ttk
checkbox_labels = ["Auto Units", "Engineering Units", "Phasor", "Two Lines", "Declaration", "Final Answer", "Copy"]
checkbox_defaults = [True, True, False, True, False, False, False]

checkbox_vars = [tk.BooleanVar(value=value) for value in checkbox_defaults]
checkboxes = {label: ttk.Checkbutton(root, text=label, variable=var, style='TCheckbutton') for label, var in zip(checkbox_labels, checkbox_vars)}

for label, checkbox in checkboxes.items():
	checkbox.pack(anchor='w', padx=10)
	checkbox.var = checkbox.cget("variable")  # Store variable reference

	checkbox.style = ttk.Style()
	checkbox.style.configure('TCheckbutton', background='#1E1E1E', font=('Helvetica', 12), foreground='#FFFFFF')
	checkbox.style.map('TCheckbutton', background=[('active', '#333333')])

# Create Format menu with custom colors
format_label = tk.Label(root, text="Format", bg='#1E1E1E', fg='#FFFFFF')
format_label.pack()

format_options = ["String", "Markdown"]
format_var = tk.StringVar(value="Markdown")

format_menu = tk.OptionMenu(root, format_var, *format_options)
format_menu.config(bg='#2E2E2E', fg='#FFFFFF')
format_menu.pack(pady=5, padx=10)

# Create Temp Calc menu with 3 options: 0, 1, 2
temp_calc_label = tk.Label(root, text="Temp Calc", bg='#1E1E1E', fg='#FFFFFF')
temp_calc_label.pack()

temp_calc_var = tk.StringVar(value="0")
temp_calc_menu = tk.OptionMenu(root, temp_calc_var, "0", "1", "2")
temp_calc_menu.config(bg='#2E2E2E', fg='#FFFFFF')
temp_calc_menu.pack(pady=5, padx=10)

# Create Save Button with custom colors
button = tk.Button(root, text="Save to Clipboard", command=save_and_close, bg='#2E2E2E', fg='#FFFFFF')
button.pack(pady=10, padx=10)

root.mainloop()