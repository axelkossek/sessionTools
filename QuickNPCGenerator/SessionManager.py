import json
import random
import os
from ssl import SSLSession

class SessionManager:
    def __init__(self, sessionFile = "", campaignName = "", sessionNumber = ""):
        self.sessionFile = sessionFile

        if not os.path.exists(sessionFile):
            self.CreateSessionFile(campaignName, sessionNumber)          

    def GetParam(self, parameter):
        session = self.GetDictionary()
        return session[parameter]

    def SetParam(self, parameter, value):
        session = self.GetDictionary()
        session[parameter] = value
        self.DumpDictionary(session)

    def GetCampaignName(self):
        return self.GetParam('campaignName')

    def SetCampaignName(self, value):
        self.SetParam('campaignName', value)

    def GetSessionNumber(self):
        return self.GetParam('sessionNumber')

    def SetSessionNumber(self, value):
        self.SetParam('sessionNumber', value)

    def GetNPCs(self):
        return self.GetParam('npcs')

    def SetNPCs(self, value):
        self.SetParam('npcs', value)

    def AppendNPC(self, npc):
        npcs = self.GetNPCs()
        npcs.append(npc)
        self.SetNPCs(npcs)

    def CreateSessionFile(self, campaignName, sessionNumber):
        if campaignName and campaignName:
            sessionContents = {
                    'campaignName': campaignName, 
                    'sessionNumber': sessionNumber,
                    'npcs' : []
                     }
            if not self.sessionFile:
                self.sessionFile = self.campaignName + "_" + str(self.sessionNumber) + ".json"
            self.DumpDictionary(sessionContents)
        else:
            print("Could not create session file because no campaign name or session number were provided during session creation.")

    def GetDictionary(self):
        with open(self.sessionFile, "r") as f:
            return json.load(f)

    def DumpDictionary(self, value):
        with open(self.sessionFile, "w") as f:
                json.dump(value, f)

    def ListSessionNPCs(self):
            for npc in self.GetNPCs():
                print("{0}, {1} the {2} {3}. Stats: {4}, Appearance: {5}".format(npc['name'], npc['family'], npc['race'], npc['occupation'], npc['stats'], npc['appearance']))

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


fileS = "test_1.json";
manager = SessionManager(sessionFile = fileS, campaignName = "test", sessionNumber = 1)

enpec1 = GenerateNPCDict("John", "Smith", "Human", "Smith", GenerateStatsDict(GenerateRandomAbilityScores()), "old")
enpec2 = GenerateNPCDict("Jane", "Novak", "Elf", "Wizard", GenerateStatsDict(GenerateRandomAbilityScores()), "young")
