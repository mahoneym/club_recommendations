from constants import DATE_FORMAT, SECOND_WINDOW_BACKGROUND, SECOND_WINDOW_FOREGROUND, SINGLE_LINE_LEFT_JUSTIFY, SECOND_WINDOW_WRAP
from tkinter import *

class UserEvents:
    """The Class for the User's Upcoming Events GUI"""

    # constructor for the User Events window
    # this will start the user event's window
    # param: a list of upcoming events (events objects) for a given user
    # returns: nothing
    def __init__(self, upcomingEventsList):
        __eventsList = Tk()
        __eventsList.configure(background=SECOND_WINDOW_BACKGROUND)
        __eventsList.wm_title("My Upcoming Events")

        index = 0
        rowsPerEvent = 6
        while(index < len(upcomingEventsList)):

            currentEvent = upcomingEventsList[index]
            name = Label(__eventsList, text= "Name: ", background=SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
            name.grid(row= (rowsPerEvent*index) + 1, column = 0, sticky = SINGLE_LINE_LEFT_JUSTIFY)

            club = Label(__eventsList, text= "Club: ", background=SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
            club.grid(row = (rowsPerEvent*index) +2, column = 0, sticky = SINGLE_LINE_LEFT_JUSTIFY)

            date = Label(__eventsList, text = "Date: ", background=SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
            date.grid(row = (rowsPerEvent*index) + 3, column = 0, sticky = SINGLE_LINE_LEFT_JUSTIFY)

            location = Label(__eventsList, text = "Location: ", background=SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
            location.grid(row = ((rowsPerEvent*index) +4), column = 0, sticky = SINGLE_LINE_LEFT_JUSTIFY)

            description = Label(__eventsList, text = "Description: ", background=SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
            description.grid(row = ((rowsPerEvent*index) +5), column = 0, sticky = SINGLE_LINE_LEFT_JUSTIFY)

            newName = Label(__eventsList, text = currentEvent.getName(), background=SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
            newName.grid(row = ((rowsPerEvent*index) + 1), column = 1, sticky = SINGLE_LINE_LEFT_JUSTIFY)

            newClub = Label(__eventsList, text = currentEvent.getClubHost().getClubName(), background=SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
            newClub.grid(row = ((rowsPerEvent*index)+2), column = 1, sticky = SINGLE_LINE_LEFT_JUSTIFY)

            newDate = Label(__eventsList, text = currentEvent.getDate().strftime(DATE_FORMAT), background=SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
            newDate.grid(row = ((rowsPerEvent*index)+3), column = 1, sticky = SINGLE_LINE_LEFT_JUSTIFY)

            newLocation = Label(__eventsList, text = currentEvent.getLocation(), background=SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
            newLocation.grid(row = ((rowsPerEvent*index)+4), column = 1, sticky = SINGLE_LINE_LEFT_JUSTIFY)

            newDescription = Label(__eventsList, text = currentEvent.getDescription(), background=SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND, wraplength = SECOND_WINDOW_WRAP, justify = LEFT)
            newDescription.grid(row = ((rowsPerEvent*index)+5), column = 1, sticky = SINGLE_LINE_LEFT_JUSTIFY)

            filler = Label(__eventsList, background=SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
            filler.grid(row=((rowsPerEvent*index)+rowsPerEvent), column = 1, sticky = SINGLE_LINE_LEFT_JUSTIFY)

            index = index + 1

        __eventsList.mainloop()
