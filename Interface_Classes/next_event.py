####### next_event.py #######
####### The NextEvent class starts the next event window #######

from constants import TOP_RIGHT_CORNER, SECOND_WINDOW_BACKGROUND, SECOND_WINDOW_FOREGROUND, SINGLE_LINE_LEFT_JUSTIFY, SECOND_WINDOW_WRAP
from tkinter import *

class NextEvent():
    """The GUI Class for a Club's Upcoming Event"""

    # the constructor for the NextEvent window
    # THIS WILL START THE NEXT EVENT WINODW
    # param: the event's: title (string), date (datetime), location (string), description (string)
    # returns: nothing
    def __init__(self, nextEventTitle, nextEventDate, nextEventLocation, nextEventDescription):
        __eventPopUp = Tk()

        # set up the pop up window
        __eventPopUp.wm_title("Next Event")
        __eventPopUp.configure(background = SECOND_WINDOW_BACKGROUND)                                                  # sets background color to midnight blue

        __title = Label(__eventPopUp, text = "Event Title: ", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __title.grid(row = 0, column = 0, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __date = Label(__eventPopUp, text = "Event Date", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __date.grid(row = 1, column = 0, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __location = Label(__eventPopUp, text = "Event Location: ", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __location.grid(row = 2, column = 0, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __description = Label(__eventPopUp, text = "Event Description", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __description.grid(row = 3, column = 0, sticky= TOP_RIGHT_CORNER)

        __eventTitle = Label(__eventPopUp, text = nextEventTitle, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __eventTitle.grid(row = 0, column = 1, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __eventDate = Label(__eventPopUp, text = nextEventDate, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __eventDate.grid(row = 1, column = 1, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __eventLocation = Label(__eventPopUp, text = nextEventLocation, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __eventLocation.grid(row = 2, column = 1, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __eventDescription = Label(__eventPopUp, text = nextEventDescription, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND, wraplength = SECOND_WINDOW_WRAP, justify = LEFT)
        __eventDescription.grid(row = 3, column = 1, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __filler = Label(__eventPopUp, background = SECOND_WINDOW_BACKGROUND, text = "")
        __filler.grid(row = 4, sticky = SINGLE_LINE_LEFT_JUSTIFY)
