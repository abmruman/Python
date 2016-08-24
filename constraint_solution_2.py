from constraint import *
p = Problem()
p.addVariable("a", [1,2,3,4])
p.addVariable("b", [1,2,3,4])
print "Before adding constraints:"
print p.getSolutions()
p.addConstraint(lambda a,b: a+b == 5, ('a', 'b'))
p.addConstraint(lambda a,b: a*b == 6, ('a', 'b'))
print ""
print "After adding constraints (a+b = 5 and a*b = 6):"
print p.getSolutions()
