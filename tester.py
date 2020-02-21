import recommender

recommendObject = recommender.Recommender()

def addClubs():
    recommendObject.addClub('Computer Science Club', 'Academic', 1)
    recommendObject.addClub('Pep Band', 'Music', 2)
    recommendObject.addClub('Students For Life', 'Political', 3)
    return None

def createUsers():
    global u1
    global u2
    u1 = recommendObject.addUser(1)
    u2 = recommendObject.addUser(2)
    return None

def addUserClubs():
    u1.addClub('Pep Band', recommendObject)
    u1.addClub('Computer Science Club', recommendObject)
    #print("User 1:")
    #u1.print_userClubs()

    u2.addClub('Pep Band', recommendObject)
    u2.addClub('Students For Life', recommendObject)
    u2.addClub('Computer Science Club', recommendObject)
    #print("User 2:")
    #u2.print_userClubs()
    return None

def checkForConnectionBetweenClubs():
    recommendObject.print_clubs()
    return None

def main_1():
    addClubs()
    createUsers()
    addUserClubs()
    checkForConnectionBetweenClubs()
    return None

main_1()
