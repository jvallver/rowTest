rowTest
-------

Util for creating row tests in python.

Usage
-----


Let's say we have a function sum that we want to test:

    def sum(num1, num2):
        return num1 + num2

Then we probably want to create the same test for diferent imputs of this function. 
We can use @rowTest decorator for this propuse:

    import unittest

    @useRowTest
    class MyTestClass(unittest.TestCase):
    
        @rowTest(testWithTwoIntNumbers = [1,2,3],
                 testWithOneNegativeNumber = [-1, 1, 0],
                 testWithTwoNegativeNumbers = [-2, -1, -3])
        def test_sum(num1, num2, expected):
            actual = sum(num1, num2)
            self.assertEquals(actual, expected)
