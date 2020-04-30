#Sum of weights for each position

from random import choices
import positions
import random
import abilities
weights_sum = {}

technical_weight = {
    "Corners": [0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    "Crossing": [0,1,2,2,3,3,1,1,4,4,1,4,4,2],
    "Dribbling":[0,1,1,1,2,2,2,2,3,3,3,4,4,3],
    "Finishing": [0,1,1,1,1,1,2,2,2,2,3,2,2,4],
    "First Touch": [1,2,2,2,3,3,3,3,3,3,3,3,3,4],
    "Free Kicks" : [0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    "Heading": [1,4,2,2,1,1,1,1,1,1,1,1,1,4],
    "Long Shots": [0,1,1,1,1,1,3,3,2,2,3,2,2,2],
    "Long Throws":[0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    "Marking":[0,4,3,3,2,2,1,1,1,1,1,1,1,1],
    "Passing":[1,2,2,2,3,3,4,4,3,3,4,2,2,2],
    "Penalty":[0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    "Tackling":[0,4,4,4,3,3,4,3,2,2,2,2,2,1],
    "Technique":[1,1,2,2,3,3,3,3,3,3,3,3,3,3]
}

mental_weight = {
    "Aggression":[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "Anticipation":[2,3,3,3,3,3,3,3,3,3,3,3,3,3],
    "Bravery":[4,2,2,2,1,1,1,1,1,1,1,1,1,1],
    "Composure":[2,2,2,2,2,2,2,3,3,3,3,3,3,4],
    "Concentration":[4,4,4,4,3,3,3,2,2,2,2,2,2,2],
    "Decision Taking":[4,4,4,4,3,3,3,3,2,2,3,2,2,2],
    "Determination":[4,4,4,4,3,3,3,3,2,2,3,2,2,2],
    "Flair":[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "Leadership":[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "Positioning":[4,4,4,4,3,3,3,2,1,1,2,1,1,2],
    "Teamwork":[2,1,2,2,2,2,2,2,2,2,2,2,2,1],
    "Vision":[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "Without Ball":[0,1,1,1,2,2,1,2,2,2,3,2,2,4],
    "Work Rate":[1,2,2,2,2,2,4,3,3,3,3,3,3,2]
}

physical_weight = {
    "Acceleration": [3,4,4,4,4,4,4,4,5,5,5,6,6,6],
    "Agility": [4,3,3,3,3,3,3,3,3,3,3,3,3,3],
    "Balance":[2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    "Jumping":[1,4,2,2,1,1,1,1,1,1,1,1,1,4],
    "Natural Fitness":[1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "Pace":[2,4,4,4,4,4,4,4,5,5,5,6,6,6],
    "Stamina":[1,3,3,3,4,4,3,3,3,3,3,3,3,2],
    "Strength":[3,4,3,3,2,2,3,3,2,2,3,2,2,4]

}

goalkeeper_weight = {
    "Aerial Ability":[4,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "Command Of Area":[4,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "Communication":[4,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "Eccentricity":[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "First Touch":[1,2,2,2,3,3,3,3,3,3,3,3,3,4],
    "Free Kicks" : [0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    "Handling":[5,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "Kicking":[4,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "One on Ones":[4,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "Penalty":[0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    "Reflexes":[5,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "Rushing Out":[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "Tendency to Punch":[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "Throwing":[3,0,0,0,0,0,0,0,0,0,0,0,0,0],
}


def setUpWeights():
    max_pos = positions.positions.__len__()
    for pos in range(1,max_pos):
        totalWeight = 0
        if(pos == 1):
            for key in goalkeeper_weight.keys():
                totalWeight+= goalkeeper_weight[key][pos-1]
            for key in mental_weight.keys():
                totalWeight += mental_weight[key][pos - 1]
            for key in physical_weight.keys():
                totalWeight+= physical_weight[key][pos-1]
        else:
            for key in technical_weight.keys():
                totalWeight+= technical_weight[key][pos-1]
            for key in mental_weight.keys():
                totalWeight += mental_weight[key][pos - 1]
            for key in technical_weight.keys():
                totalWeight+= technical_weight[key][pos-1]


        weights_sum[pos] = totalWeight



def nextAttributes(pos):
    pos = next(iter(pos.keys()))
    ca,pa = abilities.nextAbilities()
    if(pos == 1):
        theWeightIs = goalkeeper_weight
    else:
        theWeightIs = technical_weight


    return calcAttributes(ca, pos, [theWeightIs, mental_weight, physical_weight])

def calcAttributes(ability,pos,weights):
    #There dictionaries are the final characteristics we want to get
    technical = {}
    mental = {}
    physical = {}


    index = pos-1
    whichLoop = 0
    for dict in weights: # the weights contain the weights of : technical(or gk),mental and physical
        for a in dict.keys(): #a can be technical,mental or physical weight dictionary. dict
            if(dict[a][index] == 0): #if the weight is 0
                if(whichLoop == 0): #If we are examining the first position of dict(technical attributes)
                    classes = [round(ability/2),100]
                    p = [0.99, 0.01]
                    limit = choices(classes, p)[0]
                    # So what we are doing here is that if an attribute is technical but no weight(for strikers this would be marking)
                    # then this attribute is by 99% <half ability of player(Top Striker with Ability : 90 is more likely to have <45 marking)
                    if(limit == ability):
                        val = random.randint(1, ability)
                    else:
                        val = random.randint(ability, 100)

                else: #if we are not in technical dict - this is done because for instance strikers usually don't have good marking
                    #but if we examine aggression a striker can have 1 as well as 100 - there is no patter in mental or physical
                    val = round(abs(random.gauss(ability, ability*0.2))) #around 20% standard deviation
                    if(val>100):
                        val = 100
            else: #if the weight is not 0, so it counts we must regulate this
                val = round(abs(random.gauss(ability, ability * 0.2)))  # around 20% standard deviation
                if (val > 100):
                    val = 100

            if(whichLoop == 0 ):
                technical[a] = val
            elif(whichLoop == 1):
                mental[a] = val
            else:
                physical[a] = val

        whichLoop+=1
    ca,pa = redifineAbilities([technical,mental,physical],pos)
    return technical,mental,physical,ca,pa

def redifineAbilities(attr,pos):
    currentAbility = 0
    potentialAbility = 0
    index = pos-1

    i = 0
    for category in attr:
        for key in category.keys():
            #cases if the category is technical,goalkeeper,metanl,physical
            if(i==0 and pos!=1):
                w = technical_weight[key][pos-1]/weights_sum[pos]
            elif(i==0 and pos==1):
                w = goalkeeper_weight[key][pos - 1] / weights_sum[pos]
            elif(i==1):
                w = mental_weight[key][pos-1]/weights_sum[pos]
            else:
                w = physical_weight[key][pos - 1] / weights_sum[pos]

            currentAbility+= w*category[key]
        i += 1
    #The current ability must be integer and the potential ability(normally 15% up - maybe more)
    currentAbility = round(currentAbility)
    added = abs(random.gauss(0.15, 0.10)) #abs so as the potential will be at least as much as current - this case when added=0
    potentialAbility = round(currentAbility + currentAbility * added)
    if (potentialAbility > 100):
        potentialAbility = 100


    return currentAbility,potentialAbility



setUpWeights()

