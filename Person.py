# 2017-2018 Programacao II (LTI)
# Grupo 009
# 52172 Rui Ferrão
# 51648 Tiago Sousa


class Person(object):
    """
    Person class is responsible for defining a single person object

    """
    def __init__(self, name="", language="", domain=""):
        """
        Creates a person.

        Requires: An persons name, language, domain, freetime, workedminutes
        Ensures: An object Person is created with the specified attributes required
        """
        self._name = name
        self._language = language
        self._domain = domain

    def setName(self, name):
        """
        Sets the name of the person.

        Requires: A string for the name.
        Ensures: Sets the name over the previous one.
        """
        self._name = name

    def getName(self):
        """
        Ensures: A string of the person's name.
        """
        return self._name

    def setLanguage(self, language):
        """
        Sets the language of the person.

        Requires: A string for the language.
        Ensures: Sets the language over the previous one.
        """
        self._language = language

    def getLanguage(self):
        """
        Ensures: A string of the person's language.
        """
        return self._language

    def setDomain(self, domain):
        """
        Sets the domain of the person.

        Requires: A string for the domain.
        Ensures: Sets the domain over the previous one.
        """
        self._domain = domain

    def getDomain(self):
        """
        Ensures: A string of the person's domain.
        """
        return self._domain

    def __repr__(self):
        """
        Ensures: A string representing the object with the person's name, language, and domain.
        """
        return self.__str__()

    def __str__(self):
        """
        Ensures: A string representing the object with the person's name, language, and domain.
        """
        return str((self.getName(), self.getLanguage(), self.getDomain()))

    def __eq__(self, other):
        """
        Requires: Another object Person type
        Ensures: The two objects are equal
        """
        return ((self.getName().lower(), self.getLanguage().lower(), self.getDomain().lower()) ==
                (other.getName().lower(), other.getLanguage().lower(), other.getDomain().lower()))