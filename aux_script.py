FILE = 'resources/aux-res/countries-regions.txt'
FILE_OUT = 'resources/aux-res/regions.txt'
regions = []
#A script that takes the file with the countries and the names eg Germany - German names,Portugal - Portuguese names, Greek - Greek names etc
#Then converts the region names to a unique sorted file.For instance Belgium has French,Dutch and German names
def openFile(FILE):
    f = open(FILE, 'r')
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n','')
        reg = line.split(",")
        for i in range(1,reg.__len__()):
            if (not regions.__contains__(reg[i])):
                regions.append(reg[i])
    f.close()
    list.sort(regions)
    return regions

def saveFile(FILE_OUT,arr):
    f = open(FILE_OUT, "w")
    f.close()
    f = open(FILE_OUT, "a")
    for i in arr:
        f.write(i+'\n')
    f.close()


#Now these functions are to convert the csv file to file with names of each country


def csvToNames():

    names = {}
    surnames = {}
    for reg in regions:


        if(reg!="english"):
            filename = 'resources/aux-res/csv/'+reg+'.csv'
            f = open(filename, 'r')
            lines = f.readlines()
            countryNames = []
            countrySurnames = []
            for line in lines:
                line = line.replace('\n', "")
                line = line.replace("\"","")
                line = line.replace("\'","")
                if(line!="Name"):
                    if(line.__contains__(",")):
                        names = line.split(",")
                        names[0] = names[0].replace(" ","")
                        names[1] = names[1].replace(" ","")
                        countrySurnames.append(names[0])
                        countryNames.append(names[1])

                        '''
                        if(not countrySurnames.__contains__(names[0])):
                            countrySurnames.append(names[0])
                        if (not countryNames.__contains__(names[1])):
                            countryNames.append(names[1])
                        '''
                    else:
                        countryNames.append(line)
            f.close()
            exit_file_first = 'resources/names/first/'+str(reg)+'-first.txt'
            exit_file_surname = 'resources/names/surname/'+str(reg)+'-surname.txt'
            list.sort(countryNames)
            list.sort(countrySurnames)
            saveFile(exit_file_first,countryNames)
            saveFile(exit_file_surname,countrySurnames)





openFile(FILE)
saveFile(FILE_OUT,regions)
csvToNames()
