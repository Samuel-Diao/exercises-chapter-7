from example_code.groups import Group
import numpy as np


class SymmetricGroup(Group):
    symbol = "S"
    def __init__(self, n):
        super().__init__(n)

    def _validate(self, value):
        value = np.array(value)
        if not (
            value.shape == (self.n,)
            and sorted(value) == [i for i in range(0, self.n)]
        ):
            raise ValueError("Element value must be a 1 x " f"{self.n} array")

    def operation(self, a, b):
        return a[b]
    