# 2017-2018 Programacao II (LTI)
# Grupo 009
# 52172 Rui Ferrão
# 51648 Tiago Sousa

from constants import *
from Time import Time
from Operator import Operator
from User import User
from collections import UserList
from operator import itemgetter


class File(UserList):
        """
        File class is responsible for dealing with all matters related to .txt files

        """

        def __init__(self, filename):
            """
            Creates an empty list

            Requires: filename, a .txt file's name
            Ensures: An empty list with a certain time and a subject related with the filename
            """

            super().__init__(self)

            self._time = filename[-9:-7] + filename[-6:-4]
            self._subject = filename[:-9]
            self._filename = filename
            self._header_time = ""
            self._header_subject = ""

        def getCurrentTime(self):
            """
            Ensures: A string with the file's time as a 4 digit number.
            """
            return self._time

        def getCurrentTimeString(self):
            """
            Ensures: A string with the file's time as an hh:mm representation.
            """
            return str(self._time)[0:2] + ":" + str(self._time)[2:]

        def getSubject(self):
            """
            Ensures: A string with the file's subject name.
            """
            return self._subject

        def getFilename(self):
            """
            Ensures: A string with the file's name.
            """
            return self._filename


        def readFile(self):
            """
            Opens the file, defines the header time and the header subject and finally makes sure there are no
            inconsistencies between the file's name and header.

            Ensures: The header_time and header_subject are assign, and asserts that the file's name is the same
                     as the header's name
            """


            in_file = open(self._filename,"r")

            for i in range(HEADER_LINE_TIME):  # read 3 lines to skip to the time part of the header
                    in_file.readline()
            self._header_time = in_file.readline()

            for i in range(HEADER_LINE_SUBJECT):  # read 2 more lines to skip to the subject part of the header
                    in_file.readline()
            self._header_subject = in_file.readline()

            in_file.close()

            self._header_time  = self._header_time[:2] + self._header_time[3:-1]
            self._header_subject = self._header_subject[:-2].lower()


            assert self._time == self._header_time and self._subject == self._header_subject, \
                "Error in input file: inconsistency between name and header in file " + self._filename


        def getOperators(self):
            """
            Reads the operators file and splits the properties name, language, domain, freetime and workedminutes,
            and uses them to define a single operator.
            Afterwards, it appends said operator to the list. It does this until the whole file has been read and
            all the operators have been appended.

            Ensures: A list of Operators.
            """
            self.readFile()

            in_file = open(self._filename, "r")

            for i in range(7):  # read some lines to skip the header
                in_file.readline()
            for line in in_file:
                name, language, domain, freetime, workedminutes = line.strip().split(', ')
                workedminutes = int(workedminutes)
                freetime = Time(freetime).getInt()
                op = Operator(name, language, domain, freetime, workedminutes)
                self.append(op)

            in_file.close()


        def getRequests(self):
            """
            Reads the request file and splits the properties name, language, domain, service and duration,
            and uses them to define a single user. Afterwards, it appends said user to the list.
            It does this until the whole file has been read and all the user's requests have been appended.

            Ensures: A list of Users.
            """
            self.readFile()

            in_file = open(self._filename,"r")

            for i in range(7):  # read some lines to skip the header
                in_file.readline()

            for line in in_file:
                name, language, domain, service, duration = line.strip().split(', ')
                duration = int(duration)
                user = User(name, language, domain, service, duration)
                self.append(user)

            in_file.close()



        def compareHeaders(self, other):
            """
            Requires: Another .txt file name.
            Ensures: It compares the headers of the two files and in case they are the same it returns True.
            """
            header1 = ""
            header2 = ""
            f1=open(self._filename, "r")
            for i in range(HEADER_TOTAL_LINES-1):
                header1 = header1 + f1.readline()

            f1.close()


            f2=open(other._filename, "r")

            for i in range(HEADER_TOTAL_LINES-1):
                header2 = header2 + f2.readline()

            f2.close()

            return True if header1 == header2 else False




        def assignTasks(self, other):
            """
            Sorts two lists, the operators list and the requests.
            Creates a list of assigned requests (timetable) and an updated list of operators.

            Ensures: The operators list is sorted by the minimum hour at which the operator will be free,
                     then by the total number of worked minutes of that operator, and then alphabetically.
                     The requests list is sorted first by 'premium' users and then by 'fremium' users.
                     After the lists are sorted, it assigns each user request to an appropriate operator
                     (if there is one),then it updates the list of operators and creates a list of assigned requests.
            """

            assert self.compareHeaders(other), \
                "\nError in input files, inconsistency between files " + self._filename + " and "+ other._filename+"\n"

            reqSort = sorted(other, key=lambda User: User.getService(), reverse=True)
            opeSort = sorted(self, key=lambda Operator: (Operator.getFreetime(),Operator.getWorkedminutes(),Operator.getName()))
            list_assign = []

            flag = True
            i = 0

            for elem in reqSort:
                while flag == True and i < len(opeSort):
                    if elem.getLanguage() == opeSort[i].getLanguage() and elem.getDomain() in opeSort[i].getDomain() \
                            and int(opeSort[i].getWorkedminutes()) + int(elem.getDuration()) <= 240:
                        flag = False
                        if int(self.getCurrentTime()) > int(opeSort[i].getFreetime()):
                            list_assign.append((self.getCurrentTimeString(), elem.getName(), opeSort[i].getName()))

                            opeSort[i].setWorkedminutes(int(opeSort[i].getWorkedminutes()) + int(elem.getDuration()))   #update operator worked minutes

                            currentTime = Time(self.getCurrentTimeString())                                             #update operator freetime
                            currentTime.addMin(int(elem.getDuration()))
                            newFreetime = int(currentTime.getInt())
                            opeSort[i].setFreetime(newFreetime)

                        else:
                            list_assign.append((Time().getTimeToString(opeSort[i].getFreetime()), elem.getName(), opeSort[i].getName()))

                            opeSort[i].setWorkedminutes(int(opeSort[i].getWorkedminutes()) + int(elem.getDuration()))   # update operator worked minutes

                            opeTime = Time(opeSort[i].getFreetimeToString())                                            #update operator freetime
                            opeTime.addMin(int(elem.getDuration()))
                            newFreetime = int(opeTime.getInt())
                            opeSort[i].setFreetime(newFreetime)

                        opeSort = sorted(self, key=lambda Operator: \
                                (Operator.getFreetime(), Operator.getWorkedminutes(), Operator.getName()))
                    else:
                        i = i + 1
                if i == len(self):
                    list_assign.append((self.getCurrentTimeString(), elem.getName(), "not-assigned"))
                i = 0
                flag = True

            list_assign = sorted(list_assign, key=itemgetter(0, 1))
            list_ope = sorted(self, key=lambda Operator: (Operator.getFreetime(), Operator.getName()))


            self.outputTimetable(list_assign) #call method to output timetable??h??.txt
            self.outputOperators(list_ope)    #call method to output operators??h??.txt


        def outputTimetable(self, list_assign):
            """
            Creates a .txt file with the list of assigned requests, which is called "timetable00hh00.txt".

            Requires: A list_assign which is the list of assigned requests.
            Ensures: A txt file written with an updated header and a list of assigned requests.
            """

            timetable_filename = "timetable" + self.outputFilesUpdateTime(0) + ".txt"
            header = self.getOutputHeader()
            out_file = open(timetable_filename, "w")
            out_file.write(header + "Timetable:\n")
            for elem in list_assign:
                out_file.write(", ".join(elem) + "\n")
            out_file.close()


        def outputOperators(self, list_ope):
            """
            Creates a .txt file with the updated list of operators, called "operators00hh00.txt".

            Requires: a list_ope which is a list of operators.
            Ensures: a txt file written with an updated header and an updated list of operators.
            """
            operators_filename = self._subject + self.outputFilesUpdateTime(0) + ".txt"
            header = self.getOutputHeader()
            out_file = open(operators_filename, "w")
            out_file.write(header + "Operators:\n")
            sorted(self, key=lambda Operator: (Operator.getFreetime(), Operator.getName()))
            for elem in list_ope:
                out_file.write(str(elem.getName())+", "+ str(elem.getLanguage())+", "+ str(elem.getDomain())+", "+ \
                               str(elem.getFreetimeToString())+", "+ str(elem.getWorkedminutes() + "\n"))
            out_file.close()



        def outputFilesUpdateTime(self, val):
            """
            Updates the time 5 minutes and returns it on a string format

            Requires: A val of int type (0 or 1) which will tell the script to return either 00:00 or
                      00h00 string format.
            Ensures: Returns a string of with the updated time with either 00:00 or 00h00 format.
            """
            newTime = Time(self.getCurrentTimeString())
            newTime.addMin(5)

            if val == 0:
                return str(newTime.getHour()) + "h" + str(
                    "0" + str(newTime.getMin()) if int(newTime.getMin()) < 10 else newTime.getMin())
            else:
                return str(newTime.getHour()) + ":" + str(
                    "0" + str(newTime.getMin()) if int(newTime.getMin()) < 10 else newTime.getMin())


        
        def getOutputHeader(self):
            """
            Reads the file and creates an header for the output files.

            Ensures: A standard_header with the updated time for the new files that are going to be created.
            """
            standart_header = ""

            f1 = open(self._filename)
            for i in range(HEADER_TOTAL_LINES - 1):
                if i == HEADER_LINE_TIME:
                    standart_header = standart_header + self.outputFilesUpdateTime(1) + "\n"
                    f1.readline()
                else:
                    thisline = f1.readline()
                    standart_header = standart_header + thisline
            f1.close()

            return standart_header



        def __eq__(self, other):
            """
            Ensures: The two files are equal.
            """
            return self.getFilename() == other.getFilename()


        def __str__(self):
            """
            Ensures: A string representing the list with the file's name and the content.
            """
            return str(self.getFilename()) + ": " + super().__str__()