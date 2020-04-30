from random import choices
import random
SCALA = 25
classes = [1,2,3,4]
p = [0.12,0.30,0.45,0.13]
def nextAbilities():
    current = 0

    classOfPlayer = choices(classes, p)[0]
    downLimit = (classOfPlayer-1)* SCALA + 1
    upLimit = SCALA*classOfPlayer
    current = random.randint(downLimit, upLimit) # 1-25,26-50,51-75,76-100
    added = random.gauss(0.15, 0.10)
    if(added<0):
        added = 0
    potential = round(current + current*added)
    if(potential>100):
        potential = 100

    del classOfPlayer
    del downLimit,upLimit
    del added
    return current,potential



