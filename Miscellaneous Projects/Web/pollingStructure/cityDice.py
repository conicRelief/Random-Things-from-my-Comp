import random
class unfairDice:
    # This class exists as an unfair die. that returns city names. The distribution of city names is modeled off of
    # internet usage statistics for Europe taken from http://www.internetworldstats.com/europa.html
    def __init__(self):
        f = open("internetUsageStatistics")
        self.sum_off_populations = 0
        self.cityToPoluation = {}
        self.populationToCity = {}
        for entry in f:
            city, population = entry.replace('\n',"").split(" ")
            population = population.replace(",","")
            self.sum_off_populations = self.sum_off_populations + int(population)
            self.cityToPoluation[city] = population
            self.populationToCity[population] = city
        f.close()

    def __rollCityDice(self, pop, citPop,popCit):
        randRoll = random.random()*pop # in [0,1)
        sum = 0
        result = 0
        lastMass = 0
        for mass in popCit:
            lastMass = mass
            sum = sum +int(mass)
            if randRoll < sum:
                return popCit[mass]
            result+=1
        return popCit[lastMass]

    def getRandomCity(self):
        return self.__rollCityDice(self.sum_off_populations,self.cityToPoluation,self.populationToCity)
    def roll_dice_x_times(self, x):
        pollingTest = {}
        for x in xrange(x):
            name = self.__rollCityDice(self.sum_off_populations,self.cityToPoluation,self.populationToCity)
            if pollingTest.has_key(name):
                pollingTest[name] = int(pollingTest[name]) + 1
            else:
                pollingTest[name] = 0
        return pollingTest