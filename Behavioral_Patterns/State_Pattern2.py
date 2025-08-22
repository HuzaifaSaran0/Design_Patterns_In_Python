from abc import ABC, abstractmethod

class State(ABC):  # Abstract State class
    @abstractmethod
    def play(self, player):
        pass

    def pause(self, player):
        pass

    def stop(self, player):
        pass


class PlayingState(State):  # Concrete State class 1
    def play(self, player):
        print("Already playing.")
    
    def pause(self, player):
        print("Pausing playback.")
        player.state = PausingState()

    def stop(self, player):
        print("Stopping playback.")
        player.state = StoppedState()


class PausingState(State):  # Concrete State class 2
    def play(self, player):
        print("Paused playback.")
        player.state = PlayingState()

    def pause(self, player):
        print("Already Paused.")

    def stop(self, player):
        print("Stopping playback.")


class StoppedState(State):  # Concrete State class 3
    def play(self, player):
        print("Starting playback.")
        player.state = PlayingState()

    def pause(self, player):
        print("Already Paused.")

    def stop(self, player):
        print("Already Stopped.")
        

class MediaPlayer:  # Context class
    def __init__(self):
        self.state = StoppedState()
    
    def play(self):
        print("Starting media.")
        self.state.play(self)
    
    def pause(self):
        print(" Pausing media.")
        self.state.pause(self)

    def stop(self):
        print("Stopping media.")
        self.state.stop(self)


player = MediaPlayer()
player.play()   # Starting playback.
player.pause()  # Pausing playback.
player.play()   # Resuming playback.
player.stop()   # Stopping playback.
