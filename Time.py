# 2017-2018 Programacao II (LTI)
# Grupo 009
# 52172 Rui Ferrão
# 51648 Tiago Sousa


class Time(object):
    """
    Time class is responsible for dealing with all matters related with time

    """

    def __init__(self,hm="00:00"):
        """
        Creates a Time object.

        Requires: A string hm in the format '00:00'
        Ensures: An object Time is created with a certain hour and minutes associated with it.
        """
        self._hour = int(hm.split(':')[0])
        self._min = int(hm.split(':')[1])

    def sethour(self, hour):
        """
        Sets a new value for the hour.

        Requires: An int value with the new hour.
        Ensures: Sets the hour over the previous one.
        """
        self._hour = hour

    def getHour(self):
        """
        Ensures: A string with the hour value.
        """
        return self._hour

    def setMin(self, min):
        """
        Sets a new value for the minutes.

        Requires: An int value with the new minutes.
        Ensures: Sets the minutes over the previous one.
        """
        self._min = min

    def getMin(self):
        """
        Ensures: A string with the minute value.
        """
        return self._min


    def addMin(self, incr):
        """
        Increments the value of minutes, possibly changing the number of hours as well.

        Requires: incr of type int.
        Ensures: Increases the number of minutes by the number of the incr given.
        """
        if self.getMin() + incr < 60:
            self._min += incr
        else:
            self._hour += (incr + self.getMin())//60
            self._min = (incr + self.getMin())%60



    def getInt(self):
        """
        Ensures: The number of hours and minutes as an int value.
        """
        if int(self.getMin()) < 10:
            return int(str(self.getHour()) + "0" + str(self.getMin()))
        else:
            return int(str(self.getHour()) + str(self.getMin()))



    def getTimeToString(self, val):
        """
        Get an HH:MM time representation from a random 4 digit int.

        Requires: A 4 digit int value.
        Ensures: A string with a time represented as HH:MM.
        """
        return str(val)[0:2] + ":" + str(val)[2:]


    def __str__(self):
        '''
        Get an HH:MM time representation from the time.

        Ensures: A string with a time represented as HH:MM.
        '''
        if int(self.getMin()) < 10:
            return str(self.getHour()) + ":0" + str(self.getMin())
        else:
            return str(self.getHour()) + ":" + str(self.getMin())


    def __eq__(self, other):
        """
        Requires: Another object Time type
        Ensures: The two objects are equal
        """
        return (int(self._hour), int(self._min)) == (int(other._hour), int(other._min))


    def __lt__(self, other):
        """
        Requires: Another object Time type
        Ensures: One object is lesser than the other
        """
        return (int(self.getInt()) < (int(other.getInt())))