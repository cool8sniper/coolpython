from functools import partial, partialmethod


basetwo = partial(int, base=2)
print(basetwo('10010'))


def standalone(self, a=1, b=2):
    "Standalone function"

    print('  called standalone with:', (self, a, b))
    if self is not None:
        print('  self.attr =', self.attr)


def standalone(a=1, b=2):
    "Standalone function"

    print('  called standalone with:', (a, b))


class MyClass(object):
    #  Demonstration class for functools

    def __init__(self):
        self.attr = 'instance attribute'

    method1 = partialmethod(standalone)  # use partialmethod
    method2 = partial(standalone)  # use partial


o = MyClass()
o.method1()

# can't use partial
# o.method2()


stand = partial(standalone, a=5)
stand()

