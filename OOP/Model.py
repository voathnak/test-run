class Model:
    def __init__(self, values):
        for key, value in values.items():
            self.__setattr__(key, value)

    def __getattr__(self, item):
        if item not in self.__dict__:
            return False
        return self.__getattribute__(item)


class Car(Model):
    def __init__(self, values):
        super(Car, self).__init__(values)

