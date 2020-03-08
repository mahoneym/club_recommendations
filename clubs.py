import user
from graph_edge import *
import random

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
        #self.__description = "The Accounting Society seeks to provide students majoring in or interested in accounting opportunities to network with professionals, faculty and other students. In addition to networking opportunities, the Accounting Society provides opportunities for professional development and leadership, and is involved in various community service projects throughout the academic year."
        # self.__description = "abcdefghijklmnopqrstuvwxyz"

    def printRelated(self):
        print(self.__name)
        for club in self.__related:
            print("Club:" + club.getDestination().getClubName())
            print(club.getWeight())
        return None

    def getClubName(self):
        return self.__name

    def getDescription(self):
        return self.__description

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
        newConnection = GraphEdge(clubToConnectTo)
        self.__related.append(newConnection)
        return 1

    # looks at the club's most common related club
    # look for the club's heaviest edge
    # param: none
    # returns: club object to the user
    def returnMostCommonClub(self, previousIndex):
        # set the local variables so they are less than all objects
        mostCommonIndex = -1
        heaviestWeight = -1

        if(previousIndex != -1):
            previousIndex = (previousIndex + 1) % len(self.__related)
            return self.__related[previousIndex], previousIndex
        # go through the related and look for the most common link
        index = 0                   # 0 since we need to start at the beginning
        if(len(self.__related) == 0):
            return 0, 0
        while(index < len(self.__related)-1):
            if(heaviestWeight < self.__related[index].getWeight()):
                mostCommonIndex = index
                heaviestWeight = self.__related[index].getWeight()
            index = index + 1
        return self.__related[mostCommonIndex], index      # return the club to the user

    def returnARelatedClub(self, index):
        newIndex = (index + 1) % len(self.__related)
        return self.__related[newIndex], newIndex
