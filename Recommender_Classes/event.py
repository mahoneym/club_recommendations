####### EVENT.PY #######
####### Contains the event class #######
####### Event objects will be contained in clubs #######

from datetime import date

class Event:
    """Represents a club's event in the recommendation system"""

    # the constructor for the event class
    # param: event name (string), datetime object, club (object), location (string), description (string)
    def __init__(self, name, date, club, location, description):
        self.__date = date                                  # save the date for the event
        self.__hostingClub = club                                 # save the club that is hosting the event
        self.__location = location                                # save the location of the event
        self.__dateCreated = date.today                           # save today's date that it was created
        self.__name = name
        self.__description = description

    # returns the date of the event
    def getDate(self):
        return self.__date

    # returns the club that is hosting the event
    def getClubHost(self):
        return self.__hostingClub

    # returns the location of the event
    def getLocation(self):
        return self.__location

    # returns the name of the event
    def getName(self):
        return self.__name

    # returns the descripton of the event
    def getDescription(self):
        return self.__description
