class task:
    def __init__(self, initID, initDescription, initisDone):
        self.id = initID
        self.description = initDescription
        self.isDone = initisDone


class newTask:
    def __init__(self, initDescription):
        self.description = initDescription
        self.isDone = 0
