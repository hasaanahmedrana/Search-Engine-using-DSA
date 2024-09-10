class History:
    """This class represents a history item with a frequency."""
    def __init__(self, history, freq):
        """Initialize a history item with a given history and frequency."""
        self.history = history
        self.freq = freq

    def __str__(self):
        """Return a string representation of the history item."""
        return self.history * self.freq


class Maxheap:
    """ This class represents a max heap data structure."""
    def __init__(self):
        """Initialize an empty max heap."""
        self.arr = [None]
        self.size = 0

    def get_size(self):
        """Return the size of the heap."""
        return self.size

    def left_child(self, i):
        """Return the index of the left child of the node at index i."""
        return 2 * i

    def right_child(self, i):
        """Return the index of the right child of the node at index i."""
        return (2 * i) + 1

    def parent(self, i):
        """Return the index of the parent of the node at index i."""
        if i > 1:
            return i // 2
        else:
            return None

    def swap(self, i, j):
        """Swap the elements at indices i and j in the heap."""
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def insert(self, c):
        """Insert a new element into the heap and maintain the heap property."""
        self.arr.append(c)
        self.size += 1
        self.heapify_up(self.size)

    def delete(self):
        """Delete the root of the heap and maintain the heap property."""
        if self.size == 0: return;
        root = self.arr[1]
        self.arr[1] = self.arr[self.size]
        self.arr.pop()
        self.size -= 1
        self.heap_down(1)
        return root

    def heapify_up(self, idx):
        """Maintain the heap property by moving the element at index idx up the heap."""
        while idx > 1 and self.arr[idx].freq > self.arr[self.parent(idx)].freq:
            self.swap(idx, self.parent(idx))
            idx = self.parent(idx)

    def heap_down(self, idx=1):
        """Maintain the heap property by moving the element at index idx down the heap."""
        l = self.left_child(idx)
        r = self.right_child(idx)
        if l > self.size:
            return
        elif r > self.size:
            if self.arr[idx].freq >= self.arr[l].freq:
                return;
            else:
                self.swap(idx, l)
                self.heap_down(l)
        else:
            maxi = max(self.arr[l].freq, self.arr[r].freq)
            cur = self.arr[idx].freq
            if maxi == self.arr[l].freq:
                self.swap(idx, l)
                self.heap_down(l)
            elif maxi == self.arr[r].freq:
                self.swap(idx, r)
                self.heap_down(r)
            else:
                return 0;

    def peek(self):
        """Return the root of the heap without deleting it."""
        return self.arr[1]
