# Lets see we want to create a Framework and then use that Framework to 
# create Applications of different types
# The framework will be responsible for handling user interactions and executing commands.
# It doesnt know the specifics of the applications being built.
# For example: 
#    for a button, when clicked, it should execute a specific command.
#    That button and that execute method will be provided by Framework while
#    the Application defines that command and service, that should execute by clicking
#    that button.


from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Button:
    def __init__(self, command: Command):
        self._command = command

    def click(self):
        self._command.execute()


class CustomerService:
    def add_customer(self):
        print("Customer added.")


class AddCustomerCommand(Command):
    def __init__(self, service: CustomerService):
        self._service = service
 
    def execute(self):
        self._service.add_customer()


service  = CustomerService()
command = AddCustomerCommand(service)
button  = Button(command)
button.click()  # Output: Customer added.
