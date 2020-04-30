import random
def nextWeight(height):
    factor = 100*height #for 1.70 is 70, for 2.01 is 101, for 1.80 is 80
    mean_weight = (factor-100)- round(factor*0.05) #so as the weight will be close to height : the mean weight is -5% of 70 for someone 1.70
    weight = random.gauss(mean_weight, 10) #Normal Distribution for the weight
    return round(weight)

def nextHeight():
    height = random.gauss(1.78, 0.08)
    return round(height,2)


def nextFoot():
    what_foot = random.random()
    if(what_foot >= 0 and what_foot <0.35): #35% of being left foot
        left = 10
        right = random.randint(0, 5)
    if(what_foot >= 0.35 and what_foot <0.75): # 40% of being right foot
        right = 10
        left = random.randint(0, 5)
    if (what_foot >= 0.75):# 40% of being both
        if (what_foot <0.85): #better left than right
            left = 10
            right = random.randint(5+1, 10)
        else: #better right than left
            right = 10
            left = random.randint(5+1, 10)


    return left,right

def getFootString(foot):
    if(foot[0] == 10):
        if(foot[1]<=5):
            return "left"
    else:
        if(foot[0]<=5):
            return "right"


    return "both"




