class Column:
    def __init__(self, name, **kwargs):
        self.name = name
        self.unique = kwargs['unique'] if 'unique' in kwargs else False
        self.not_null = kwargs['not_null'] if 'not_null' in kwargs else False
        self.type = eval(kwargs['type']) if 'type' in kwargs else str

    def __str__(self):
        format =  {
            "name": self.name,
            "type": self.type,
            "constraints": {
                "unique": self.unique,
                "not_null": self.not_null
            }
        }
        return str(format)

