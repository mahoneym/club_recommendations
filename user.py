from clubs.py import addRelated
from recommender.py import getClubPointer
import graph_edge.py
import random

class User:
    """Represents a student in the recommendation system"""
    clubs           # put graoh edge objects for the student's interests
    id              # a unique id for the user
    name            # student's full name

    def __init__(self, studentId, studentName):
        self.clubs = []
        self.id = studentId
        self.name = studentName

    def addClub(clubName):
        # check that the club isn't already being pointed to
        for club in clubs:                                  # loop through each of the clubs
            if (club.destination == clubName):              # check the graph_edge destinations to be the same as the parameter
                return -1                                   # Get out of here cause the club is already here..
        getClubPointer(clubName)                            # get a pointer to the club from recommender class
        newClub = graph_edge(a)                             # create a graph_edge object
        clubs.append(newClub)                               # append the graph_edge object to the clubs dictionary
        # make connections between clubs to the club I just added to this user
        return 0

    # pre-condition:
    def findClubs():
        # https://docs.python.org/3.8/library/random.html
        index = random.randrange(len(clubs)) # get random number
        index = index % len(clubs)           # mod it by the number of things in the clubs array
        # go to that club
        clubs[index].pointer
        # follow one of the pointers and get it back
        return 0

    def addUserData():
        # add a pointer to the new interests
        return 0
