from sys import maxsize


class New:

    def __init__(self, surname=None, name=None, id=None):
        self.surname = surname
        self.name = name
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name