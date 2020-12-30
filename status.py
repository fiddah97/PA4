from enum import Enum

class Status(Enum):
    NEW = 1
    IN_PROGRESS = 2
    DONE = 3

    def __str__(self):
        if self == Status.NEW:
            return "NEW"
        elif self == Status.IN_PROGRESS:
            return "in-progress"
        elif self == Status.DONE:
            return "Done"

# status=Status(3)
# print(status)