import observer
import states


class try_observer(observer.Observer):
    def notify(self, message):
        if int(message) == 5:
            states.main_state_machine.to("game over")


class win_observer(observer.Observer):
    def notify(self, message):
        if message == -1:
            states.main_state_machine.to("congratulations")
