import clubs
import user

class Recommender:
    """The hub of activity for the project"""

    # these need to be instance variables i think => initialize here not in __init__()
    # i think if they aren't then how will I deal with them in user
    __users = []                   # a private dictionary of the students
    __clubs = []                   # a private dictionary of the created clubs

    # __users: id => ptr to user object
    # the __club: name => ptr to club object

    def __init__(self):
        # read in the data for users
        #self.__users                      # initiate to an empty array
        readUserData()
        # read in the data for clubs
        #self.__clubs                      # initiate to an empty array
        readClubData()
        return 0

    # create a user and add to the __user dictionary
    # param: student's ID
    # returns: 0
    def addUser(id):
        newUser = User(id, studentName)             # call __init__ of the user class
        __users.update({id: newUser})               # add the user to the dict
        return 0

    def addClub(clubName, clubCategory, clubID):
        newClub = Club(clubName, clubCategory, clubID)
        __clubs.update({clubName: newClub})     # do i need self.__clubs? i dk
        return 0

    # return the id of the club if it is found; o.w. return -1
    def getClub(clubName):
        for club in __clubs:
            if(clubName == club.name):
                return club                         # return the pointer to the club
        return -1                                   # something went wrong..

    def createUserRecommendations(id):
        # set recommendation to None (NULL) so it has the scope of the method
        recommendation = None
        # get user's node address
        for user in __users:
            if(user.id == id):
                # call findClub() in the user's object to get recommendations
                recommendation = user.findClub()
        return recommendation

    # the read data methods are taking it from excel spreadsheets
    def __readClubData():
        # open club information
        return 0

    def __readUserData():
        return 0
