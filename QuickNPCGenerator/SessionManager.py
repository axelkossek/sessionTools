import json
import random

def CreateSessionFile(campaignName, sessionNumber, sessionFile = ""):
    dictionary = {
        'campaignName': campaignName, 
        'sessionNumber': sessionNumber,
        'npcs' : []
         }
    
    
    if not sessionFile:
        sessionFile = campaignName + "_" + str(sessionNumber) + ".json"

    with open(sessionFile, "w") as f:
        json.dump(dictionary, f)

def AbilityDistribution(percentile):
    distro = [5, 25, 40, 25, 5]
    values = [7, 8, 9, 10, 11]
    if   percentile < sum(distro[0:1]):
        return values[0]
    elif percentile < sum(distro[0:2]):
        return values[1]
    elif percentile < sum(distro[0:3]):
        return values[2]
    elif percentile < sum(distro[0:4]):
        return values[3]
    else:
        return values[4]


def GenerateRandomAbilityScores():
    return [ AbilityDistribution(random.randint(0, 99)) for i in range(0,10) ]

def GenerateStatsDict(scores):
    return {
        'str' : scores[0],
        'dex' : scores[1],
        'con' : scores[2],
        'int' : scores[3],
        'wis' : scores[4],
        'cha' : scores[5]
        }


def GenerateNPCDict(name, family, race, occupation, stats, appearance):
    return {
        'name' : name,
        'family' : family,
        'race' : race,
        'occupation' : occupation,
        'stats' : stats,
        'appearance' : appearance
        }

def AppendNPCToSession(sessionFile, npc):
    with open(sessionFile, "r") as f:
        session = json.load(f)
    
    session['npcs'].append(npc)

    with open(sessionFile, "w") as f:
        json.dump(session, f)


def ListSessionNPCs(sessionFile):
    with open(sessionFile, "r") as f:
        session = json.load(f)
        for npc in session['npcs']:
            print("{0}, {1} the {2} {3}. Stats: {4}, Appearance: {5}".format(npc['name'], npc['family'], npc['race'], npc['occupation'], npc['stats'], npc['appearance']))

fileS = "test_1.json";
CreateSessionFile("test", 1)
enpec = GenerateNPCDict("John", "Smith", "Human", "Smith", GenerateStatsDict(GenerateRandomAbilityScores()), "old")
AppendNPCToSession(fileS, enpec)
enpec = GenerateNPCDict("Jane", "Novak", "Elf", "Wizard", GenerateStatsDict(GenerateRandomAbilityScores()), "young")
AppendNPCToSession(fileS, enpec)
ListSessionNPCs(fileS)
