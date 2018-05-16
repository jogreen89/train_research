class Station:
    def __init__(self, name, address = None):
        self.name = name
        self.address = address


    def get_name(self):
        return self.name

    def get_address(self):
        return self.address
