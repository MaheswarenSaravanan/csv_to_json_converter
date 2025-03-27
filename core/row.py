from .column import Column
from .data import Data

class Row:
    def __init__(self):
        self.values = []
    
    def __str__(self):
        format = [{"column": d.column.name, "value": d.value} for d in self.values]
        return str(format)

    def add_data(self, column:Column, value):
        data = Data(column = column, value = value)
        self.values.append(data)
