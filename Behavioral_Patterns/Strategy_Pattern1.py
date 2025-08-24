  from abc import ABC, abstractmethod


class Algorithm(ABC):
    @abstractmethod
    def execute(self, data):
        pass

class DataStructure(ABC):
    @abstractmethod
    def use(self):
        pass

class ConcreteDataStructureA(DataStructure):
    def use(self):
        print("Using Data Structure A")

class ConcreteDataStructureB(DataStructure):
    def use(self):
        print("Using Data Structure B")

class ConcreteAlgorithmA(Algorithm):
    def execute(self, data):
        print(f"Algorithm A processing {data}")


class ConcreteAlgorithmB(Algorithm):
    def execute(self, data):
        print(f"Algorithm B processing {data}")


class Context:
    def __init__(self, strategy: Algorithm, data_structure: DataStructure):
        self._strategy = strategy
        self._data_structure = data_structure

    def execute(self, data):
        self._data_structure.use()
        self._strategy.execute(data)

# Example usage

data = "Sample Data"
context = Context(ConcreteAlgorithmB(), ConcreteDataStructureA())
context.execute(data)
