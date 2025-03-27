from .column import Column
from .row import Row

class Table:
    def __init__(self):
        self.column_details = {}
        self.data_store = []

    def __add_column__(self, name, **kwargs):        
        col = Column(name, **kwargs)
        self.column_details[name] = col
        return col

    __get_columns__ = lambda self, data: [{"name": k} for k in data]

    def __parse_dict__(self, data, infer_column):
        counter = 0
        row = Row()

        if infer_column:
            for k,v in data.items():
                data = None
                row.add_data(column = self.column_details[k], value = v)    
        else:
            counter = 0
            for v in data.values():
                data = None
                row.add_data(column = self.column_details[str(counter)], value = v)
                counter += 1

        return row


    def set_columns(self, input:iter, **kwargs):
        if not isinstance(input, (list, tuple)):
            raise TypeError("The input should be list(dict)/tuple(dict)")

        for value in input:
            name = value.pop("name")
            self.__add_column__(name, **value)


    def add_row(self, input:iter, **kwargs):
        if not isinstance(input, (list, tuple, dict)):
            raise TypeError("The input should be an iter")
        
        infer_column = False
        if "infer_column" in kwargs:
            if not isinstance(kwargs['infer_column'], bool):
                raise TypeError("infer_column argument should be of type bool")
            infer_column = kwargs['infer_column']
        
        if isinstance(input, dict):
            if infer_column:
                col_input = self.__get_columns__(input)
            else:
                col_input = [{"name": str(i)} for i in range(len(input))]

            self.set_columns(col_input)
            row = self.__parse_dict__(input, infer_column)
            self.data_store.append(row)


    def describe(self):
        format = [str(c) for _,c in self.column_details.items()]
        return format
        

    def test(self):
        print(self.describe())
        print()
        print()
        for d in self.data_store:
            print(d)