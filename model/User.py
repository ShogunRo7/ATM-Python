import itertools

class User :
    id_generator = itertools.count(101)

    def __init__(self, name='', pin='', currentBalance=0.0) :
        self.cardId = next(User.id_generator)
        self.name = name
        self.pin = pin
        self.currentBalance = currentBalance
