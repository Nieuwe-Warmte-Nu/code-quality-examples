class MyWorstCodeEver(dict):
    values: list[int]

    def __init__(self):
        # Not going to call super
        self.values = []

    def has_values(self) -> bool:
        if bool(self.values):
            return True
        else:
            return False

    def f(self, n: int):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return self.f(n-1) + self.f(n-2)
