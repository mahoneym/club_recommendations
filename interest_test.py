import recommender

recommend = recommender.Recommender()

u1 = recommend.addUser(1)
u2 = recommend.addUser(2)
u3 = recommend.addUser(3)
u4 = recommend.addUser(4)
u5 = recommend.addUser(5)

u1.addClub('MuskieTHON', recommend)
u1.addClub('Computer Science Club', recommend)
u1.addClub("Accounting Society", recommend)

u2.addClub('MuskieTHON', recommend)
u2.addClub('A Xavier Christmas', recommend)
u2.addClub('Computer Science Club', recommend)

u3.addClub('A Xavier Christmas', recommend)
u3.addClub('4 Paws for Ability at XU', recommend)
u3.addClub("Don't Tell Anna", recommend)

u4.addClub('A Xavier Christmas', recommend)
u4.addClub("Don't Tell Anna", recommend)
u4.addClub('MuskieTHON', recommend)

u5.addClub("Computer Science Club", recommend)
u5.addClub("Don't Tell Anna", recommend)
u5.addClub('A Xavier Christmas', recommend)

recommend.addUserInterest(1, "STEM")
#recommend.createInterestRecommendation(1)
print(str(recommend.createInterestRecommendation(1).getClubName()))
#print(u1.getUserInterest().getInterestName())
