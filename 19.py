def nextDay(currentDay):
    if currentDay == "Monday":
        return "Tuesday"
    elif currentDay == "Tuesday":
        return "Wednesday"
    elif currentDay == "Wednesday":
        return "Thursday"
    elif currentDay == "Thursday":
        return "Friday"
    elif currentDay == "Friday":
        return "Saturday"
    elif currentDay == "Saturday":
        return "Sunday"
    elif currentDay == "Sunday":
        return "Monday"



def isLeapYear(year):
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False

def nextDate(currentDate):
    currentDate = currentDate.split()
    months30 = ["April", "June", "September", "November"]
    months31 = ["January", "March", "May", "July", "August", "October", "December"]
    if currentDate[] == ""

currentDay = "Monday"
currentDate = "1 Jan 1901"
