# club_recommendations

  This repository is my senior project. I am developing it on MacOS, and the commands included will be for the Mac terminal. This repository is a club recommendation system, which will help students to find clubs based on the clubs in which the user is already participating and their interests. 
  To do this for club recommendations, I am using a weighted graph. The users track their clubs, and these connections are not weighted. On the other hand, the clubs have connections between them. The weight of these connections is the number of common members between the two clubs. If two clubs have zero members in common, there will not be an edge between the two clubs.
    When making a club-based recommendation, the system will go to one of the user's clubs (based on a random number). Then, the program will look for the heaviest connection between clubs which leaves the chosen club. If the user is already in this club, the recommender will not return this club to the user and will look for another one.
  For interest recommendations, each user will keep track of its interests. The interests will point to all the clubs which are related to that interest. For interest recommendations, two random numbers will pick which user interest to use and which club to recommend based on the user's interest.
  The system also keeps track of events for each club. Because of this, upcoming events can be given for each of the recommended clubs or for the user's clubs. 
  To build the system, I am using Python3. In order to run the test program, which was built during development to make sure the system is working as expected, I navigate to the project's main directory, club_recommendations and use 'python3 event_test.py', 'python3 interest_test.py', and 'python3 clubs_test.py' in the terminal. This will run the tests that I have written for the different parts of the system and will print some results after the file runs. 
  A graphical user interface [GUI] is also available for this recommendation system. Similar to the test program, I navigate to the project's directory and use 'python3 application.py' in the terminal. Another window should come up, where an entry box will come up. Student id's 1-4 have clubs and interests already entered into the system, and student 5 has clubs in the system. Any other user ID will cause an error message. As you will see, there is an admin button, which allows the admin user to add events to clubs. In order to access the admin section, enter "Admin" into the student id box. The other buttons will cause error messages with this in the student id box. 
  From the GUI, a user can get a club-based recommendation or an interest-based recommendation. The user can get an upcoming event for any club which is recommended if there is one in the system. The user can also get their upcoming events for their clubs.
