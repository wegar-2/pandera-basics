

class A:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class B:

    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':

    A_inst = A(1, 3)
    B_inst = B(4, 55)
    A_inst.z = 32  # allowed by IDE
    B_inst.z = 333 # not allowed by IDE
