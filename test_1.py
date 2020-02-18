import recommender
#import clubs

def addSomeClubs():
    #import clubs
    clubs.Club('Computer Science Club', 'Academic', 1)
    clubs.print_clubs()
    #clubs.Club('Pep Band', 'Music', 2)
    return None

def createUser1(recommendObject):
    global u1
    u1 = recommendObject.addUser(1)
    #recommendObject.print__users()
    print("Created user 1")
    return None

def addUser1Clubs():
    u1.addClub('Pep Band')
    return None

def main_1():
    recommendObject = recommender.Recommender()
    #addSomeClubs()
    print("added some clubs")
    createUser1(recommendObject)
    #addUser1Clubs()                     # this is causing problems
    #a = u1.checkForClub('Pep Band')
    #print (a)
    return None

main_1()
#addSomeClubs()
