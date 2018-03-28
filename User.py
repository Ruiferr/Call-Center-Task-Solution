# 2017-2018 Programacao II (LTI)
# Grupo 009
# 52172 Rui Ferrão
# 51648 Tiago Sousa


from Person import Person


class User(Person):
    """
    User class is responsible for defining a single User that derives from Person

    """
    def __init__(self, name="", language="", domain="", service="", duration=0):
        """
        Creates a user.

        Requires: An user's name, language, domain, freetime, workedminutes
        Ensures: An object User is created with the specified attributes required
        """
        super().__init__(name, language, domain)

        self._service = service
        self._duration = duration


    def setService(self, service):
        """
        Sets the service required by user.

        Requires: A string for the service.
        Ensures: Sets the service over the previous one.
        """
        self._service = service

    def getService(self):
        """
        Ensures: A string of the user's required service.
        """
        return self._service

    def setDuration(self, duration):
        """
        Sets the duration of the user's request.

        Requires: An int for the duration of handling the request.
        Ensures: Sets the duration over the previous one.
        """
        self._duration = duration

    def getDuration(self):
        """
        Ensures: A string of the request's duration.
        """
        return str(self._duration)

    def __str__(self):
        """
        Ensures: A string representing the object with the user's name, language, domain, service and duration.
        """
        return super().__str__() + str((self.getService(), self.getDuration()))

    def __eq__(self, other):
        """
        Requires: Another object User type
        Ensures: The two objects are equal
        """
        return super().__eq__(other) and (self.getService().lower(), int(self.getDuration())) == \
                                         (other.getService().lower(), int(other.getDuration()))

    def __lt__(self, other):
        """
        Requires: Another object User type
        Ensures: One User is lesser than the other by comparing the service type
        """
        return self.getService() < other.getService()