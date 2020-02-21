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

    u2.addClub('Pep Band', recommendObject)
    u2.addClub('Students For Life', recommendObject)
    u2.addClub('Computer Science Club', recommendObject)
    return None

def checkForConnectionBetweenClubs():
    recommendObject.print_clubs()
    return None

def main_1():
    addClubs()
    createUsers()
    addUserClubs()
    #checkForConnectionBetweenClubs()
    a = recommendObject.createUserRecommendations(1)
    print("recommendation for user 1: " + a.destination.name + '\n')

    b = recommendObject.createUserRecommendations(2)
    print("recommendation for user 2: " + b.destination.name)
    return None

main_1()
