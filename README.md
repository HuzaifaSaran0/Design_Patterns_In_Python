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
