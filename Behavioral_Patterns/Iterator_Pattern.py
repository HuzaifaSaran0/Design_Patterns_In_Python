from abc import ABC, abstractmethod

# Iterator interface
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def current(self):
        pass

    @abstractmethod
    def next(self):
        pass

# Concrete Iterator
class ListIterator(Iterator):
    def __init__(self, items):
        self._items = items
        self._index = 0

    def has_next(self):
        return self._index < len(self._items)

    def current(self):
        return self._items[self._index]

    def next(self):
        if self.has_next():
            item = self._items[self._index]
            self._index += 1
            return item


# Browser History
class BrowserHistory:
    def __init__(self):
        self._history = []
        self._index = 0

    def push(self, url):
        self._history.append(url)
        self._index += 1

    def create_iterator(self):
        return ListIterator(self._history)
    

history = BrowserHistory()
history.push("a")
history.push("b")
history.push("c")

iterator = history.create_iterator()
while iterator.has_next():
    print(iterator.next())
