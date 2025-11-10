"""
Simple OOP example:
- Counter: increase or decrease numbers
- Triangle: store 3 points and find perimeter
"""

from math import sqrt


class Counter:
    def __init__(self):
        self.value = 0

    def incr(self):
        self.value += 1

    def decr(self):
        self.value -= 1

    def incrby(self, n: int):
        self.value += n

    def decrby(self, n: int):
        self.value -= n


class Triangle:
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        if len(self.points) >= 3:
            raise ValueError("Only 3 points allowed")
        self.points.append((x, y))

    def _dist(self, p1, p2):
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def perimeter(self):
        if len(self.points) != 3:
            raise ValueError("Need 3 points to find perimeter")
        a, b, c = self.points
        return self._dist(a, b) + self._dist(b, c) + self._dist(c, a)

    def __eq__(self, other):
        return sorted(self.points) == sorted(other.points)


if __name__ == "__main__":
    print("=== Counter Demo ===")
    c = Counter()
    c.incr()          # value = 1
    c.incrby(5)       # value = 6
    c.decrby(2)       # value = 4
    c.decr()          # value = 3
    print("Final Counter value:", c.value)  # Should print 3

    print("\n=== Triangle Demo ===")
    # Triangle t1
    t1 = Triangle()
    t1.add_point(0, 0)
    t1.add_point(0, 3)
    t1.add_point(4, 0)
    print("t1 perimeter:", t1.perimeter())  # 12.0

    # Triangle t2
    t2 = Triangle()
    t2.add_point(1, 2)
    t2.add_point(2, 1)
    t2.add_point(1, 5)
    print("t2 perimeter:", t2.perimeter())

    # Triangle t3 (same points as t2)
    t3 = Triangle()
    t3.add_point(1, 2)
    t3.add_point(2, 1)
    t3.add_point(1, 5)
    print("t3 perimeter:", t3.perimeter())

    # Equality checks
    print("\nEquality Checks:")
    print("t1 == t3:", t1 == t3)  # False
    print("t1 == t2:", t1 == t2)  # False
    print("t2 == t3:", t2 == t3)  # True

