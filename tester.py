import recommender

recommendObject = recommender.Recommender()

def addSomeClubs():
    recommendObject.addClub('Computer Science Club', 'Academic', 1)
    recommendObject.addClub('Pep Band', 'Music', 2)
    return None

def createUser1():
    global u1
    u1 = recommendObject.addUser(1)
    recommendObject.print_users()
    print("Created user 1")
    return None

def addUser1Clubs():
    u1.addClub('Pep Band', recommendObject)
    u1.print_userClubs()
    return None

def main_1():
    #recommendObject = recommender.Recommender()
    addSomeClubs()
    print("added some clubs")
    # works to here..
    createUser1()
    addUser1Clubs()                     # this is causing problems
    # PEP BAND IS THERE!!!
    a = u1.checkForClub('Pep Band')
    print (a)
    return None

main_1()
