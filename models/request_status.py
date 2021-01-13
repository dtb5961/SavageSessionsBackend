from enum import Enum
class Status(Enum):
    ORDERED = 1
    PROCESSING = 2
    BEING_FILLED = 3
    AWAITING_FEEDBACK = 4
    RESOLVED = 5
    REOPENED = 6

    def to_string(self):
        return self.name

    def __add__(self,val):
        if(self.value + val < 7):
            return Status(self.value + val)
        else:
            return Status(1)