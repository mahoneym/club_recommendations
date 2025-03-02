####### CLUB_TEST.PY #######
####### This tests clubs being added to the recommender and the connections between the clubs #######
####### The file also tests the recommendations- makes sure the recommendations are not redundant to the user #######

import recommender

def addMiniClubs():
    recommendObject.addClub('Computer Science Club', 'Academic', 1,"")
    recommendObject.addClub('Pep Band', 'Music', 2,"")
    recommendObject.addClub('A Xavier Christmas', 'Service', 3,"")
    recommendObject.addClub('Accounting Club', 'Academic', 24,"")
    return None

def addSmallClubs():
    recommendObject.addClub("Don't Tell Anna", 'Service', 4, "")
    recommendObject.addClub('4 Paws for Ability', 'Animals', 5,"")
    return None

def addLargeClubs():
    recommendObject.addClub("c1",'Games', 6,"")
    recommendObject.addClub("c2",'Sports', 7,"")
    recommendObject.addClub("c3",'Politics', 8,"")
    recommendObject.addClub("c4",'Fundraisers', 9,"")
    recommendObject.addClub("c5", 'English', 10,"")
    recommendObject.addClub("c6", 'English', 10,"")
    recommendObject.addClub("c7", 'English', 11,"")
    recommendObject.addClub("c8", 'English', 12,"")
    recommendObject.addClub("c9", 'English', 13,"")
    recommendObject.addClub("c10", 'English', 14,"")
    recommendObject.addClub("c11", "English", 15,"")
    recommendObject.addClub("c12", 'English', 16,"")
    recommendObject.addClub("c13", 'English', 17,"")
    recommendObject.addClub("c14", 'English', 18,"")
    recommendObject.addClub("c15", 'English', 19,"")
    recommendObject.addClub("c16", 'English', 20,"")
    recommendObject.addClub("c17", 'English', 21,"")
    recommendObject.addClub("c18", 'English', 22,"")
    recommendObject.addClub("c19", 'English', 23,"")
    return None

def miniDataSet():
    global u1, u2
    addMiniClubs()

    u1 = recommendObject.addUser(1)
    u2 = recommendObject.addUser(2)

    u1.addClub('Pep Band', recommendObject)
    u1.addClub('Computer Science Club', recommendObject)
    u1.addClub("Accounting Club", recommendObject)

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
    global u6, u7, u8, u9, u10, u12, u13, u14, u15, u16, u17, u18, u19, u20, u21, u22, u23, u25, u24
    addLargeClubs()

    u6 = recommendObject.addUser(6)
    u7 = recommendObject.addUser(7)
    u8 = recommendObject.addUser(8)
    u9 = recommendObject.addUser(9)
    u10 = recommendObject.addUser(10)
    u12 = recommendObject.addUser(12)
    u13 = recommendObject.addUser(13)
    u14 = recommendObject.addUser(14)
    u15 = recommendObject.addUser(15)
    u16 = recommendObject.addUser(16)
    u17 = recommendObject.addUser(17)
    u18 = recommendObject.addUser(18)
    u19 = recommendObject.addUser(19)
    u20 = recommendObject.addUser(20)
    u21 = recommendObject.addUser(21)
    u22 = recommendObject.addUser(22)
    u23 = recommendObject.addUser(23)
    u24 = recommendObject.addUser(24)
    u25 = recommendObject.addUser(25)

    u6.addClub("c1", recommendObject)
    u6.addClub("c2", recommendObject)
    u6.addClub("c3", recommendObject)

    u7.addClub("c2", recommendObject)
    u7.addClub("c3", recommendObject)
    u7.addClub("c4", recommendObject)

    u8.addClub("c1", recommendObject)
    u8.addClub("c3", recommendObject)
    u8.addClub("c4", recommendObject)

    u9.addClub("c2", recommendObject)
    u9.addClub("c4", recommendObject)
    u9.addClub("c5", recommendObject)

    u10.addClub("c5", recommendObject)
    u10.addClub("c6", recommendObject)
    u10.addClub("c7", recommendObject)

    u12.addClub("c6", recommendObject)
    u12.addClub("c7", recommendObject)
    u12.addClub("c8", recommendObject)

    u13.addClub("c8", recommendObject)
    u13.addClub("c12", recommendObject)
    u13.addClub("c9", recommendObject)

    u14.addClub("c12", recommendObject)
    u14.addClub("c16", recommendObject)
    u14.addClub("c15", recommendObject)

    u15.addClub("c8", recommendObject)
    u15.addClub("c12", recommendObject)
    u15.addClub("c13", recommendObject)

    u16.addClub("c8", recommendObject)
    u16.addClub("c1", recommendObject)
    u16.addClub("c18", recommendObject)

    u17.addClub("c8", recommendObject)
    u17.addClub("c19", recommendObject)
    u17.addClub("c1", recommendObject)

    u18.addClub("c19", recommendObject)
    u18.addClub("c2", recommendObject)
    u18.addClub("c10", recommendObject)

    u19.addClub("c5", recommendObject)
    u19.addClub("c13", recommendObject)
    u19.addClub("c19", recommendObject)

    u20.addClub("c17", recommendObject)
    u20.addClub("c18", recommendObject)
    u20.addClub("c14", recommendObject)

    u21.addClub("c13", recommendObject)
    u21.addClub("c14", recommendObject)
    u21.addClub("c17", recommendObject)

    u22.addClub("c16", recommendObject)
    u22.addClub("c17", recommendObject)
    u22.addClub("c18", recommendObject)

    u23.addClub("c11", recommendObject)
    u23.addClub("c12", recommendObject)
    u23.addClub("c13", recommendObject)

    u24.addClub("c13", recommendObject)
    u24.addClub("c14", recommendObject)
    u24.addClub("c18", recommendObject)

    u25.addClub("c8", recommendObject)
    u25.addClub("c10", recommendObject)
    u25.addClub("c12", recommendObject)

    largeRecommendations()

    return None

def miniRecommendations():
    print("\n" + "Mini Recommendations:")
    a = recommendObject.createClubRecommendation(1)
    #print("recommendation for user 1: " + a.getDestination().getClubName())
    assert(a.getDestination().getClubName() != 'Pep Band')
    assert(a.getDestination().getClubName() != 'Computer Science Club')
    assert(a.getDestination().getClubName() != 'Accounting Club')

    b = recommendObject.createClubRecommendation(2)
    #print("recommendation for user 2: " + b.getDestination().getClubName())
    assert(b.getDestination().getClubName() != 'Pep Band')
    assert(b.getDestination().getClubName() != 'A Xavier Christmas')
    assert(b.getDestination().getClubName() != 'Computer Science Club')

    print("Mini recommendations passed")
    return None

def smallRecommendations():
    print("\n" + "Small Recommendations:")
    a = recommendObject.createClubRecommendation(3)
    #cleprint("recommendation for user 3: " + a.getDestination().getClubName())
    assert(a.getDestination().getClubName() != 'A Xavier Christmas')
    assert(a.getDestination().getClubName() != '4 Paws for Ability')
    assert(a.getDestination().getClubName() != "Don't Tell Anna")

    b = recommendObject.createClubRecommendation(4)
    #print("recommendation for user 4: " + b.getDestination().getClubName())
    assert(b.getDestination().getClubName() != "Don't Tell Anna")
    assert(b.getDestination().getClubName() != "Pep Band")
    assert(a.getDestination().getClubName() != "A Xavier Christmas")

    print("Small recommendations passed")
    return None

def largeRecommendations():
    print("\n" + "Large recommendations:")
    a = recommendObject.createClubRecommendation(6)
    assert(a.getDestination().getClubName() != "c1")
    assert(a.getDestination().getClubName() != "c2")
    assert(a.getDestination().getClubName() != "c3")

    b = recommendObject.createClubRecommendation(7)
    assert(b.getDestination().getClubName() != "c2")
    assert(b.getDestination().getClubName() != "c3")
    assert(b.getDestination().getClubName() != "c4")

    c = recommendObject.createClubRecommendation(8)
    assert(c.getDestination().getClubName() != "c1")
    assert(c.getDestination().getClubName() != "c3")
    assert(c.getDestination().getClubName() != "c4")

    d = recommendObject.createClubRecommendation(9)
    assert(d.getDestination().getClubName() != "c2")
    assert(d.getDestination().getClubName() != "c4")
    assert(d.getDestination().getClubName() != "c5")

    a = recommendObject.createClubRecommendation(10)
    assert(a.getDestination().getClubName() != "c5")
    assert(a.getDestination().getClubName() != "c6")
    assert(a.getDestination().getClubName() != "c7")

    b = recommendObject.createClubRecommendation(12)
    assert(b.getDestination().getClubName() != "c6")
    assert(b.getDestination().getClubName() != "c7")
    assert(b.getDestination().getClubName() != "c8")

    c = recommendObject.createClubRecommendation(13)
    assert(c.getDestination().getClubName() != "c8")
    assert(c.getDestination().getClubName() != "c12")
    assert(c.getDestination().getClubName() != "c9")

    d = recommendObject.createClubRecommendation(14)
    assert(d.getDestination().getClubName() != "c12")
    assert(d.getDestination().getClubName() != "c16")
    assert(d.getDestination().getClubName() != "c15")

    a = recommendObject.createClubRecommendation(15)
    assert(a.getDestination().getClubName() != "c8")
    assert(a.getDestination().getClubName() != "c12")
    assert(a.getDestination().getClubName() != "c13")

    b = recommendObject.createClubRecommendation(16)
    assert(b.getDestination().getClubName() != "c8")
    assert(b.getDestination().getClubName() != "c1")
    assert(b.getDestination().getClubName() != "c18")

    c = recommendObject.createClubRecommendation(17)
    assert(c.getDestination().getClubName() != "c8")
    assert(c.getDestination().getClubName() != "c19")
    assert(c.getDestination().getClubName() != "c1")

    d = recommendObject.createClubRecommendation(18)
    assert(d.getDestination().getClubName() != "c19")
    assert(d.getDestination().getClubName() != "c2")
    assert(d.getDestination().getClubName() != "c10")

    a = recommendObject.createClubRecommendation(19)
    assert(a.getDestination().getClubName() != "c5")
    assert(a.getDestination().getClubName() != "c13")
    assert(a.getDestination().getClubName() != "c19")

    b = recommendObject.createClubRecommendation(20)
    assert(b.getDestination().getClubName() != "c17")
    assert(b.getDestination().getClubName() != "c18")
    assert(b.getDestination().getClubName() != "c14")

    c = recommendObject.createClubRecommendation(21)
    assert(c.getDestination().getClubName() != "c13")
    assert(c.getDestination().getClubName() != "c14")
    assert(c.getDestination().getClubName() != "c17")

    d = recommendObject.createClubRecommendation(22)
    assert(d.getDestination().getClubName() != "c16")
    assert(d.getDestination().getClubName() != "c17")
    assert(d.getDestination().getClubName() != "c18")

    c = recommendObject.createClubRecommendation(23)
    assert(c.getDestination().getClubName() != "c11")
    assert(c.getDestination().getClubName() != "c12")
    assert(c.getDestination().getClubName() != "c13")

    d = recommendObject.createClubRecommendation(24)
    assert(d.getDestination().getClubName() != "c13")
    assert(d.getDestination().getClubName() != "c14")
    assert(d.getDestination().getClubName() != "c18")

    d = recommendObject.createClubRecommendation(25)
    assert(d.getDestination().getClubName() != "c8")
    assert(d.getDestination().getClubName() != "c10")
    assert(d.getDestination().getClubName() != "c12")

    print("Large recommendations passed")
    return None

def caseForNoRelated():
    print("\n" + "A club having no related clubs")

    recommendObject.addClub("Lone Club", 'Test Case', 0,"")

    u0 = recommendObject.addUser(11)

    u0.addClub("Lone Club", recommendObject)

    c = recommendObject.createClubRecommendation(11)
    assert(c == None)
    print("The assertion passed")
    return None

def checkNotReturningClubAlreadyIn():
    print("\n" + "Not recommending a club the user is already in")

    u101 = recommendObject.addUser(101)
    u102 = recommendObject.addUser(102)

    a = recommendObject.addClub('Common Club', 'something', 2,"")
    b = recommendObject.addClub('Not in it club', 'something', 3,"")
    c = recommendObject.addClub("Random Other Club", 'something', 4,"")

    u101.addClub("Common Club", recommendObject)
    u101.addClub("Random Other Club", recommendObject)

    u102.addClub("Common Club", recommendObject)
    u102.addClub("Not in it club", recommendObject)
    u102.addClub("Random Other Club", recommendObject)

    c = recommendObject.createClubRecommendation(101)
    assert(c.getDestination().getClubName() == "Not in it club")
    print("The assertion passed")
    return None

def tryAddingExcelClubs():
    recommendObject.addExcelClubs()
    print("Added the clubs from excel")
    return None

def clubBasedTests():
    miniDataSet()
    smallDataSet()
    largeDataSet()
    caseForNoRelated()
    checkNotReturningClubAlreadyIn()
    return 0

recommendObject = recommender.Recommender()
clubBasedTests()
