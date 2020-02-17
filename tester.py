import recommender

def createUser1():
    recommendObject.addUser(1)
    recommendObject.print__users()
    print("Created user 1")
    return 0

recommendObject = recommender.Recommender()
createUser1()
