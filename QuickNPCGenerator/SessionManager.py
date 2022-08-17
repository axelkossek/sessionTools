import json

def CreateSessionFile(campaignName, sessionNumber, sessionFile = ""):
    dictionary = {
        'campaignName': campaignName, 
        'sessionNumber': sessionNumber,
        'npcs' : []
         }
    
    
    if not sessionFile:
        sessionFile = campaignName + "_" + str(sessionNumber) + ".json"

    with open(sessionFile, "w") as file:
        json.dump(dictionary, file)

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
    with open(sessionFile, "r") as file:
        session = json.load(file)
    
    session['npcs'].append(npc)

    with open(sessionFile, "w") as file:
        json.dump(session, file)


def ListSessionNPCs(sessionFile):
    with open(sessionFile, "r") as file:
        session = json.load(file)
        for npc in session['npcs']:
            print("{0}, {1} the {2} {3}. Stats: {4}, Appearance: {5}".format(npc['name'], npc['family'], npc['race'], npc['occupation'], npc['stats'], npc['appearance']))
        #print("{0}, {1} the {3} {4}. Stats: {5}, Appearance: {6}".format(npc['name'], npc['family'], npc['race'], npc['occupation'], npc['stats'], npc['appearance']) for npc in session['npcs'])

fileS = "test_1.json";
CreateSessionFile("test", 1)
enpec = GenerateNPCDict("John", "Smith", "Human", "Smith", "14,12,12,10,10,10", "old")
AppendNPCToSession(fileS, enpec)
enpec = GenerateNPCDict("Jane", "Novak", "Elf", "Wizard", "8,12,10,14,12,10", "young")
AppendNPCToSession(fileS, enpec)
ListSessionNPCs(fileS)

