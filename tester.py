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

def addLargeClubs():
    recommendObject.addClub("Child's Play",'Games', 6)
    recommendObject.addClub("Club Sports",'Sports', 7)
    recommendObject.addClub("Network of Enlightened Women",'Politics', 8)
    recommendObject.addClub("MuskieTHON",'Fundraisers', 9)
    recommendObject.addClub("Newswire", 'English', 10)
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

def largeDataSet():
    global u6, u7, u8, u9, u10, u12, u13, u14, u15, u16, u17, u18, u19, u20
    addLargeClubs()

    u1.addClub("Child's Play", recommendObject)

    #u6.addClub()

    #u7.addClub()

    #u8.addClub()

    #u9.addClub()

    #u10.addClub()

    largeRecommendations()

    return None

def miniRecommendations():
    print("\n" + "Mini Recommendations:")
    a = recommendObject.createUserRecommendations(1)
    print("recommendation for user 1: " + a.destination.name + '\n')

    b = recommendObject.createUserRecommendations(2)
    print("recommendation for user 2: " + b.destination.name + '\n')
    return None

def smallRecommendations():
    print("\n" + "Small Recommendations:")
    a = recommendObject.createUserRecommendations(3)
    print("recommendation for user 3: " + a.destination.name + '\n')

    b = recommendObject.createUserRecommendations(4)
    print("recommendation for user 2: " + b.destination.name)
    return None

def largeRecommendations():
    print("\n" + "Large recommendations:")
    return None

def caseForNoRelated():
    print("\n" + "A club having no related clubs")

    recommendObject.addClub("Lone Club", 'Test Case', 0)

    u0 = recommendObject.addUser(11)

    u0.addClub("Lone Club", recommendObject)

    c = recommendObject.createUserRecommendations(11)
    assert(c == None)
    print("Success! The assertion passed!")
    return None

def checkNotReturningClubAlreadyIn():
    print("\n" + "Not recommending a club the user is already in")

    u101 = recommendObject.addUser(101)
    u102 = recommendObject.addUser(102)
    u103 = recommendObject.addUser(103)

    a = recommendObject.addClub('Common Club', 'something', 2)
    b = recommendObject.addClub('Not in it club', 'something', 3)
    c = recommendObject.addClub("Random Other Club", 'something', 4)

    u101.addClub("Common Club", recommendObject)
    u101.addClub("Random Other Club", recommendObject)

    u102.addClub("Common Club", recommendObject)
    u102.addClub("Not in it club", recommendObject)
    u102.addClub("Random Other Club", recommendObject)

    c = recommendObject.createUserRecommendations(101)
    print("Recommendation: " + c.destination.name)
    return None

recommendObject = recommender.Recommender()
#miniDataSet()
#smallDataSet()
#largeDataSet()
caseForNoRelated()

checkNotReturningClubAlreadyIn()
