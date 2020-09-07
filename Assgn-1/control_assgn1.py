from sympy import *
init_printing(use_unicode=True)

#declaring variable for use of mathematical expression
s = symbols('s')			

#given expression
problem = 10**4*(s+5)*(s+70)/(s*(s+45)*(s+55)*(s**2+7*s+110)*(s**2+6*s+95))

#apart function returns the partial fraction decomposition of rational functions
ans = apart(problem)

pprint(ans)			#prints data in a pretty way
