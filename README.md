# Design Patterns
#### (Open the Pattern Named file in the repo to get Code and Here in Readme, you can get the understanding of the pattern)
## 1. Memento Pattern


### 🎯 Purpose

The Memento Pattern is used to capture and restore an object’s state without exposing its internal details.
It is especially useful for implementing Undo / Redo or Checkpoint / Restore functionality.

### 🔑 Roles in My Code

#### Originator (Editor)

     The main object whose state we want to save/restore.

     Editor has content, and can create a state (snapshot) or restore one.
```python
def create_state(self): 
    return EditorState(self._content)
def restore(self, state): 
    self._content = state.get_content()
```

#### Memento (EditorState)

    Stores a snapshot of the state at a particular moment.

    Doesn’t allow modification (read-only).

    In my code → EditorState holds _content.

#### Caretaker (History)

    Manages the collection (stack) of saved states.

    Doesn’t know what’s inside the state, just pushes/pops them.

    In my code → History stores EditorState objects.

### 📌 Important Detail (Undo Style)

    My History.pop() removes the latest snapshot and returns the previous one.

    That means:

      After "C", when undo → "C" is discarded, and "B" is restored.

      This matches the Undo behavior of editors.
________________________________________________________________________________________________________________
## 2. State Pattern

### 🎯 Purpose
The State Pattern allows an object to change its behavior depending on its internal state.
It helps avoid long if/else or switch statements by encapsulating each state in a separate class.

In my state2 file example, the behavior of mouse_down and mouse_up changes depending on the currently selected tool (Selection, Brush, Eraser).

### 🔑 Roles in My Code
#### Context (ToolContext)
    The main class that holds a reference to the current state.

    Delegates actions (mouse_down, mouse_up) to the current state.

    Allows switching the state dynamically.

```python
def __init__(self):
    self.state = EraserTool()

def mouse_down(self):
    print(self.state.mouse_down())

def mouse_up(self):
    print(self.state.mouse_up())
```
#### State (Abstract Class)

    Defines the common interface (mouse_down, mouse_up) that all concrete states must implement.

    In my code → the abstract State class ensures all tools behave consistently.
```python
class State(ABC):
    @abstractmethod
    def mouse_down(self): pass

    @abstractmethod
    def mouse_up(self): pass
```
#### Concrete States (SelectionTool, BrushTool, EraserTool)

    Each concrete state represents a specific tool.

    They implement the behavior differently for mouse_down and mouse_up.
##### Examples in State1 File:

    SelectionTool → shows selection icon, draws rectangle.

    BrushTool → shows brush icon, draws with brush.

    EraserTool → shows eraser icon, erases drawing.
```python
class BrushTool(State):
    def mouse_down(self):
        return "Brush Icon Showing"

    def mouse_up(self):
        return "Drawing with Brush"
```
### 📌 Important Detail (Behavior Switching)

The behavior depends entirely on the current state:

    If context has SelectionTool:

    mouse_down() → “Selection Icon Showing”

    mouse_up() → “Drawing Rectangle”

    If context switches to BrushTool:

         mouse_down() → “Brush Icon Showing”

         mouse_up() → “Drawing with Brush”

    This makes it very easy to add new tools without modifying existing code.
_________________________________________________________________________________________________________________________
## 3. Iterator Pattern
### 🎯 Purpose

The Iterator Pattern provides a way to access elements of a collection (list, history, playlist, etc.) one at a time without exposing the underlying details of how the collection is stored.

    Instead of looping directly over an array or list, you use an Iterator object that gives you control with methods like:

    has_next() → Check if more items exist

    next() → Get the next item

    current() → Look at the current item

This makes your code cleaner, flexible, and independent of the collection’s internal structure (array, linked list, database, etc.).

In my browser history example, the iterator is used to go through visited URLs one by one, without directly touching the list inside BrowserHistory.

### 🔑 Roles in My Code

#### Collection (BrowserHistory)
   Stores the actual data (list of URLs).

Provides a method create_iterator() to give an iterator for traversal.

Hides internal storage (client doesn’t know it’s a list).
```python
class BrowserHistory:
    def __init__(self):
        self._history = []

    def push(self, url):
        self._history.append(url)

    def create_iterator(self):
        return ListIterator(self._history)
```

#### Iterator Interface (Iterator)

Defines the common methods every iterator must have:

    has_next()

    current()

    next()

This ensures all iterators behave consistently.
```python
class Iterator(ABC):
    @abstractmethod
    def has_next(self): pass

    @abstractmethod
    def current(self): pass

    @abstractmethod
    def next(self): pass
```
#### Concrete Iterator (ListIterator)

    Implements the actual traversal logic.

    Keeps track of position/index in the collection.

    Knows how to return items one by one.
```python
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
```
#### 4. Client (Code Using Iterator)
    Doesn’t care how items are stored.
    Only uses the iterator’s methods (has_next, next).
```python
history = BrowserHistory()
history.push("a")
history.push("b")
history.push("c")

iterator = history.create_iterator()
while iterator.has_next():
    print(iterator.next())
```
### 📌 Important Detail (Encapsulation of Traversal)
The client never touches the raw list (_history).

If tomorrow BrowserHistory stores items in a linked list or database, the client code won’t change.

It will still work with the iterator.
