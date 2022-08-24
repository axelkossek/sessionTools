import json
import random

class StatsRandomizer:
    def __init__(self, randomizationFilePath = "./RandomizationFiles/base_stats_distribution.json"):
        with open(randomizationFilePath, "r") as f:
            distribution = json.load(f)
        self.distro = []
        self.scores = []
        for dist in distribution['stats']:
            self.scores.append(dist[0])
            self.distro.append(dist[1])

    def AbilityDistribution(self, percentile):
        for i in range(len(self.distro)):
            if percentile < sum(self.distro[0:i+1]):
                return self.scores[i]
        print("Unexpected percentile: " + str(percentile))
        return 0

    def GenerateRandomAbilityScores(self):
        return [ self.AbilityDistribution(random.randint(0, sum(self.distro) - 1)) for i in range(0,6) ]

