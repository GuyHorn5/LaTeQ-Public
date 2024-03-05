# LaTeQ
 LaTeX equations generator for Jupyter Notebooks

---

## Important Notes

__For examples of use view the `Tests.ipynb` file__
__For ease of use, run the `CMD_gen.py` file, that will open a GUI window helping in the generation of the command, outputting it to the clipboard__

___

## How to Use

1. Download the repo.
1. Open a new Jupyter Notebook file and import the repo.
	> an example of how to import the repo exists in the `Tests.ipynb` file, however you will need to either have the current file in the same dir, or import the repo from the different dir of which the file currently is in.
1. Run the `CMD_gen.py` file in a different window.
1. Enter the relevant inputs:
	- `var`: the output of the equation {string}.
	- `eq`: the actual equation {string}.
		> if there are variables in the equation, you should put them __as a string__ inside the eq string.
		> meaning: `eq=f'A+B'`.
		> for more info open the `Tests.ipynb` file.
	- `copy`: should the equation be copied to the clipboard {True/False}.
	- `auto_units`: should the script automatically add scientific units to the final answer {True/False}.
		> for example, if the `var` is $V_0$, it will add $[V]$.
		> auto units work only if the number is to the power bigger than $-12$ and smaller than $12$.
	- `units`: manual units {string}.
		> __only works if `auto_units` is false__.
	- `eng`: should the script automatically add engineering notation to the final answer {True/False}.
		> for example, if the final answer is $1000 [V]$, it will add $1 [kV]$.
	- `phasor`: should the script automatically format all of the numbers as phasors {True/False}.
		> __phasor, units and eng do not work together__.
	- `two_line`: should the script make each step it's own line {True/False}.
		> for calculations with only numbers and no variables, this __must be False__.
		> for example for the following equation: $1 + 2 + 3$, this will not work if it is True.
	- `declare`: declare a new variable {True/False}.
		> only mark True if the variable has not been set yet in the script.
	- `fin_ans`: should the script automatically add a box marking the answer {True/False}.
		> mainly for marking an import / the final calculation of a question.
	- `temp`: temporary caculation {0/1/2}.
		> for use examples check the `Tests.ipynb` file.
	- `out`: should the output be markdown or latex {Markdown/String}.
		> String is latex output.
1. Press `OK`
	> the entire command will be entered in your clipboard.
1. Go to the Jupyter Notebook and paste the command in a python cell.
1. Run the cell.
	> of course after running the cell importing the repo.

## Unusual Use Cases

### Numpy

For the numpy package, just import it as `np`, and __use the `np.` in the string of `eq`__.

### Symbols

Work partially.

### Matrices

Work for simple cases (add/sub/multiply).

### Negative Power

Does not work well, however dividing by the number instead works as expected.
> meaning instead of multiplying by $10^-6$ just divide by $10^6$