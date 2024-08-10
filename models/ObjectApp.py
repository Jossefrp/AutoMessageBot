class ObjectApp:
    def __init__(self, header:str, values:list, status:bool = True):
        self.header = header
        self.values = values
        self.status = status