__author__ = 'vlim'

# fill in this function
def fib():
    pass #this is a null statement which does nothing when executed, useful as a placeholder.
    last_yield, b4_last_yield = 1, 1

    yield b4_last_yield
    yield last_yield
    for i in xrange(2,20):
        yield_val = last_yield + b4_last_yield
        yield yield_val
        b4_last_yield = last_yield
        last_yield = yield_val




# testing code
import types

print "fib: %s" % type(fib())
if type(fib()) == types.GeneratorType:
    print "Good, The fib function is a generator."

    counter = 0
    for n in fib():
        print n
        counter += 1
        if counter == 10:
            break