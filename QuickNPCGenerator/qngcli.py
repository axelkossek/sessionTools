import argparse
from sessionmanager import SessionManager
from statsrandomizer import StatsRandomizer
import json

RACES_FILE_DEFAULT = "RandomizationFiles/races.json"
OCCUPATION_FILE_DEFAULT = "RandomizationFiles/occupations.json"

def GenerateNPCDict(name, family, race, occupation, stats, appearance):
    return {
        'name' : name,
        'family' : family,
        'race' : race,
        'occupation' : occupation,
        'stats' : stats,
        'appearance' : appearance
        }

def GenerateScoresDict(scores):
    return {
        'str' : scores[0],
        'dex' : scores[1],
        'con' : scores[2],
        'int' : scores[3],
        'wis' : scores[4],
        'cha' : scores[5]
        }

def ApplyRacialBonuses(scores, race, racesFile = RACES_FILE_DEFAULT):
    with open(racesFile, "r") as f:
            races = json.load(f)
    return [sum(tup) for tup in zip(scores, races[race]["score_bonuses"])]

def ApplyOccupationBonuses(scores, occupation, occupationFile = OCCUPATION_FILE_DEFAULT):
    with open(occupationFile, "r") as f:
            occupations = json.load(f)
    return [sum(tup) for tup in zip(scores, occupations[occupation]["score_bonuses"])]



#fileS = "test_1.json";
#manager = SessionManager(sessionFile = fileS, campaignName = "test", sessionNumber = 1)

##enpec1 = GenerateNPCDict("John", "Smith", "Human", "Smith", GenerateStatsDict(GenerateRandomAbilityScores()), "old")
##enpec2 = GenerateNPCDict("Jane", "Novak", "Elf", "Wizard", GenerateStatsDict(GenerateRandomAbilityScores()), "young")

def main():
    parser = argparse.ArgumentParser(description = "A npc generator!")

    parser.add_argument("-s", "--scores", type = str, nargs = 1,
                        metavar = "0,0,0,0,0,0", default = None,
                        help = "Set scores instead of random.")

    parser.add_argument("-r", "--race", type = str, nargs = 1,
                        metavar = "race", default = None,
                        help = "Chooses race for the generator.")
    
    parser.add_argument("-o", "--occupation", type = str, nargs = 1,
                        metavar = "occupation", default = "commoner",
                        help = "Chooses race for the generator.")

    args = parser.parse_args()

    statsRand = StatsRandomizer()
    scores = statsRand.GenerateRandomAbilityScores()

    if args.scores != None:
        scores = [int(i) for i in args.scores[0].split(',')]
    if args.race != None:
        scores = ApplyRacialBonuses(scores, args.race[0])
    if args.occupation != None:
        scores = ApplyOccupationBonuses(scores, args.occupation[0])

    scoreDict = GenerateScoresDict(scores)
    print(scoreDict)

if __name__ == "__main__":
    main()
