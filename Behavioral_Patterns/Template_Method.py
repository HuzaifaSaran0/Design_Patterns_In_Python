from abc import ABC, abstractmethod

class TemplateMethod(ABC):
    # Template method
    def template_method(self):
        self.step_one()
        self.step_two()
        self.step_three()

    # Abstract methods
    @abstractmethod
    def step_one(self):
        pass

    @abstractmethod
    def step_two(self):
        pass

    # Default implementation (Optional Methods)
    def step_three(self):
        print("Default implementation of step three.")


# Concrete Classes
class ConcreteClassA(TemplateMethod):
    def step_one(self):
        print("ConcreteClassA: Step One")

    def step_two(self):
        print("ConcreteClassA: Step Two")

    # def step_three(self):
    #     pass


class ConcreteClassB(TemplateMethod):
    def step_one(self):
        print("ConcreteClassB: Step One")

    def step_two(self):
        print("ConcreteClassB: Step Two")

    def step_three(self):
        print("ConcreteClassB: Step Three")


obj = ConcreteClassA()
obj.template_method()

obj = ConcreteClassB()
obj.template_method()
