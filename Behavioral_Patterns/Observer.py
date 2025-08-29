# What it is
# One object (Subject) changes, and it automatically tells other objects (Observers) about the change.

# Why it exists
# Instead of every Observer asking “Did you change?” again and again, the Subject says “I changed, here’s the new info.”

# Roles

# Subject = The thing being watched (e.g., DataSource).
# Observers = Things that react when Subject changes (e.g., Spreadsheet, Chart).

# Flow

# Observers subscribe to Subject.
# Subject stores the list of Observers.
# When Subject changes, it notifies all Observers.
# Observers react in their own way.

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

class file1(Observer):
    def update(self):
        print("file1 got updated")

class file2(Observer):
    def update(self):
        print("file2 got updated")

class file3(Observer):
    def update(self):
        print("file3 got updated")

class Subject:
    def __init__(self):
        self._observers = []

    def addObserver(self, observer):
        self._observers.append(observer)

    def removeObserver(self, observer):
        self._observers.remove(observer)

    def notifyObservers(self):
        for observer in self._observers:
            observer.update()


class DataSource(Subject):
    def __init__(self):
        super().__init__()
        self.value = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
        self.notifyObservers()


ds = DataSource()
ds.addObserver(file1())
ds.addObserver(file2())
ds.addObserver(file3())
ds.set_value(10)  # This will notify all observers and they will react accordingly
