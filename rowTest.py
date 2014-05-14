# Copyright (C) 2013 by Jordi Vallverdu <jvallver@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.



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
