import random
#In this script we need some stuff on memory
#All the First Names and Surnames of each region. eg firstnames[0] = a list of all afrikaans names
#Then a dict regionToIndex so as match regions with indices eg. afrikaans : 0 (check above why)
#Then a dict countries_regions because we need to match a country to the region names : South Africa -> afrikaans names
#Finally we have some exceptions,because Brazil and China players most of them a only a one name
firstnames = []
surnames = []
regionToIndex = {}
REGIONS_FILE = 'resources/aux-res/regions.txt'
COUNTRIES_REGIONS_FILE = 'resources/aux-res/countries-regions.txt'
countries_regions = {}
special_countries = ["Brazil","China"] #These countries usually have one name instead of First and Surname
#A function to open files to load stuff in memory
def openFile(NAMES_FILE,SUR_FILES,firstArr,surArr):
    f1 = open(NAMES_FILE, 'r')
    lines = f1.readlines()
    for line in lines:
        line = line.replace('\n','')
        firstArr.append(line)
    f1.close()

    f2 = open(SUR_FILES, 'r')
    lines = f2.readlines()
    for line in lines:
        line = line.replace('\n','')
        surArr.append(line)
    f2.close()
    del f1,f2
    return


def setupFiles():
    f = open(REGIONS_FILE,'r')
    lines = f.readlines()
    index = 0 #index is used so as to create a dictionary to know the exact index in firstnames and surnames array
    # eg afrikaans: index = 0, firstnames[0] = all first afrikaans names
    for region in lines:
        region = region.replace('\n','')
        NAMES_FILE = 'resources/names/first/'+region+'-first.txt'
        SUR_FILES = 'resources/names/surname/'+region+'-surname.txt'
        firstnames.append([])
        surnames.append([])
        openFile(NAMES_FILE,SUR_FILES,firstnames[index],surnames[index])

        regionToIndex[region] = index
        index+=1

    f.close()
    del f
    f = open(COUNTRIES_REGIONS_FILE,'r')
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n','')
        cont = line.split(',')
        country = cont[0]
        r = ""
        for i in range(1,cont.__len__()):
            r = r+","+cont[i]

        countries_regions[country] = r
    f.close()
    del f,lines,index,region,country,r


def getRegions(country):
    regs = countries_regions[country].split(",")
    del regs[0] #this you should not delete
    return regs

def getName(country,name): #get random name or surname(depends on the array you pass)
    name_pool = []
    regionsAvailable = getRegions(country)
    for region in regionsAvailable:
        index_of_region = regionToIndex[region]  # eg Afrikaans = 1
        for n in name[index_of_region]:

            name_pool.append(n)  # append the surnames of each region

    s = random.randint(0, name_pool.__len__() - 1)
    name = name_pool[s]

    del regionsAvailable,name_pool,index_of_region,s
    return name
def nextName(country):

    if(not isinstance(country, str)):
        country = country[random.randint(0,country.__len__()-1)]

    if(special_countries.__contains__(country)):
        r = random.random()
        if(r<0.7):
            surname = ""
        else:
            surname = getName(country,surnames)
    else:
        surname = getName(country,surnames)

    name = getName(country,firstnames)

    return name,surname

setupFiles()

