import age, attributes, body, country, names, positions
class Player():
    def __init__(self,id):

        self.id = id
        self.myAge = age.nextAge()
        self.myDate = age.getDate(self.myAge)

        self.myPositions = positions.nextPositions() #merely a problem

        self.myTechnical,self.myMental,self.myPhysical,self.myCurrentAbility,self.myPotentialAbility = attributes.nextAttributes({1:20})

        self.myHeight = body.nextHeight()

        self.myWeight = body.nextWeight(self.myHeight)
        self.myFoot = body.nextFoot()

        self.myCountry = country.nextCountry()
        self.myName,self.mySurname = names.nextName(self.myCountry)

    def __del__(self):
        del self.id,self.myAge,self.myDate,self.myPositions
        del self.myTechnical,self.myMental,self.myPhysical,self.myCurrentAbility,self.myPotentialAbility
        del self.myHeight,self.myWeight,self.myFoot,self.myCountry,self.myName,self.mySurname

    def showMesage(self):
        print("==============")
        print("Hello I am :",self.myName,self.mySurname)
        print("I am from :", self.myCountry)
        print("I am born in ",self.myDate," and I am",self.myAge,"years old")
        print("I am : ",self.myHeight,"cm and",self.myWeight,"kg")
        print("My strong foot is :",body.getFootString(self.myFoot))
        print("My main position is: ",positions.posToString(self.myPositions))

    def toDict(self):
        dict = {}
        dict["ID"] = self.id
        dict["Name"] = self.myName
        dict["Surname"] = self.mySurname
        dict["Age"] = self.myAge
        dict["Date"] = self.myDate
        dict["Height"] = self.myHeight
        dict["Weight"] = self.myWeight
        dict["Foot"] = self.myFoot
        dict["Country"] = self.myCountry
        dict["Positions"] = self.myPositions
        dict["Technical"] = self.myTechnical
        dict["Mental"] = self.myMental
        dict["Physical"] = self.myPhysical
        dict["Current Ability"] = self.myCurrentAbility
        dict["Potential Ability"] = self.myPotentialAbility

        return dict



