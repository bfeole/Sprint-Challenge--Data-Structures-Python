class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    # adds element to buffer
    def append(self, item):
        # set passed in item to current buffer position/index
        self.storage[self.current] = item
        # if we progress past our list capacity set the current index back to 0, replacing 'least' used item
        if self.current < self.capacity - 1:
            # sets up next index to be updated
            self.current += 1
        else:
            # returns us to start of list if capacity is met
            self.current = 0

    # return all elements in the buffer in a list in given order
    # should not return None values, even if present
    def get(self):
        items = []
        for i in self.storage:
            if i is not None:
                items.append(i)
        print(items)
        return items
