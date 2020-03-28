from graph_edge import *
import random

class Interest:
    """Represents an interest a freshman would fill in on
        the Road To/Thru Xavier Form"""

    # constructor for the interest class
    def __init__(self, interestName):
        self.__name = interestName
        self.__relatedClubs = []

    # returns the interest name to the caller
    def getInterestName(self):
        return self.__name

    # prints the clubs in the interest
    def printClubsInCategory(self):
        for club in self.__relatedClubs:
            print(club.getClubName())

    # returns a random club based on the random number
    # param: None
    # returns: a club object
    def getRandomRecommendation(self):
        index = random.randint(0, 1000) % len(self.__relatedClubs)
        recommendation = self.__relatedClubs[index]
        return recommendation

    # adds a club to the interest's related list
    # param: the club to link
    # return: None
    def addRelatedClub(self, club):
        self.__relatedClubs.append(club)
        return None
