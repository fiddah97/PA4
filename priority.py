from enum import Enum

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    def __str__(self):
        if self == Priority.LOW:
            return "LOW"
        elif self == Priority.MEDIUM:
            return "MEDIUM"
        elif self == Priority.HIGH:
            return "HIGH"

# priority=Priority(2)
# print(priority)
