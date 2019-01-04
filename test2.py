import cython


@cython.cfunc
@cython.returns(cython.bint)
@cython.locals(a=cython.int, b=cython.int)
def c_compare(a,b):
    return a+b

print(c_compare(10,10))

