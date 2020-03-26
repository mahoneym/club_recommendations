# ----------------------------- USER.PY ---------------------------------------
# This file contains a User class, which will represent each user of the system
# (or student). The User class tracks the user's ID number (as a way to identify
# each one) and keeps a list of the user's clubs. As a result, the class is
# able to addClubs and calls the methods to maintain the connections between clubs.

import clubs
from graph_edge import *
import random

class User:
    """Represents a student in the recommendation system"""

    def __init__(self, studentId):
        self.id = studentId                             # a unique id for the user => given by the data
        self.__userClubs = []                           # put graph edge objects for the student's interests
        self.__userInterests = []

    # goes through the clubs array and connects the index added and the other indices
    # pre-condition: assumes the item that needs to be connected is the last item in the clubs array
    # param: the index of the club that was added before this method
    # returns: 0
    def __makeConnectionsBetweenClubs(self, recommender):
        index = 0
        indexAdded = len(self.__userClubs) - 1
        while(index < len(self.__userClubs)):
            if (index != indexAdded):                                                       # make sure im not gonna connect the club with itself
                self.__userClubs[index].getDestination().addConnection(self.__userClubs[indexAdded].getDestination())       # from the already present club to the new one
                self.__userClubs[indexAdded].getDestination().addConnection(self.__userClubs[index].getDestination())       # from the new club to the already present club
            index = index + 1
        return 0

    # adds a club to the user's clubs array
    # param: the name of the club to be added
    # returns: 0 when the method finish
    def addClub(self, clubName, recommender):
        index = 0
        # check that the club isn't already in the list
        while(index < len(self.__userClubs)):               # loop through each of the clubs
            if (self.__alreadyInClub(clubName)):               # check the graph_edge destinations to be the same as the parameter
                return -1                                   # Get out of here cause the club is already here..
            index = index + 1

        club = recommender.getClub(clubName)                # get the club object that I need
        newClub = GraphEdge(club)                           # create a graph_edge object
        self.__userClubs.append(newClub)                    # append the graph_edge object to the clubs dictionary

        # add connections between the new club and the rest of the user's clubs
        self.__makeConnectionsBetweenClubs(recommender)
        return 0

    # checks to see if this user is in the given club clubName
    # param: the name of the club as a string
    # returns: True if the user is in the club; o.w. False
    def __alreadyInClub(self, clubName):
        for club in self.__userClubs:
            if(club.getDestination().getClubName() == clubName):
                return True
        return False

    def print_userClubs(self):
        for club in self.__userClubs:
            print(club.getDestination().getClubName())
            print(club.getWeight())

    # find club with highest weight to a random club that the user is in
    # param: None
    # returns: the club with the heaviest connection to the one chosen in this method
    def findClub(self):
        # go to a "random" club => random index of the user's clubs
        lengthOfClubs = len(self.__userClubs)
        club = 0
        count = 0
        foundInUser = True
        index = random.randint(0, 1000)
        while(club == 0 and foundInUser):
            index = (index + 1) % lengthOfClubs
            usingClubToRecommend = self.__userClubs[index].getDestination()
            # use club index to call the most common club method on club's object
            club, firstIndexUsed = usingClubToRecommend.returnMostCommonClub(-1)
            if(club != 0):
                foundInUser = self.__alreadyInClub(club.getDestination().getClubName())
                indexUsed = -1
                while(foundInUser and (indexUsed != firstIndexUsed)):
                    club, indexUsed = usingClubToRecommend.returnARelatedClub(indexUsed)
                    foundInUser = self.__alreadyInClub(club.getDestination().getClubName())
                    # if the club was found
                    if(foundInUser):
                        #reset the club to nothing to use the user's next club for a recommendation
                        club = 0

            count = count + 1

            # if there are no related clubs and we have tried 5 times
            if(count == 5 and club == 0):
                club = None             # set club to none so we stop trying

        return club

    # adds an interest to the user
    # param: takes the self and the interest object to be added
    # returns: nothing
    def addInterest(self, interest):
        self.__userInterests.append(interest)
        return None

    def getUserInterest(self):
        index = random.randint(0, 1000) % len(self.__userInterests)
        return self.__userInterests[index]

    # checks if the user is already in the given club
    # param: the club object that is being checked for
    # return: True if the user is in the club; o.w. False
    def checkForClub(self, club):
        flag = False
        for oneClub in self.__userClubs:
            if(oneClub.getDestination() == club):
                flag = True
        return flag

    def getInterestRecommendation(self):
        foundOne = False
        recommendation = None
        while(foundOne == False and len(self.__userInterests) > 0):
            index = random.randint(0, 1000) % (len(self.__userInterests)-1)
            interest = self.__userInterests[index]
            recommendation = interest.getRandomRecommendation()
            flag = self.checkForClub(recommendation)
            foundOne = (not flag)
        return recommendation
