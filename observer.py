"""Observer class"""


class Observer:
    def __init__(self):
        pass

    def notify(self, message):
        pass  # you have to implement this yourself as a custom event


"""Subject class"""


class Subject:
    def __init__(self):
        self.observers = []

    def addObserver(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.notify(message)
