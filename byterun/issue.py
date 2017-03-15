class Issue(object):
    def __repr__(self):
        return ('%s: "%s"' % (type(self), str(self)))

class TypeChange(Issue):
    def __init__(self, oldType, newType, identifier, context=None):
        self.oldType = oldType
        self.newType = newType
        self.identifier = identifier

    def __str__(self):
        return (
            ("Type change:  variable %s was type %s, " +
             "now is type %s") %
            (str(self.oldType), str(self.newType),
             self.identifier))

    def __eq__(self, that):
        return (self.oldType == that.oldType and
                self.newType == that.newType and
                self.identifier == that.identifier)

class DictionaryIter(object):
    def __init__(self):
        pass

    def __str__(self):
        return ("Tried to iterate over a dictionary without " +
                "explicitly calling")


    def __eq__(self, that):
        return type(self) == type(that)
