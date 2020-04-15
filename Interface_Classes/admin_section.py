from tkinter import *
import tkinter.messagebox
from datetime import datetime, time
from tkinter import ttk
from tkcalendar import DateEntry
from constants import SINGLE_LINE_LEFT_JUSTIFY, WHOLE_ROW, SECOND_WINDOW_BACKGROUND, SECOND_WINDOW_FOREGROUND, ERROR_BOX_TOP

class AdminSection:
    """The Admin Section of the GUI"""

    # the constructor for the AdminSection
    # CREATES AND STARTS THE ADMIN SECTION
    # param: the recommender object
    # returns: nothing
    def __init__(self, recommendObject):
        global eventName, descriptionEntry, dateInput, minuteEntry, locationEntry, hourEntry, clubEntry, recommend

        recommend = recommendObject

        __clubNames = recommend.getClubNames()

        __admin = Tk()
        __admin.configure(background=SECOND_WINDOW_BACKGROUND)
        __admin.wm_title("Admin Section")

        __directions = Label(__admin, text = "Welcome, Admin! Below you can add an event for any of the clubs. Have a fantastic day :)", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __directions.grid(row = 0, columnspan = 2, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __admin_space_1 = Label(__admin, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __admin_space_1.grid(row = 1, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __eventNameLabel = Label(__admin, text = "Event Name: ", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __eventNameLabel.grid(row = 2, column = 0, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        eventName = Entry(__admin)
        eventName.grid(row = 2, column = 1, sticky= WHOLE_ROW)

        __admin_space_2 = Label(__admin, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __admin_space_2.grid(row = 3, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        # date input
        __dateLabel = Label(__admin, text = "Date of Occurance (in MM/DD/YY): ", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __dateLabel.grid(row = 4, column = 0, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        dateInput = DateEntry(__admin, locale = 'en_US')
        dateInput.grid(row = 4, column = 1, sticky= WHOLE_ROW)
        #, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND

        __admin_space_8 = Label(__admin, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __admin_space_8.grid(row = 5, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __hourLabel = Label(__admin, text = "Hour (in 24 hour format): ", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __hourLabel.grid(row = 6, column = 0, sticky = SINGLE_LINE_LEFT_JUSTIFY)

        hourEntry = Entry(__admin)
        hourEntry.grid(row = 6, column = 1, sticky = WHOLE_ROW)

        __admin_space_7 = Label(__admin, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __admin_space_7.grid(row = 7, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __minuteLabel = Label(__admin, text = "Minute: ", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __minuteLabel.grid(row = 8, column = 0, sticky = SINGLE_LINE_LEFT_JUSTIFY)

        minuteEntry = Entry(__admin)
        minuteEntry.grid(row = 8, column = 1, sticky = WHOLE_ROW)

        __admin_space_3 = Label(__admin, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __admin_space_3.grid(row = 9, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __locationLabel = Label(__admin, text = "Location: ", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __locationLabel.grid(row = 10, column = 0, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        locationEntry = Entry(__admin)
        locationEntry.grid(row = 10, column = 1, sticky= WHOLE_ROW)

        __admin_space_4 = Label(__admin, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __admin_space_4.grid(row = 11, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __descriptionLabel = Label(__admin, text = "Event Description: ", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __descriptionLabel.grid(row = 12, column = 0, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        descriptionEntry = Entry(__admin)
        descriptionEntry.grid(row = 12, column = 1, sticky= WHOLE_ROW)

        __admin_space_5 = Label(__admin, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __admin_space_5.grid(row = 13, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __clubDescriptionLabel = Label(__admin, text = "Club: ", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __clubDescriptionLabel.grid(row = 14, column = 0, sticky = SINGLE_LINE_LEFT_JUSTIFY)

        clubEntry = ttk.Combobox(__admin, values = __clubNames)
        clubEntry.grid(row = 14, column = 1, sticky = WHOLE_ROW)

        __admin_space_6 = Label(__admin, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __admin_space_6.grid(row = 15, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __submitButton = Button(__admin, text = "Submit", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND, command = self.creatingAnEvent)
        __submitButton.grid(row = 16, columnspan = 2, sticky = WHOLE_ROW)

        __admin.mainloop()

    # creates an event based on user input
    # gets called when the user hits submit
    # param: none
    # returns: nothings
    def creatingAnEvent(self):
            name = eventName.get()
            club = clubEntry.get()
            date = dateInput.get_date()
            hour = hourEntry.get()
            minute = minuteEntry.get()

            location = locationEntry.get()
            description = descriptionEntry.get()
            if(name == "" or club == "" or date == None or location == "" or description == "" or hour == "" or minute == ""):
                tkinter.messagebox.showerror(ERROR_BOX_TOP, "You left one or more fields blank. Fill them all in then try again.")
            else:
                newHour = int(hour)
                newMinute = int(minute)
                eventTime = time(newHour, newMinute)
                eventDateTime = datetime.combine(date, eventTime)

                if(eventDateTime < datetime.now()):
                    tkinter.messagebox.showerror("Oops", "The date you entered is in the past.")

                recommend.addEventToClub(club, name, eventDateTime, location, description)
                tkinter.messagebox.showinfo("Event Added", "Your event has been added")
                self.__clearTheScreen()


    # clears the Admin screen
    # param: none
    # returns: none
    def __clearTheScreen(self):
        eventName.delete(0,'end')     # clears the user's input in the entry box
        clubEntry.delete(0, 'end')
        hourEntry.delete(0, 'end')
        minuteEntry.delete(0, 'end')
        locationEntry.delete(0, 'end')
        descriptionEntry.delete(0, 'end')
