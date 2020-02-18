#import clubs
#import recommender

def addSomeClubs():
    import clubs
    clubs.addClub('Computer Science Club', 'Academic', 1)
    clubs.addClub('Pep Band', 'Music', 2)
    #recommendObject.print_clubs()
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
    import recommender
    recommendObject = recommender.Recommender()
    addSomeClubs(recommendObject)
    print("added some clubs")
    createUser1(recommendObject)
    addUser1Clubs()                     # this is causing problems
    #a = u1.checkForClub('Pep Band')
    #print (a)
    return None

#main_1()
addSomeClubs()
