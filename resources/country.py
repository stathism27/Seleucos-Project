import csv
COUNTRIES_FILE = 'resources/countries-population.csv'
countries = []
population = []
w = 0
import random
# def openFile():
#     f = open(COUNTRIES_FILE, 'r')
#     lines = f.readlines()
#     for line in lines:
#         line = line.replace('\n','')
#         countries.append(line)
#     f.close()
#     del f
#     return countries


def openFile():
    world_population = 0
    with open(COUNTRIES_FILE) as f:
        c= 0
        csv_reader = csv.reader(f)
        for row in csv_reader:
            if(c>0):
                countries.append(row[0])
                population.append(int(row[1]))
                world_population += int(row[1])
            c+=1

        del countries[0],population[0]

        for i in range(len(population)):
            population[i] /= world_population

# def nextCountry():
#     double_citizenship = random.random()
#     whatCitizenShip = random.randint(0, countries.__len__() - 1)
#     citizenship = countries[whatCitizenShip]
#
#     if(double_citizenship < 0.1): # 10% that someone will have a second citizenship
#         whatCitizenShip2 = random.randint(0, countries.__len__() - 1)
#         citizenship2 = countries[whatCitizenShip2]
#         while(citizenship == citizenship2):
#             whatCitizenShip2 = random.randint(0, countries.__len__()-1)
#             citizenship2 = countries[whatCitizenShip2]
#         return citizenship,citizenship2
#     else:
#         return citizenship


def nextCountry():
    double_citizenship = random.random()
    whatCitizenShip = random.choices(countries, population)[0]
    citizenship = whatCitizenShip

    if(double_citizenship < 0.1): # 10% that someone will have a second citizenship
        whatCitizenShip2 = random.choices(countries, population)[0]
        citizenship2 = whatCitizenShip2
        while(citizenship == citizenship2):
            whatCitizenShip2 = random.choices(countries, population)[0]
            citizenship2 = whatCitizenShip2
        return citizenship,citizenship2
    else:
        return citizenship


openFile()
for i in range(200):
    print(nextCountry())