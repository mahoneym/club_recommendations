####### INTEREST_TEST.PY #######
####### This tests adding interests to the user and getting recommendations from it #######

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
recommend.addUserInterest(1, "General Interests")
recommend.addUserInterest(1, "Spirituality")

u1Recommendation = recommend.createInterestRecommendation(1)
assert(u1Recommendation.getClubName() != "MuskieTHON")
assert(u1Recommendation.getClubName() != "Computer Science Club")
assert(u1Recommendation.getClubName() != "Accounting Society")

recommend.addUserInterest(2, "Health Professions")
recommend.addUserInterest(2, "Wellness")
recommend.addUserInterest(2, "Service and Social Justice")

u2Recommendation = recommend.createInterestRecommendation(2)
assert(u2Recommendation.getClubName() != "MuskieTHON")
assert(u2Recommendation.getClubName() != "A Xavier Christmas")
assert(u2Recommendation.getClubName() != "Computer Science Club")

recommend.addUserInterest(3, "STEM")
recommend.addUserInterest(3, "General Interests")
recommend.addUserInterest(3, "Wellness")

u3Recommendation = recommend.createInterestRecommendation(3)
assert(u3Recommendation.getClubName() != "A Xavier Christmas")
assert(u3Recommendation.getClubName() != "4 Paws for Ability at XU")
assert(u3Recommendation.getClubName() != "Don't Tell Area")

recommend.addUserInterest(4, "Service & Social Justice")
recommend.addUserInterest(4, "Spirituality")
recommend.addUserInterest(4, "STEM")

u4Recommendation = recommend.createInterestRecommendation(4)
assert(u4Recommendation.getClubName() != "A Xavier Christmas")
assert(u4Recommendation.getClubName() != "Don't Tell Anna")
assert(u4Recommendation.getClubName() != "MuskieTHON")

#recommend.createInterestRecommendation(1)
print("user 1: " + str(u1Recommendation.getClubName()))
print("user 2: " + str(u2Recommendation.getClubName()))
print("user 3: " + str(u3Recommendation.getClubName()))
print("user 4: " + str(u4Recommendation.getClubName()))
