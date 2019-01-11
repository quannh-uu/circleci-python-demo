from calculator import Calculator

import unittest

class Calc0TestCaseAdd(unittest.TestCase):
    def runTest(self):
        calc = Calculator()
        assert calc.add(1, 1) == 2, "addition is wrong"
        assert calc.x == 2, "addition is wrong"


class Calc0TestCaseSub(unittest.TestCase):
    def runTest(self):
        calc = Calculator()
        assert calc.sub(1, 2) == -1, "substraction is wrong"


def getTestSuite():
    suite = unittest.TestSuite()
    suite.addTest(Calc0TestCaseAdd())
    suite.addTest(Calc0TestCaseSub())
    return suite


def main():
    runner = unittest.TextTestRunner()
    runner.run(getTestSuite())


if __name__ == '__main__':
    main()
