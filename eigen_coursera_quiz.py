from sympy import *
init_session()
# from sympy import Matrix, Symbol, det, eye, roots, init_printing

init_printing(use_latex=True, use_unicode=False)

# --------------------------------------------------------------
a = Matrix([ [3/2, -1], [-1/2, 1/2] ])

# --------------------------------------------------------------
a = Matrix([ [4, -5, 6], [7, -8, 6], [Rational(3,2), Rational(-1, 2), -2]])
a
a.eigenvals()
a.eigenvects()

# --------------------------------------------------------------
# q2
Matrix([[0,0,0,1],[1,0,0,0],[0,1,0,0],[0,0,1,0]]).eigenvals()
Matrix([[0.1,0.1,0.1,0.7],[0.7,0.1,0.1,0.1],[0.1,0.7,0.1,0.1],[0.1,0.1,0.7,0.1]]).eigenvals()

# --------------------------------------------------------------
# separeted
Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]])
Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]]).eigenvals()
Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]]).eigenvects()

# --------------------------------------------------------------
# dumpling
Matrix([[0.1,0.7,0.1,0.1],[0.7,0.1,0.1,0.1],[0.1,0.1,0.1,0.7],[0.1,0.1,0.7,0.1]]).eigenvals()

# --------------------------------------------------------------
# q6
a = Matrix([[Rational(3,2), -1], [Rational(-1, 2), Rational(1,2)]])
l = Symbol("lambda")
char_pol = det(a - l*eye(2))
char_pol
roots(char_pol, l)

a.eigenvals()
evs = a.eigenvects()
v1 = evs[0][2][0]
v1.simplify()
v1
v2 = evs[1][2][0]
v2.simplify()
v2

c = Matrix.hstack(v1,v2)
d = c.inv() * a * c
d.simplify()
d

