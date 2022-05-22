global extradays
global isPM


def add_time(start, duration, StartDay = "none"):
    
    new_time = ""
    global extradays
    global isPM
    extradays = 0
    isPM = False
    
    #check and flag if we were given a start day
    hasStartDay = False
    if(StartDay != "none"):
        hasStartDay = True
        StartDay = StartDay.title()
    
    #check if we are AM or PM
    startSplit = start.split()
    if(startSplit[1] == "PM"):
        isPM = True
    
    #split our times into hours and minutes
    startTime = startSplit[0]
    startTime= startTime.split(':')
    startTimeHrs = startTime[0]
    startTimeMins = startTime[1]

    durationTime = duration.split(':')
    durationHrs = durationTime[0]
    durationMins = durationTime[1]

    #add our minutes, add any extra hours
    minsAdd = minutesAdder(startTimeMins,durationMins)
    if(minsAdd[1] > 0):
      durationHrs = minsAdd[1] + int(durationHrs)
    durationHours = hoursAdder(startTimeHrs,durationHrs)

    #build our string with the finale time
    newMins = ""
    
    if(minsAdd[0] < 10):
        newMins = str(minsAdd[0]).zfill(2)
    else:
        newMins = str(minsAdd[0])

    new_time = str(durationHours) + ":" + newMins
    
    if(isPM):
        new_time += " PM"
    else:
        new_time += " AM"
    if(hasStartDay):
        new_time += "," + dayoftheweekNames(extradays + dayoftheweekInts(StartDay))
    if(extradays > 0):
            new_time += daysCounterConverter(extradays)
    return new_time

#adds together our minutes and returns the extra hours and leftover minutes, or simply sums the minutes
def minutesAdder(mins1, mins2):
    rMins = int(mins1) + int(mins2)
    extraHours = 0
    if(rMins > 59):
        extraHours= int(rMins/60)
        rMins = int(rMins % 60)
    return [rMins,extraHours]

#adds together our hours and returns if we needed to flip AM/PM
def hoursAdder(hours1, hours2):
    hoursSum = int(hours1) + int(hours2)
    global isPM
    global extradays
    if(isPM):
        hoursSum = hoursSum + 12
    if(hoursSum > 24):
        if not (isPM):
            extradays += roundUper(hoursSum/24)
        else:
            extradays += int(hoursSum/24)
        hoursSum = hoursSum % 24
    
    if(hoursSum == 0):
        hoursSum = 12
        isPM = False
        return hoursSum
    if(hoursSum >= 12):
        isPM = True
        if(hoursSum > 12):
            hoursSum = hoursSum - 12
    else:
        isPM = False

    return hoursSum

#returns a float as a rounded up int
def roundUper(floatNum):
    global isPM
    intR = int(floatNum)
    if(isPM):
        if(floatNum % 1 != 0 ):
            intR += 1
    return intR

#converts a day of the week from an integer to its String name
def dayoftheweekNames(intNum):
    if(intNum > 7):
        intNum = intNum % 7
    if(intNum == 0):
        return " Monday"
    if(intNum == 1):
        return " Teusday"
    if(intNum == 2):
        return " Wednesday"
    if(intNum == 3):
        return " Thursday"
    if(intNum == 4):
        return " Friday"
    if(intNum == 5):
        return " Saturday"
    if(intNum == 6):
        return " Sunday"
    if(intNum == 7):
        return " Monday"

#returns the integer representation of the day of the week from a given string.
def dayoftheweekInts(strName):
    strName = strName.title()
    
    if(strName == "Monday"):
        return 0
    if(strName == "Tuesday"):
        return 1
    if(strName == "Wednesday"):
        return 2
    if(strName =="Thursday" ):
        return 3
    if(strName == "Friday"):
        return 4
    if(strName == "Saturday"):
        return 5
    if(strName == "Sunday"):
        return 6

#converts our extra day counter into the properly formated string
def daysCounterConverter(intNum):
    if(intNum == 1):
        return " (next day)"
    else:
        return " (" + str(intNum) + " days later)"