from constraint import *
p = Problem()
p.addVariable("a", [1,2,3])
p.addVariable("b", [4,5,6])
print p.getSolutions()
p.addConstraint(lambda a,b: a*2 == b, ('a', 'b'))
print p.getSolutions()
