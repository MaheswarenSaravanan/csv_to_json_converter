from .column import Column

class Data:
    def __init__(self, column:Column, value, **kwargs):
        self.column = column
        self.value = self.column.type(value)

    def __str__(self):
        format = {
            "column": self.column.name,
            "value": self.value
        }

        return str(format)