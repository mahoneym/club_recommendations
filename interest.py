from graph_edge import *
import random

class Interest:
    """Represents an interest a freshman would fill in on
        the Road To/Thru Xavier Form"""

    def __init__(interestName):
        self.__name = interestName
        self.__relatedClubs = []

    def getInterestName(self):
        return self.__name

    def getRandomRecommendation():
        index = random.randint(0, 1000) % len(self.__relatedClubs)
        recommendation = self.__relatedClubs[index]
        return recommendation

    def addRelatedClub(club):
        self.__relatedClubs.append(club)
        return None
