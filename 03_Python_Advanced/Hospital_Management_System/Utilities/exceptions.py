class Invalid_Patient(Exception):
    def __init__(self, message  = "Invalid Patient ID"):
        self.message = message
        super().__init__(self.message)


class Invalid_Doctor(Exception):
    def __init__(self, message = "Invalid Doctor ID"):
        self.message = message
        super().__init__(self.message)

class Invalid_Treatment(Exception):
    def __init__(self, message = "Invalid Treatment added"):
        self.message = message
        super().__init__(self.message)

class Invalid_username(Exception):
    def __init__(self, message = "Invalid Username"):
        self.message = message
        super().__init__(self.message)

class Invalid_password(Exception):
    def __init__(self, message = "Invalid Password"):
        self.message = message
        super().__init__(self.message)
        