import random
daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

CURRENT_YEAR = 2020
def nextAge():
    age = random.randint(17, 35) # inclusive random : [17,35], Uniform Distribution
    return age

def getDate(age):
    month = random.randint(1, 12)# inclusive random : [1,12], Uniform Distribution

    dayLimit = daysInMonth[month - 1]
    day = random.randint(1, dayLimit) #inclusive limit : ex December [1,31]


    return day,month, CURRENT_YEAR - age




