class User:
    class_counter = 0

    def __init__(self, name, type):
        self._id = User.class_counter + 1
        self._name = name
        self._type = type
        User.class_counter += 1

    def id(self):
        return self._id

    def name(self):
        return self._name

    def type(self):
        return self._type
