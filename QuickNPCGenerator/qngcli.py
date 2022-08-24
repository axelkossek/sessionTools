from sessionmanager import SessionManager
from statsrandomizer import StatsRandomizer

def GenerateNPCDict(name, family, race, occupation, stats, appearance):
    return {
        'name' : name,
        'family' : family,
        'race' : race,
        'occupation' : occupation,
        'stats' : stats,
        'appearance' : appearance
        }

def GenerateStatsDict(abilityscores):
    return {
        'str' : abilityscores[0],
        'dex' : abilityscores[1],
        'con' : abilityscores[2],
        'int' : abilityscores[3],
        'wis' : abilityscores[4],
        'cha' : abilityscores[5]
        }

fileS = "test_1.json";
manager = SessionManager(sessionFile = fileS, campaignName = "test", sessionNumber = 1)

#enpec1 = GenerateNPCDict("John", "Smith", "Human", "Smith", GenerateStatsDict(GenerateRandomAbilityScores()), "old")
#enpec2 = GenerateNPCDict("Jane", "Novak", "Elf", "Wizard", GenerateStatsDict(GenerateRandomAbilityScores()), "young")

statsRand = StatsRandomizer()
scores = GenerateStatsDict(statsRand.GenerateRandomAbilityScores())
