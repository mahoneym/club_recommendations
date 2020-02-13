import clubs.py
import user.py

class Recommender:
    """The hub of activity in the project"""

    # these need to be instance variables i think
    # i think if they aren't then how will I deal with them in user
    __users                   # a private dictionary of the students
    __clubs                   # a private dictionary of the created clubs

    # __users: id => ptr to user object
    # the __club: name => ptr to club object

    def __init__(self):
        # read in the data for users
        __users = []                      # initiate to an empty array
        readUserData()
        # read in the data for clubs
        __clubs = []                      # initiate to an empty array
        readClubData()
        return 0

    def addUser(id, studentName):
        # call __init__ of the user class
        newUser = User(id, studentName)
        ptr = id(newUser)
        __users.update({id: ptr})
        return 0

    # return the id of the club if it is found; o.w. return -1
    def getClubPointer(clubName):
        for club in __clubs:
            if(clubName == club.name):
                return id(club)                     # return the pointer to the club
        return -1

    def createUserRecommendations():
        recommendations = []
        # get user's node address
        for user in __users:
            # call findClub() in the user's object to get 3 recommendations
            recommendations = user.findClub()
        return recommendations

    # the read data methods are taking it from excel spreadsheets
    def __readClubData():
        # open club information
        return 0

    def __readUserData():
        return 0
