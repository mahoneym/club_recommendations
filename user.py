import clubs
import recommender
import graph_edge
import random

class User:
    """Represents a student in the recommendation system"""
    clubs           # put graph edge objects for the student's interests
    id              # a unique id for the user

    def __init__(self, studentId):
        self.clubs = []
        self.id = studentId

    def addClub(clubName):
        index = 0
        # check that the club isn't already being pointed to
        while(index < len(clubs)):                                  # loop through each of the clubs
            if (club.destination == clubName):                      # check the graph_edge destinations to be the same as the parameter
                return -1                                           # Get out of here cause the club is already here..
            index = index + 1
        # a = getClubPointer(clubName)                              # get a pointer to the club from recommender class
        # clubs[index].destination will be the club
        newClub = graph_edge(clubs[index].destination)              # create a graph_edge object
        clubs.append(newClub)                                       # append the graph_edge object to the clubs dictionary

        clubs[index].makeConnectionsBetweenClubs(clubs, index)
        return 0

    def findClub():
        # find club with highest weight
        index = 0
        # set maxIndex and weight to a negative number
        # so we will know if something messed up
        maxIndex = -1
        maxWeight = -1
        while(index < len(clubs)):
            if club.weight > maxWeight:
                maxIndex = index
                maxWeight = club.Weight
            index = index + 1
        # follow the club index to the club's actual object to get recommendation
        return clubs[index].destination.returnMostCommonClub()

    def addUserData():
        # add a pointer to the new interests
        return 0
