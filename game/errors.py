from email import message


class NoClassError(Exception):
    def __init__(self, message='This class is not found! Please enter a correct class-name.'):
       self.message = message
       super().__init__(self.message)

class NoNameError(Exception):
    def __init__(self, message='This field cannot be empty! Please fill in a name.'):
        self.message = message
        super().__init__(self.message)

class NoAgeError(Exception):
    def __init__(self, message='Thsi field cannot be empty! Please fill in an Age.'):
        self.message = message
        super().__init__(self.message)

class NoRaceError(Exception):
    def __init__(self, message='This field cannot be empty! Please fill in a race.'):
        self.message = message
        super().__init__(self.message)

class NoLanguageError(Exception):
    def __init__(self, message='This field cannot be empty! Please fill in a language.'):
        self.message = message
        super().__init__(self.message)     

  
