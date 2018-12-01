class Vector(object):
    def __init__(self, *elements):
        self.elements = elements
        self.iterator = None

    def manhattan_distance(self):
        return sum(
            abs(n)
            for n in self.elements
        )

    def __add__(self, other):
        return Vector(*[
            a + b
            for a, b in zip(self.elements, other.elements)
        ])

    def __sub__(self, other):
        return Vector(*[
            a - b
            for a, b in zip(self.elements, other.elements)
        ])

    def __mul__(self, k):
        return Vector(*[
            k * n
            for n in self.elements
        ])

    def __eq__(self, other):
        return self.elements == other.elements

    def __ne__(self, other):
        return self.elements != other.elements

    def __hash__(self):
        return hash(self.elements)

    def __str__(self):
        return f"({', '.join(str(n) for n in self.elements)})"

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        self.iterator = iter(self.elements)
        return self

    def __next__(self):
        return next(self.iterator)
