class EditorState:  # Memento Class
    def __init__(self, content: str):
        self._content = content   # private variable

    def get_content(self):
        return self._content


class Editor:  # Originator Class
    def __init__(self):
        self._content = ""

    def set_content(self, content: str):
        self._content = content

    def get_content(self):
        return self._content

    def create_state(self) -> EditorState:
        """Create a memento (snapshot)"""
        return EditorState(self._content)

    def restore(self, state: EditorState):
        """Restore from a memento"""
        self._content = state.get_content()
        
class History:  # CareTaker Class
    def __init__(self):
        self.history = []

    def push(self, state):
        self.history.append(state)
    
    def pop(self):
        self.history.pop()
        return self.history[-1]
 
 
editor = Editor()
history = History()

editor.set_content("A")
history.push(editor.create_state())
print(editor.get_content())


editor.set_content("B")
history.push(editor.create_state())
print(editor.get_content())


editor.set_content("C")
history.push(editor.create_state())
editor.restore(history.pop())
print(editor.get_content())



