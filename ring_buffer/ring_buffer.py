class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.last_value = None

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            self.last_value = 0
        elif len(self.storage) == self.capacity:
            self.storage[self.last_value] = item
            self.last_value += 1
            if self.last_value == self.capacity:
                self.last_value = 0

    def get(self):
        return self.storage


r = RingBuffer(3)
r.append('a')
r.append('b')
r.append('c')
r.append('d')
r.append('e')
r.append('f')
r.append('g')
r.append('h')
print(r.get())
