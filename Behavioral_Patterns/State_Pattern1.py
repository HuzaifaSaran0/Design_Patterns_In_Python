from abc import ABC, abstractmethod


class State(ABC): # Abstract State class
    @abstractmethod
    def MouseDown(self):
        pass

    @abstractmethod
    def MouseUp(self):
        pass

class SelectionTool(State): # Concrete State class 1
    def MouseDown(self):
        return "Selection Icon Showing"

    def MouseUp(self):
        return "Drawing Rectangle"
    

class BrushTool(State): # Concrete State class 2
    def MouseDown(self):
        return "Brush Icon Showing"

    def MouseUp(self):
        return "Drawing with Brush"


class EraserTool(State): # Concrete State class 3
    def MouseDown(self):
        return "Eraser Icon Showing"

    def MouseUp(self):
        return "Erasing Drawing"


class Main: # Context class 
    def __init__(self):
        self.state = EraserTool()

    def MouseDown(self):
        print(self.state.MouseDown())

    def MouseUp(self):
        print(self.state.MouseUp())


tool = Main()
tool.MouseDown()
tool.MouseUp()
