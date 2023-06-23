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

    def f(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return self.f(n-1) + self.f(n-2)

    def values(self, start_index: int) -> list[int]:
        return self.values[start_index:]

    def this_function_is_not_typechecked_as_no_typehint(self):
        a = 'b'
        b = 5.0
        return a+b


def main() -> None:
    obj = MyWorstCodeEver()
    print(obj.f('5'))
    print(obj.f(obj.has_values()))
    obj.values.append(5.0)
