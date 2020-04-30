import player
import time
import json
players_list = []


def create(id):
    p = player.Player(id)
    players_list.append(p)

starting_id = 100000 #Players will have ID starting at 100000
sizeOfDB = 10000 #10k players

def exportToJSON(players_list,FILENAME):
    finalDictionary = {}
    finalDictionary["Size"] = sizeOfDB
    for player in players_list:
        finalDictionary[player.id] = player.toDict()
    with open(FILENAME, 'w') as fp:
        json.dump(finalDictionary, fp,indent=4)

start_time = time.time()


for id in range(starting_id,starting_id+sizeOfDB):
    #print(i)
    create(id)

exportToJSON(players_list,"result.json")


print(sizeOfDB,",",(time.time() - start_time))
print(players_list.__len__())

