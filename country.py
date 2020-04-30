COUNTRIES_FILE = 'resources/countries.txt'
countries = []
import random
def openFile():
    f = open(COUNTRIES_FILE, 'r')
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n','')
        countries.append(line)
    f.close()
    del f
    return countries

def nextCountry():
    double_citizenship = random.random()
    whatCitizenShip = random.randint(0, countries.__len__() - 1)
    citizenship = countries[whatCitizenShip]

    if(double_citizenship < 0.1): # 10% that someone will have a second citizenship
        whatCitizenShip2 = random.randint(0, countries.__len__() - 1)
        citizenship2 = countries[whatCitizenShip2]
        while(citizenship == citizenship2):
            whatCitizenShip2 = random.randint(0, countries.__len__()-1)
            citizenship2 = countries[whatCitizenShip2]
        return citizenship,citizenship2
    else:
        return citizenship


openFile()