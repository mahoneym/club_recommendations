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

    # goes through the clubs array and connects the index added and the other indices
    # pre-condition: assumes the item that needs to be connected is the last item in the clubs array
    # param: the index of the club that was added before this method
    # returns: 0
    def makeConnectionsBetweenClubs(self, recommender):
        index = 0
        indexAdded = len(self.__userClubs) - 1
        while(index < len(self.__userClubs)):
            if (index != indexAdded):                                                       # make sure im not gonna connect the club with itself
                self.__userClubs[index].destination.addConnection(self.__userClubs[indexAdded].destination)       # from the already present club to the new one
                self.__userClubs[indexAdded].destination.addConnection(self.__userClubs[index].destination)       # from the new club to the already present club
            index = index + 1
        return 0

    # adds a club to the user's clubs array
    # param: the name of the club to be added
    # returns: 0 when the method finish
    def addClub(self, clubName, recommender):
        index = 0
        # check that the club isn't already in the list
        while(index < len(self.__userClubs)):               # loop through each of the clubs
            if (self.alreadyInClub(clubName)):               # check the graph_edge destinations to be the same as the parameter
                return -1                                   # Get out of here cause the club is already here..
            index = index + 1

        club = recommender.getClub(clubName)                # get the club object that I need
        newClub = GraphEdge(club)                           # create a graph_edge object
        self.__userClubs.append(newClub)                    # append the graph_edge object to the clubs dictionary

        # add connections between the new club and the rest of the user's clubs
        self.makeConnectionsBetweenClubs(recommender)
        return 0

    def alreadyInClub(self, clubName):
        for club in self.__userClubs:
            if(club.destination.name == clubName):
                return True
        return False

    def print_userClubs(self):
        for club in self.__userClubs:
            print(club.destination.name)
            print(club.weight)

    # find club with highest weight to a random club that the user is in
    # NOTE: THIS COULD RETURN A CLUB THE USER IS ALREADY IN
    # param: None
    # returns: the club with the heaviest connection to the one chosen in this method
    def findClub(self):
        # go to a "random" club => random index of the user's clubs
        lengthOfClubs = len(self.__userClubs)
        club = 0
        count = 0
        foundInUser = False
        while(club == 0 or foundInUser == True):
            index = random.randint(0, 1000) % lengthOfClubs        # this might return numberOfItems
            usingClubToRecommend = self.__userClubs[index].destination
            print("Going to " + usingClubToRecommend.name)
            # use club index to call the most common club method on club's object
            club = usingClubToRecommend.returnMostCommonClub()
            if(club != 0):
                foundInUser = self.alreadyInClub(club.destination.name)
            count = count + 1

            # if there are no related clubs and we have tried 5 times
            if(count == 5 and club == 0):
                club = None         # set club to none so we stop trying
        return club
