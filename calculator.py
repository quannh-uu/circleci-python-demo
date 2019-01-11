class Calculator(object):
    """A simple calculator for integers."""

    def __init__(self):
        self.x = 0

    def add(self, x, y):
        ret = x + y
        self.x = ret
        return ret

    def sub(self, x, y):
        ret = x - y
        self.x = ret
        return ret

    def mul(self, x, y):
        ret = x * y
        self.x = ret
        return ret

    def div(self, x, y):
        if y == 0:
            return "Can not div by zero"
        return x/y
