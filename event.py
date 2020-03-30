from datetime import date

class Event:
    """Represents a club's event in the recommendation system"""

    def __init__(self, name, date, club, location, description):
        self.__date = date                                  # save the date for the event
        self.__hostingClub = club                                 # save the club that is hosting the event
        self.__location = location                                # save the location of the event
        self.__dateCreated = date.today                           # save today's date that it was created
        self.__name = name
        self.__description = description

    def getDate(self):
        return self.__date

    def getClubHost(self):
        return self.__hostingClub

    def getLocation(self):
        return self.__location

    def getEventName(self):
        return self.__name

    def getEventDescription(self):
        return self.__description
