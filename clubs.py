import user
from graph_edge import *
import random

class Club:
    """Represents clubs at Xavier University"""

    # the constructor for the Clubs class
    def __init__(self, clubName, clubCategory, clubID, recommender):
        self.name = clubName
        self.category = clubCategory
        self.related = []
        self.id = clubID
        self.recommender = recommender

    # add a related club by pointing to it in the related array
    # returns 0 if the connection was added; o.w. returns -1
    def addRelated(self, clubName):
        club = self.recommender.getClub(clubName)                   # get pointer to the club in the recommender object
        flag = -1
        #print("about to check club")                                      # assumes the connection will not be added
        if(club != -1):
            newConnection = GraphEdge(club)    # create the graph_edge object
            self.related.append(newConnection);               # append the related array with the object
            flag = 0
        return flag

    def printRelated(self):
        print(self.name)
        for club in self.related:
            print("Club:" + club.destination.name)
            print(club.weight)
        return None

    # call when tbe club needs to connect it to person's other clubs
    # param: the club [object/pointer] to connect to
    # return: 0 if the club's weight was added; 1 if the club is new to related
    def addConnection(self, clubToConnectTo):
        for club in self.related:
            if(club.destination.name == clubToConnectTo.name):
                club.addOneToWeight()
                return 0                                    # get out of here cause we don't need to add it again

        # If I am here, I know the club was not already related
        newConnection = GraphEdge(clubToConnectTo)
        self.related.append(newConnection)
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
            previousIndex = (previousIndex + 1) % len(self.related)
            return self.related[previousIndex], previousIndex
        # go through the related and look for the most common link
        index = 0                   # 0 since we need to start at the beginning
        if(len(self.related) == 0):
            return 0, 0
        while(index < len(self.related)-1):
            if(heaviestWeight < self.related[index].weight):
                mostCommonIndex = index
                heaviestWeight = self.related[index].weight
            index = index + 1
        return self.related[mostCommonIndex], index      # return the club to the user

    def returnARelatedClub(self, index):
        newIndex = (index + 1) % len(self.related)
        return self.related[newIndex], newIndex
