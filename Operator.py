# 2017-2018 Programacao II (LTI)
# Grupo 009
# 52172 Rui Ferrão
# 51648 Tiago Sousa

from Person import Person


class Operator(Person):
    """
    Operator class is responsible for defining a single Operator that derives from Person

    """

    def __init__(self, name="", language="", domain="", freetime="", workedminutes=0):
        """
        Creates an operator.

        Requires: An operators name, language, domain, freetime, workedminutes
        Ensures: An object Operator is created with the specified attributes required
        """
        super().__init__(name, language, domain)

        self._freetime = freetime
        self._workedminutes = workedminutes

    def setFreetime(self, freetime):
        """
        Requires: A freetime new value
        Ensures: The new freetime value is set
        """
        self._freetime = freetime

    def getFreetime(self):
        """
        Ensures: A string with the operator's freetime
        """
        return self._freetime

    def getFreetimeToString(self):
        """
        Ensures: A string with the operator's freetime represented as hh:mm format.
        """
        return str(self._freetime)[0:2] + ":" + str(self._freetime)[2:]

    def setWorkedminutes(self, workedminutes):
        """
        Requires: An int value for the total worked minutes.
        Ensures: The new workedminutes value is set.
        """
        self._workedminutes = workedminutes

    def getWorkedminutes(self):
        """
        Ensures: A string with the total worked minutes.
        """
        return str(self._workedminutes)


    def __str__(self):
        """
        Ensures: A string representing the object with the operator's name, language, domain, freetime and workedminutes.
        """
        return super().__str__() + str((self.getFreetimeToString(), self.getWorkedminutes()))

    def __eq__(self, other):
        """
        Requires: Another object Operator type
        Ensures: The two objects are equal
        """
        return super().__eq__(other) and (int(self.getFreetime()), int(self.getWorkedminutes())) == \
                                         (int(other.getFreetime()), int(other.getWorkedminutes()))

    def __lt__(self, other):
        """
        Requires: Another object Operator type
        Ensures: One Operator is lesser than the other
        """
        return (int(self.getFreetime()), int(self.getWorkedminutes())) < (int(other.getFreetime()), int(other.getWorkedminutes()))


