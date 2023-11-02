class DoubleElement:

    def __init__(self, *lst):
        self.list = lst
        self.index = 0

    def __next__(self):
        if self.index < len(self.list):
            value1 = self.list[self.index]
            value2 = None
            self.index += 1
            if self.index < len(self.list):
                value2 = self.list[self.index]
                self.index += 1
            return value1, value2
        else:
            raise StopIteration

    def __iter__(self):
        return self


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)
