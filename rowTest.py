"""
Python Row Tests

@author: jvallver [jvallver@gmail.com]
"""


def useRowTest(cls):
    def _wrapMethod(method, *params, **kwargs):
        def wrap(*args, **kwargs):
            method(*(args + params), **kwargs)
        return wrap
    items = cls.__dict__.iteritems()
    attrToBeSet = []
    attrToDelete = []
    for name, method in items:
        if hasattr(method, 'testParams'):
            for functionName, functionArgs in method.testParams.iteritems():
                attrToBeSet.append([cls, functionName, _wrapMethod(method, *functionArgs)])
            attrToDelete.append([cls, method.__name__])
    [setattr(*attr) for attr in attrToBeSet]
    [delattr(*attr) for attr in attrToDelete]
    return cls


def rowTest(**testParams):
    def wrap(functor):
        def wrap_f(*args, **kwargs):
            functor(*args, **kwargs)
        wrap_f.testParams = testParams
        wrap_f.__name__ = functor.__name__
        return wrap_f
    return wrap
