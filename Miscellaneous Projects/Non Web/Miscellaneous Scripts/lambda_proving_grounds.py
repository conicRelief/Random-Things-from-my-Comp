#
# def f (x): return x**2
# print f(8)
#
# g = lambda x: x**2
#
# print g(8)
#
# def make_incrementor (n):   return lambda x: x + x
#
# f = make_incrementor(2)
# g = make_incrementor(6)
#
# print f(42),     g(42)

class lambdaJuggler:
    value = 0
    def __init__(self, val = 0):
        self.value = val
    def returnValue(self):
        return self.value
    def accept_lambda(self, the_lambda):
        self.value = the_lambda(self.value)

item1 = lambdaJuggler(5)
item2 = lambdaJuggler(1)

lam = lambda x: x**2

print item1.returnValue()
item1.accept_lambda(lam)
print item1.returnValue()
item2.accept_lambda(lam)
print item2.returnValue()