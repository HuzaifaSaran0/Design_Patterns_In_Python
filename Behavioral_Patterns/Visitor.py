from abc import ABC, abstractmethod

# Element Interface (Animal)
class Animal(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


# Concrete Elements (Lion, Monkey, Elephant)
class Elephant(Animal):
    def accept(self, visitor):
        visitor.visit_elephant(self)

class Lion(Animal):
    def accept(self, visitor):
        visitor.visit_lion(self)

class Monkey(Animal):
    def accept(self, visitor):
        visitor.visit_monkey(self)


# Visitor Interface
class AnimalVisitor(ABC):
    @abstractmethod
    def visit_elephant(self, elephant: Elephant):
        pass

    @abstractmethod
    def visit_lion(self, lion: Lion):
        pass

    @abstractmethod
    def visit_monkey(self, monkey: Monkey):
        pass


# Concrete Visitor1
class SpeakVisitor(AnimalVisitor):
    def visit_elephant(self, elephant: Elephant):
        print("The elephant trumpets.")

    def visit_lion(self, lion: Lion):
        print("The lion roars.")

    def visit_monkey(self, monkey: Monkey):
        print("The monkey chatters.")


# Concrete Visitor2
class FeedVisitor(AnimalVisitor):
    def visit_elephant(self, elephant: Elephant):
        print("Feeding the elephant with fruits.")

    def visit_lion(self, lion: Lion):
        print("Feeding the lion with meat.")

    def visit_monkey(self, monkey: Monkey):
        print("Feeding the monkey with bananas.")


# Client Code
animals = [Elephant(), Lion(), Monkey()]

speak_visitor = SpeakVisitor()
feed_visitor = FeedVisitor()

for animal in animals:
    animal.accept(speak_visitor)
    animal.accept(feed_visitor)
