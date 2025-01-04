class House:
    def __init__(self, name, flor):
        self.name = name
        self.flor = flor
        self.say_info()

    def say_info(self):
        print(f"{self.name},{self.flor}")

    def __repr__(self):
        return f"{self.name}"

    def __len__(self):
        return self.flor

    def __eq__(self, other):
        if isinstance(other, House):
            return self.flor == other.flor
        return False


    def __lt__(self, other):
        if isinstance(other, House):
            return self.flor < other.flor
        else:
            return NotImplemented
    def __le__(self, other):
        if isinstance(other, House):
            return self.flor <= other.flor
        else:
            return NotImplemented
    def __gt__(self, other):
        if isinstance(other, House):
            return self.flor > other.flor
        else:
            return NotImplemented
    def __ge__(self, other):
        if isinstance(other, House):
            return self.flor >= other.flor
        else:
            return NotImplemented
    def __ne__(self, other):
        if isinstance(other, House):
            return self.flor != other.flor
        else:
            return True

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.flor + value)
        elif isinstance(value, House):
            return House(self.name, self.flor + value.flor)
        else:
            return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
h1 = h1 + 10
h1 += 10
h2 = 10 + h2
print(h1 == h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)


