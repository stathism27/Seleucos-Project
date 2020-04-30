import random
from random import choices
positions = {
    1: "Goalkeeper",
    2: "Defender Center",
    3: "Defender Left",
    4: "Defender Right",
    5: "Winger Back Left",
    6: "Winger Back Right",
    7: "Defensive Midfielder",
    8: "Midfielder Center",
    9: "Midfielder Left",
    10: "Midfielder Right",
    11: "Attacking Midfielder",
    12: "Attacking Midfielder Left",
    13: "Attacking Midfielder Right",
    14: "Striker"
}
#Which positions are more likely
positionsExtra = {
    2: [4,3,7,8],
    3: [2,4,9,7],
    4: [2,3,10,7],
    5: [3,9,12,7],
    6: [4,10,13,7],
    7: [2,8,11,14],
    8: [5,11,9,10],
    9: [12,3,8,10],
    10: [12,4,8,9],
    11: [14,8,12,13],
    12:[9,13,13,11],
    13: [10,12,14,11],
    14: [11,12,13,8]
}
def nextPositions():
    mainPosition = random.randint(1,12)
    willHaveExtra = random.random()
    if(willHaveExtra<0.1 or mainPosition == 1): #10% that the player can play only in one position
        return {mainPosition:100}

    else:
        #return None
        return getExtraPositions(mainPosition)


def getExtraPositions(mainPosition):
    pos = {mainPosition:100}
    extraPos = [1, 2, 3, 4]
    p = [0.60, 0.30, 0.07, 0.03] #distribution so as to know how many extra positions will have,max 4
    howManyExtraPos = choices(extraPos, p)[0]
    pExtra = [0.9,0.04,0.04,0.02] #distributions of what these will be,according to dictionary above

    newPosArray = positionsExtra[mainPosition]

    addPositions = choices(newPosArray, pExtra,k=howManyExtraPos) #Now I am creating an array of added positions
    #For instance if we add 4 positions this will create an array of 4 elements containing the extra positions

    for i in range(howManyExtraPos):
        finalPosition = addPositions[i] #we add to the positions dictionary our position
        finalScore = random.randint(50,100) #find a score between 50-100 (50 is an adequate level)
        pos[finalPosition] = finalScore

    del extraPos,p,howManyExtraPos,newPosArray,addPositions,

    return pos

#Function to convert the dictionary to String Dictionary
#containing the positions in their proper forms
def posToDictString(pos):
    newDict = {}
    for key in pos:
        newDict[positions[key]] = pos[key]
    return newDict

def posToString(pos):
    newPos = posToDictString(pos)
    return next(iter(newPos.keys()))

