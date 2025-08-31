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

#### 1. Collection (BrowserHistory)
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

#### 2. Iterator Interface (Iterator)

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
#### 3. Concrete Iterator (ListIterator)

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
_________________________________________________________________________________________________________
## 4. Strategy Pattern
### 🎯 Purpose

The Strategy Pattern defines a family of algorithms (or behaviors), encapsulates each one, and makes them interchangeable.

Instead of hardcoding if/else statements to choose an algorithm, the Strategy Pattern lets the client plug in the desired algorithm at runtime.

This makes your system:

    Flexible → You can change algorithms without touching client code.

    Extensible → Adding a new algorithm just means creating a new class.

    Open/Closed Principle friendly → No need to modify existing logic.

In my Algorithm + DataStructure example, the Context doesn’t care which algorithm or data structure is being used. It just calls them. The client decides which ones to inject at runtime.

### 🔑 Roles in My Code

#### 1. Strategy Interface (Algorithm, DataStructure)
    Defines the contract all strategies must follow.
    Algorithm defines how data should be processed.
    DataStructure defines how data should be stored/used.
```python
class Algorithm(ABC):
    @abstractmethod
    def execute(self, data): pass

class DataStructure(ABC):
    @abstractmethod
    def use(self): pass

```

#### 2. Concrete Strategies (ConcreteAlgorithmA/B, ConcreteDataStructureA/B)

    Provide actual implementations of algorithms and data structures.

    Each class follows the common interface, so they are interchangeable.
```python
class ConcreteAlgorithmA(Algorithm):
    def execute(self, data):
        print(f"Algorithm A processing {data}")

class ConcreteAlgorithmB(Algorithm):
    def execute(self, data):
        print(f"Algorithm B processing {data}")

class ConcreteDataStructureA(DataStructure):
    def use(self):
        print("Using Data Structure A")

class ConcreteDataStructureB(DataStructure):
    def use(self):
        print("Using Data Structure B")
```
#### 3. Context (Main)
Holds references to strategies and delegates work to them.

The Context is agnostic to which algorithm/data structure is used — it just calls the interface methods.
```python
class Context:
    def __init__(self, strategy: Algorithm, data_structure: DataStructure):
        self._strategy = strategy
        self._data_structure = data_structure

    def execute(self, data):
        self._data_structure.use()
        self._strategy.execute(data)
```
#### 4. Client (Code Using Strategies)
The client decides which concrete strategies to plug into the Context.

It can easily switch to different algorithms or data structures without touching the Context code.
```python
data = "Sample Data"

context = Context(ConcreteAlgorithmB(), ConcreteDataStructureA())
context.execute(data)  
# Using Data Structure A
# Algorithm B processing Sample Data
```
### 📌 Important Detail (Encapsulation of Behavior)
    The Context never knows the details of algorithms or data structures.
If tomorrow you add ConcreteAlgorithmC or ConcreteDataStructureC, you don’t touch the Context or client logic.
The only thing that changes is which strategy you choose when creating the Context.
This keeps your system flexible and avoids bloated if/else conditions.
____________________________________________________________________________________________________________________________
## 5. Template Method Pattern
### 🎯 Purpose

The Template Method Pattern defines the skeleton of an algorithm in a base class, while letting subclasses redefine specific steps without changing the overall structure.

This makes your system:

    Consistent → The high-level process is fixed.

    Flexible → Subclasses can override details of the process.

    Extensible → New variations only require new subclasses, not rewriting the algorithm.

### 🔑 Roles in My Code

#### 1. Abstract Class (TemplateMethod)
Defines the template method (template_method) that specifies the algorithm flow.
It includes:

    Abstract methods (step_one, step_two) → must be implemented by subclasses.

    Hook/Optional method (step_three) → has a default implementation but can be overridden..
```python
class TemplateMethod(ABC):
    def template_method(self):
        self.step_one()
        self.step_two()
        self.step_three()

    @abstractmethod
    def step_one(self): pass

    @abstractmethod
    def step_two(self): pass

    def step_three(self):  # Hook
        print("Default implementation of step three.")
```

#### 2. Concrete Classes (ConcreteClassA, ConcreteClassB)

Provide implementations of the abstract steps.

    ConcreteClassA → uses the default step_three.

    ConcreteClassB → overrides all three steps, including step_three.
```python
class ConcreteClassA(TemplateMethod):
    def step_one(self):
        print("ConcreteClassA: Step One")

    def step_two(self):
        print("ConcreteClassA: Step Two")
    # step_three comes from base class


class ConcreteClassB(TemplateMethod):
    def step_one(self):
        print("ConcreteClassB: Step One")

    def step_two(self):
        print("ConcreteClassB: Step Two")

    def step_three(self):  # overrides optional step
        print("ConcreteClassB: Step Three")
```
#### 3. Template Method Execution (Client Code)
The client instantiates a concrete class and calls the template method.
The base class ensures the same process order, while allowing different subclass behavior.
```python
obj = ConcreteClassA()
obj.template_method()
# ConcreteClassA: Step One
# ConcreteClassA: Step Two
# Default implementation of step three.

obj = ConcreteClassB()
obj.template_method()
# ConcreteClassB: Step One
# ConcreteClassB: Step Two
# ConcreteClassB: Step Three
```
### 📌 Important Detail (Algorithm Skeleton)
    The core algorithm is defined once in the base class (template_method).

    Subclasses cannot change the algorithm structure (the order of steps is fixed).

    Subclasses only fill in or override steps (step_one, step_two, step_three).

    The hook (step_three) provides default behavior and makes customization optional.

    This avoids duplicated algorithm structures across subclasses while still enabling flexibility.
_________________________________________________________________________________________________________________________
## 6. Command Pattern
### 🎯 Purpose

The Command Pattern lets you wrap a request (an action to perform) inside an object.
This makes it easy to:

    Decouple → The object that triggers an action (like a button) doesn’t know how the action is done.

    Re-use → Commands can be reused in different contexts.

    Extend → Adding new actions only needs new command classes, not changes to existing code.

### 🔑 Roles in My Code

#### 1. Command Interface (Command)
Defines the execute() method.

Every command must implement this method.
```python
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
```

#### 2. Receiver (CustomerService)

The class that actually knows how to do the work (like adding a customer).
```python
class CustomerService:
    def add_customer(self):
        print("Customer added.")
```
#### 3. Concrete Command (AddCustomerCommand)
Wraps the action you want to perform (add_customer) into an object.

Calls the right method on the receiver when execute() is triggered.
```python
class AddCustomerCommand(Command):
    def __init__(self, service: CustomerService):
        self._service = service

    def execute(self):
        self._service.add_customer()
```
#### 4. Invoker (Button)
The object that triggers the command.

It doesn’t care what the command does, it just calls execute().
```python
class Button:
    def __init__(self, command: Command):
        self._command = command

    def click(self):
        self._command.execute()
```
#### 5. Client (Setup and Execution)
Creates the service, wraps it in a command, attaches the command to a button, and then clicks.
```python
service  = CustomerService()
command = AddCustomerCommand(service)
button  = Button(command)
button.click()  
# Output: Customer added.
```
### 📌 Important Detail (Algorithm Skeleton)
    Lets see we want to create a Framework and then use that Framework to 
    create Applications of different types
    The framework will be responsible for handling user interactions and executing commands.
    It doesnt know the specifics of the applications being built.
    For example: 
         for a button, when clicked, it should execute a specific command.
         That button and that execute method will be provided by Framework while
         the Application defines that command and service, that should execute by clicking
         that button.
The button doesn’t know anything about CustomerService.
The command acts as a bridge between the button and the service.
If you want a new action (e.g., DeleteCustomerCommand), you just create a new command class — no need to change the Button.
___________________________________________________________________________________________________________
## 7. Observer Pattern
### 🎯 Purpose

The Observer Pattern lets one object (the Subject) automatically notify and update other objects (the Observers) whenever it changes.

This makes it easy to:

    Decouple → The Subject doesn’t need to know the details of Observers, just that they want updates.

    Re-use → Observers can be attached or removed without changing the Subject.

    Extend → New Observers can be added anytime without changing existing code.

### 🔑 Roles in My Code

#### 1. Observer Interface (Observer)
Defines the update() method. Every Observer must implement this to react when notified.
```python
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass
```

#### 2. Concrete Observers (file1, file2, file3)

These are the actual classes that react when the Subject notifies them. Each defines its own update() logic.
```python
class file1(Observer):
    def update(self):
        print("file1 got updated")

class file2(Observer):
    def update(self):
        print("file2 got updated")

class file3(Observer):
    def update(self):
        print("file3 got updated")
```
#### 3. Subject (Subject)
Keeps a list of observers and provides methods to add/remove them.
When something changes, it calls notifyObservers() to update all.
```python
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
```
#### 4. Concrete Subject (DataSource)
The actual data holder. When its value changes, it notifies all observers.
```python
class DataSource(Subject):
    def __init__(self):
        super().__init__()
        self.value = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
        self.notifyObservers()
```
#### 5. Client (Setup and Execution)
Creates the Subject and Observers, registers the Observers, and changes the value to trigger updates.
```python
ds = DataSource()
ds.addObserver(file1())
ds.addObserver(file2())
ds.addObserver(file3())

ds.set_value(10)  
# Output:
# file1 got updated
# file2 got updated
# file3 got updated
```
### 📌 Important Detail (Automatic Update System)
    The Subject = broadcaster (DataSource).

    The Observers = listeners (file1, file2, file3).

    Whenever the Subject’s value changes → it notifies all Observers → each reacts in its own way.

This way, the Subject never directly depends on the Observers’ code.
If you add a new observer (e.g., Logger), you just attach it — no changes needed in DataSource.
__________________________________________________________________________________________________________
## 8. Mediator Pattern
### 🎯 Purpose

The Mediator Pattern centralizes communication between objects so that they don’t directly talk to each other.

Instead, they send their messages/requests to a Mediator, and the Mediator decides how to forward them.

This makes it easy to:

    Decouple → Users don’t need to know about each other, they only know the Mediator.
    Organize → The Mediator controls who gets which message.
    Extend → You can add multiple chat rooms (mediators) without changing User code.

👉 Example: In a **WhatsApp** group, if Alice sends a message, only Bob and Charlie (not Alice herself) receive it. If we have 2 groups, messages in one group don’t go to the other.
### 🔑 Roles in My Code

#### 1. Mediator Interface (ChatMediator)
Defines methods for adding users and sending messages.
```python
from abc import ABC, abstractmethod

# Mediator Interface
class Mediator(ABC):
    @abstractmethod
    def send_message(self, message: str, sender: "User") -> None:
        pass
```

#### 2. Concrete Mediator (ChatRoom)

Implements the mediator logic. Keeps track of users and forwards messages to all except the sender.
```python
# Concrete Mediator
class ChatRoom(Mediator):
    def __init__(self):
        self._users = []

    def add_user(self, user: "User") -> None:
        self._users.append(user)

    def send_message(self, message: str, sender: "User") -> None:
        for user in self._users:
            if user != sender:  # don't send back to the sender
                user.receive(message, sender)
```
#### 3. Colleague Interface (User)
Defines how a user sends and receives messages.
```python
# Colleague
class User:
    def __init__(self, name: str, mediator: Mediator):
        self._name = name
        self._mediator = mediator
        mediator.add_user(self)

    def send(self, message: str) -> None:
        print(f"{self._name} sends: {message}")
        self._mediator.send_message(message, self)

    def receive(self, message: str, sender: "User") -> None:
        print(f"{self._name} received from {sender._name}: {message}")
```
#### 4. Concrete Colleagues (RealUser)
Actual implementation of the User, interacting only through the Mediator. It could be used but i didn't use it in this code.
#### 5. Client (Setup and Execution)
Creates ChatRooms (mediators) and Users. Users send messages via the mediator.
```python
# Example Usage
chatroom1 = ChatRoom()
chatroom2 = ChatRoom()

alice = User("Alice", chatroom1)
bob = User("Bob", chatroom1)
charlie = User("Charlie", chatroom1)

ali = User("Ali", chatroom2)
# bob2 = User("Bob", chatroom2)
# charlie2 = User("Charlie", chatroom2)

alice.send("Hello everyone!")
bob.send("Hi Alice!")
```
### 📌 Important Detail (WhatsApp Group Analogy)
    Mediator = ChatRoom (Group).

    Colleagues = Users.
A user never directly messages another user → they always go through the mediator.
This allows multiple groups to exist independently, just like in real chat apps.
_________________________________________________________________________________________________
## 9. Chain of Responsibility Pattern
### 🎯 Purpose

The Chain of Responsibility Pattern allows multiple handlers to process a request sequentially until one of them handles it (or the chain ends).

This makes it easy to:

    Decouple → The sender does not need to know which handler will process the request.

    Flexible → Handlers can be added, removed, or reordered without changing the client.

    Extendable → You can add more handlers for new request types without changing existing code.

👉 Example: In an ATM Machine, when you withdraw money, the machine checks the largest denomination first (e.g., 1000 notes). If the full amount cannot be handled, it passes the remainder down the chain (e.g., to 500, then 100).
### 🔑 Roles in My Code

#### 1. Handler Interface (ATMHandler)
Defines a method for handling the request and holds a reference to the next handler.
```python
from abc import ABC, abstractmethod

class ATMHandler(ABC):
    def __init__(self, denomination, next_handler=None):
        self.denomination = denomination
        self.next_handler = next_handler

    @abstractmethod
    def handle(self, amount):
        pass
```

#### 2. Concrete Handler (ConcreteATMHandler)

Implements the actual logic for handling requests.

    Tries to process as many notes as possible for its denomination.

    If something is left, it passes the remainder to the next handler.
```python
# Concrete Mediator
class ConcreteATMHandler(ATMHandler):
    def handle(self, amount):
        dividend, remainder = divmod(amount, self.denomination)

        if dividend > 0:
            print(f"Handler{self.denomination} processed {dividend} notes of {self.denomination}")

        if remainder > 0 and self.next_handler:
            self.next_handler.handle(remainder)
        elif remainder > 0 and not self.next_handler:
            print(f"Cannot dispense {remainder}, unsupported amount.")
```
#### 3. Client (ATM Machine Setup & Execution)
The client connects handlers in a chain (1000 → 500 → 100).
It just sends the request to the first handler, which either handles it or passes it on.
```python
# Smallest denomination last
h100 = ConcreteATMHandler(100)
h500 = ConcreteATMHandler(500, h100)
h1000 = ConcreteATMHandler(1000, h500)

print("ATM Machine:")
h1000.handle(2500)   # 2x1000 + 1x500
h1000.handle(2600)   # 2x1000 + 1x500 + 1x100
h1000.handle(2000)   # 2x1000
h1000.handle(1255)   # 1x1000 + 2x100 + "cannot dispense 55"
```
### 📌 Important Detail (ATM Analogy)
    Handlers = Cash dispensers of different denominations (1000, 500, 100).

    Client = User requesting money.

A request (withdrawal) starts at the highest handler → passes remainder to the next → and so on.

👉 The ATM doesn’t need to know which handler can fully process it. It only knows the entry point (1000 note handler), and the chain takes care of the rest.
_________________________________________________________________________________________________

