####### CLUBS.PY #######
####### This file contains the Club class. A club object will represent a club in the recommender system. #######

from Recommender_Classes import user

from datetime import datetime
from Recommender_Classes import graph_edge

class Club:
    """Represents clubs at Xavier University"""

    # the constructor for the Clubs class
    def __init__(self, clubName, clubCategory, clubID, clubDescription, recommender):
        self.__name = clubName
        self.__category = clubCategory
        self.__related = []
        self.__id = clubID
        self.__recommender = recommender
        self.__description = clubDescription
        self.__upcomingEvents = []                          # a sorted list of events (sorted by date of occurrance)

    # accessor method for the club's name
    # param: none
    # return: a string- the name
    def getClubName(self):
        return self.__name

    # accessor method for the club's description
    # param: none
    # return: a string- the description
    def getDescription(self):
        return self.__description

    # accessor method for the club's category
    # param: none
    # return: a string- the category
    def getCategory(self):
        return self.__category

    # call when tbe club needs to connect it to person's other clubs
    # param: the club [object/pointer] to connect to
    # return: 0 if the club's weight was added; 1 if the club is new to related
    def addConnection(self, clubToConnectTo):
        for club in self.__related:
            if(club.getDestination().getClubName() == clubToConnectTo.getClubName()):
                club.addOneToWeight()
                return 0                                    # get out of here cause we don't need to add it again

        # If I am here, I know the club was not already related
        newConnection = graph_edge.GraphEdge(clubToConnectTo)
        self.__related.append(newConnection)
        return 1

    # looks at the club's most common related club
    # look for the club's heaviest edge
    # param: none
    # returns: graph_edge object
    def returnMostCommonClub(self, previousIndex):
        # set the local variables so they are less than all objects
        mostCommonIndex = -1
        heaviestWeight = -1

        if(previousIndex != -1):
            previousIndex = (previousIndex + 1) % len(self.__related)
            return self.__related[previousIndex], previousIndex
        # go through the related and look for the most common link
        index = 0
        if(len(self.__related) == 0):
            return 0, 0
        while(index < len(self.__related)-1):
            if(heaviestWeight < self.__related[index].getWeight()):
                mostCommonIndex = index
                heaviestWeight = self.__related[index].getWeight()
            index = index + 1
        return self.__related[mostCommonIndex], index      # return the club to the user

    # uses a random number to pick a 'random' related club
    # return: a related club
    # param: last index tried
    def returnARelatedClub(self, index):
        newIndex = (index + 1) % len(self.__related)
        return self.__related[newIndex], newIndex

    # adds an event to the club's list
    # param: a (pointer to an) event object
    # return: nothing
    def addEvent(self, event):
        index = 0
        looking = True
        if(len(self.__upcomingEvents) == 0):        # if there's no Events
            # we don't have to look and we can just add the event to be the first in the list
            looking = False
            self.__upcomingEvents.append(event)

        while(index < len(self.__upcomingEvents) and looking == True):
            if(self.__upcomingEvents[index].getDate() > event.getDate()):
                self.__upcomingEvents.insert(index, event)
                looking = False
            elif(index == (len(self.__upcomingEvents)-1)):
                self.__upcomingEvents.append(event)
                looking = False
            index = index + 1

    # gets the next event
    # param: none
    # return: the next event object for this club
    def getNextEvent(self):
        event = None
        if(len(self.__upcomingEvents) > 0):
            index = 0
            stillInPastEvents = True
            while(stillInPastEvents == True and index < len(self.__upcomingEvents)):
                if(self.__upcomingEvents[index].getDate() >= datetime.now()):
                    stillInPastEvents = False
                    event = self.__upcomingEvents[index]
                index = index + 1
        return event

    # prints the club's Events
    # param: none
    # returns: nothing
    def getClubEvents(self):
        for event in self.__upcomingEvents:
            print("Event Name: " + event.getName() + "     Event date: " + str(event.getDate()))

    # get the number of related Clubs
    # param: none
    # returns the number of related list
    def getNumberOfRelated(self):
        return len(self.__related)
