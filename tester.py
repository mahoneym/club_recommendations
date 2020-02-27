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
    recommendObject.addClub("c1",'Games', 6)
    recommendObject.addClub("c2",'Sports', 7)
    recommendObject.addClub("c3",'Politics', 8)
    recommendObject.addClub("c4",'Fundraisers', 9)
    recommendObject.addClub("c5", 'English', 10)
    recommendObject.addClub("c7", 'English', 11)
    recommendObject.addClub("c8", 'English', 12)
    recommendObject.addClub("c9", 'English', 13)
    recommendObject.addClub("c10", 'English', 14)
    recommendObject.addClub("c11", "English", 15)
    recommendObject.addClub("c12", 'English', 16)
    recommendObject.addClub("c13", 'English', 17)
    recommendObject.addClub("c14", 'English', 18)
    recommendObject.addClub("c15", 'English', 19)
    recommendObject.addClub("c16", 'English', 20)
    recommendObject.addClub("c17", 'English', 21)
    recommendObject.addClub("c18", 'English', 22)
    recommendObject.addClub("c19", 'English', 23)
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
    global u6, u7, u8, u9, u10, u12, u13, u14, u15, u16, u17, u18, u19, u20, u21, u22, u23, u24
    addLargeClubs()

    u6.addClub("c1")
    u6.addClub("c2")
    u6.addClub("c3")

    u7.addClub("c2")
    u7.addClub("c3")
    u7.addClub("c4")

    u8.addClub("c1")
    u8.addClub("c3")
    u8.addClub("c4")

    u9.addClub("c2")
    u9.addClub("c4")
    u9.addClub("c5")

    u10.addClub("c5")
    u10.addClub("c6")
    u10.addClub("c7")

    u11.addClub("c6")
    u11.addClub("c7")
    u11.addClub("c8")

    u12.addClub("c8")
    u12.addClub("c12")
    u12.addClub("c9")

    u13.addClub("c12")
    u13.addClub("c16")
    u13.addClub("c15")

    u14.addClub("c8")
    u14.addClub("c12")
    u14.addClub("c13")

    u15.addClub("c8")
    u15.addClub("c1")
    u15.addClub("c18")

    u16.addClub("c8")
    u16.addClub("c19")
    u16.addClub("c1")

    u17.addClub("c19")
    u17.addClub("c2")
    u17.addClub("c10")

    u18.addClub("c5")
    u18.addClub("c13")
    u18.addClub("c19")

    u19.addClub("c17")
    u19.addClub("c18")
    u19.addClub("c14")

    u20.addClub("c13")
    u20.addClub("c14")
    u20.addClub("c17")

    u21.addClub("c16")
    u21.addClub("c17")
    u21.addClub("c18")

    u22.addClub("c11")
    u22.addClub("c12")
    u22.addClub("c13")

    u23.addClub("c13")
    u23.addClub("c14")
    u23.addClub("c18")

    u24.addClub("c8")
    u24.addClub("c10")
    u24.addClub("c12")

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
    print("Recommendation for user 101: " + c.destination.name)
    print("Should be: Not in it club")
    return None

recommendObject = recommender.Recommender()
miniDataSet()
smallDataSet()
#largeDataSet()
caseForNoRelated()

#checkNotReturningClubAlreadyIn()
