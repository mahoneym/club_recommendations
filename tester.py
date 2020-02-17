import recommender

def addSomeClubs(recommendObject):
    recommendObject.addClub('Computer Science Club', 'Academic', 1)
    recommendObject.addClub('Pep Band', 'Music', 2)
    recommendObject.print_clubs()
    return 0

def createUser1(recommendObject):
    recommendObject.addUser(1)
    recommendObject.print__users()
    print("Created user 1")
    return 0

def addUser1Clubs():
    return 0

def main():
    recommendObject = recommender.Recommender()
    addSomeClubs(recommendObject)
    print("added some clubs")
    createUser1(recommendObject)
    return None


main()
