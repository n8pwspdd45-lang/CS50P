class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size


    def deposit(self, n):
        self.add = n
        if self.size + self.add > self.capacity:
            raise ValueError("Too many cookies")
        self._size += n


    def withdraw(self, n):
        self.remove = n
        if self.size - self.remove < 0:
            raise ValueError("Not enough cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, cap):
        if not isinstance(cap, int) or cap < 0:
            raise ValueError("Invalid capacity")
        self._capacity = cap

    @property
    def size(self):
        return self._size

