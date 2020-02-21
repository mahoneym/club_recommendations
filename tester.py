import recommender

def addMiniClubs():
    recommendObject.addClub('Computer Science Club', 'Academic', 1)
    recommendObject.addClub('Pep Band', 'Music', 2)
    recommendObject.addClub('A Xavier Christmas', 'Service', 3)
    return None

def addSmallClubs():
    recommendObject.addClub("Don't Tell Anna", 'Service', 4)
    recommendObject.addClub('4 Paws for Ability', 'Animals', 5)
    return None

def addMediumClubs():
    return None

def miniDataSet():
    global u1, u2
    addMiniClubs()

    u1 = recommendObject.addUser(1)
    u2 = recommendObject.addUser(2)

    u1.addClub('Pep Band', recommendObject)
    u1.addClub('Computer Science Club', recommendObject)

    u2.addClub('Pep Band', recommendObject)
    u2.addClub('A Xavier Christmas', recommendObject)
    u2.addClub('Computer Science Club', recommendObject)

    miniRecommendations()
    return None

def smallDataSet():
    global u3, u4, u5
    addSmallClubs()

    u3 = recommendObject.addUser(3)
    u4 = recommendObject.addUser(4)
    u5 = recommendObject.addUser(5)

    u3.addClub('A Xavier Christmas', recommendObject)
    u3.addClub('4 Paws for Ability', recommendObject)
    u3.addClub("Don't Tell Anna", recommendObject)

    u4.addClub('A Xavier Christmas', recommendObject)
    u4.addClub("Don't Tell Anna", recommendObject)
    u4.addClub('Pep Band', recommendObject)

    u5.addClub("Computer Science Club", recommendObject)
    u5.addClub("Don't Tell Anna", recommendObject)
    u5.addClub('A Xavier Christmas', recommendObject)

    smallRecommendations()
    return None

def mediumDataSet():
    return None

def miniRecommendations():
    print("Mini Recommendations: \n")
    a = recommendObject.createUserRecommendations(1)
    print("recommendation for user 1: " + a.destination.name + '\n')

    b = recommendObject.createUserRecommendations(2)
    print("recommendation for user 2: " + b.destination.name + '\n')
    return None

def smallRecommendations():
    print("Small Recommendations: \n")
    a = recommendObject.createUserRecommendations(3)
    print("recommendation for user 3: " + a.destination.name + '\n')

    b = recommendObject.createUserRecommendations(4)
    print("recommendation for user 2: " + b.destination.name)
    return None

def mediumRecommendations():
    return None

recommendObject = recommender.Recommender()
miniDataSet()
smallDataSet()
