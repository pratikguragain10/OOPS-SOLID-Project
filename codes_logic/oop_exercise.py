"""Simple OOP demo: Counter and Triangle classes with basic functionality."""

from math import sqrt

class Counter:
    """Simple counter to increment or decrement a numeric value."""

    def __init__(self):
        """Initialize counter to zero."""
        self.value = 0

    def incr(self):
        """Increment the counter by 1."""
        self.value += 1

    def decr(self):
        """Decrement the counter by 1."""
        self.value -= 1

    def incrby(self, n: int):
        """Increment the counter by n."""
        self.value += n

    def decrby(self, n: int):
        """Decrement the counter by n."""
        self.value -= n


class Triangle:
    """Represents a triangle with 3 points and can calculate perimeter or check equality."""

    def __init__(self):
        """Initialize with an empty list of points."""
        self.points = []

    def add_point(self, x, y):
        """Add a point to the triangle; max 3 points allowed."""
        if len(self.points) >= 3:
            raise ValueError("Only 3 points allowed")
        self.points.append((x, y))

    def _dist(self, p1, p2):
        """Return Euclidean distance between two points."""
        return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    def perimeter(self):
        """Return the perimeter of the triangle."""
        if len(self.points) != 3:
            raise ValueError("Need 3 points to find perimeter")
        a, b, c = self.points
        return self._dist(a, b) + self._dist(b, c) + self._dist(c, a)

    def __eq__(self, other):
        """Check equality based on sorted points."""
        return sorted(self.points) == sorted(other.points)


if __name__ == "__main__":
    print("=== Counter Demo ===")
    c = Counter()
    c.incr()
    c.incrby(5)
    c.decrby(2)
    c.decr()
    print("Final Counter value:", c.value)

    print("\n=== Triangle Demo ===")
    t1 = Triangle()
    t1.add_point(0, 0)
    t1.add_point(0, 3)
    t1.add_point(4, 0)
    print("t1 perimeter:", t1.perimeter())

    t2 = Triangle()
    t2.add_point(1, 2)
    t2.add_point(2, 1)
    t2.add_point(1, 5)
    print("t2 perimeter:", t2.perimeter())

    t3 = Triangle()
    t3.add_point(1, 2)
    t3.add_point(2, 1)
    t3.add_point(1, 5)
    print("t3 perimeter:", t3.perimeter())

    print("\nEquality Checks:")
    print("t1 == t3:", t1 == t3)
    print("t1 == t2:", t1 == t2)
    print("t2 == t3:", t2 == t3)

