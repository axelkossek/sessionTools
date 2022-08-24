import json
import os

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

