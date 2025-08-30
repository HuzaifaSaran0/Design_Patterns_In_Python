# If we have to create a whatsapp group, where if a person sends the message, then all the
# others except that person would receive that message. 
# For example, if Alice sends a message, then Bob and Charlie should receive it, but not Alice herself.
# So for that we have this MEDIATOR pattern.
# in this pattern, Mediator class is like Group and the colleagues are the Users.
# The Mediator handles the communication between Users, ensuring that 
# messages are sent to the appropriate recipients.
# If we create 2 chat rooms, users in one room shouldn't receive messages from the other room.

# Roles: 
#       Mediator: ChatRoom
#       Colleagues: Users (Alice, Bob, Charlie, Ali)
# Flow:
#       1. User sends a message
#       2. Mediator receives the message
#       3. Mediator forwards the message to all other users
#       4. All the other Users except the sender receive the message

from abc import ABC, abstractmethod

# Mediator Interface
class Mediator(ABC):
    @abstractmethod
    def send_message(self, message: str, sender: "User") -> None:
        pass


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
