#! /usr/bin/python3
import random
import copy
from sorting_network import SortingNetwork, NUM_COMPARATORS, NUM_INPUTS

POPULATION_SIZE = 1000 #MUST BE DIVISIBLE BY 2

class Individual:
    def __init__(self):
        """
            Creates a new Individual
        """
        self.network = SortingNetwork()
        self.fitness = 0.0

    def __str__(self):
        return "Fitness: {: >6.2f}, Network: {}".format(self.fitness, self.network)

class Population:

    def __init__(self):
        """
            Creates a random population of individuals of size POPULATION_SIZE
        """
        self.individuals = [Individual() for i in range(POPULATION_SIZE)]

    def __str__(self):
        string = "Population:\n"
        for i in self.individuals:
            string += "   " + str(i) + "\n"
        return string

    def evaluate(self):
        """
            Determine the fitness of each individual in the population.
            Sort the population from high fitness to low fitness.
        """

        for i in self.individuals:
            i.fitness = i.network.evaluate()
        self.individuals = sorted(self.individuals, key = lambda individual: individual.fitness, reverse = True)
    def select(self):
        """
            Use Roulette Wheel to select individuals for next generation
            Always propagate the best 2 individuals to the next generation

            WARNING: Remember to deepcopy the individuals so you don't
            have two elements in self.individuals that are pointers to the
            same individual
        """
        tfitness = 0.0
        fit_list = []
        min_max_list = []
        mini=0.0
        tsum = 0
        selectPopulation = []
        for i in self.individuals:
            tfitness = tfitness + i.fitness #create total fitness
        for a in self.individuals:
            float(a.fitness)
            fit_list.append((a.fitness/tfitness)) #create % of fitness
            tsum = tsum+(a.fitness/tfitness)
        #for rem in range (1, POPULATION_SIZE-1):
           # selectPopulation.individuals.remove(rem)
        for index in range(0, len(fit_list)): #assign ranges to %'s
            
            min_max = []
            min_max.append(mini)
            min_max.append(mini + fit_list[index])
            min_max_list.append(min_max)
            mini = mini+fit_list[index]
        #print(min_max_list)
        count = 0
        while count<POPULATION_SIZE-2:
            randomnumber = random.random()
            for b in range(0, len(fit_list)-1): #check who our lucky winner is
                if min_max_list[b][0] < randomnumber and min_max_list[b][1] >= randomnumber:
                    selectPopulation.append(copy.deepcopy(self.individuals[b]))
                    count = count +1
                    break
            
        selectPopulation.append(copy.deepcopy(self.individuals[0]))
        selectPopulation.append(copy.deepcopy(self.individuals[1]))
        self.individuals = selectPopulation
        #selectPopulation.individuals

    def crossover(self):
        """
            With probability CROSSOVER_RATE, perform uniform crossover.
            Otherwise, copy parents.

            Always propagate the best 2 individuals to the next generation

            WARNING: Ensure mutated comparators are still legal
                     (see SortingNetwork __init__)
        """
        #xPopulation = Population()

        xpopulation = []
        CROSSOVER_RATE = .75
        for i in range(0, len(self.individuals)-2):
            temp = []
            check = 9999999
            while True:
                parent1=random.randint(0, POPULATION_SIZE-1)
                parent2=random.randint(0, POPULATION_SIZE-1)
                if parent1==parent2:
                    break
            for a in range(0, NUM_COMPARATORS):
                rn = random.random()
                if rn<CROSSOVER_RATE: #use parent 1
                    if check == self.individuals[parent1].network.comparators[a]:#if we get repeat
                        temp.append(self.individuals[parent2].network.comparators[a])#use other parent
                        check = self.individuals[parent2].network.comparators[a]
                    else:
                        temp.append(self.individuals[parent1].network.comparators[a])
                        check = self.individuals[parent1].network.comparators[a]
                else: #use parent 2
                    if check == self.individuals[parent2].network.comparators[a]:
                        temp.append(self.individuals[parent1].network.comparators[a])
                        check = self.individuals[parent1].network.comparators[a]
                    else:
                        temp.append(self.individuals[parent2].network.comparators[a])
                        check = self.individuals[parent2].network.comparators[a]
            xpopulation.append(temp)
        self.individuals = sorted(self.individuals, key = lambda individual: individual.fitness, reverse = True)
        xpopulation.append(self.individuals[0].network.comparators)
        xpopulation.append(self.individuals[1].network.comparators)
        #print(xpopulation)
        for k in range(0, len(self.individuals)-2):
            self.individuals[k].network.comparators = xpopulation[k]

    def mutate(self):
        """
            With probability MUTATION_RATE, mutate the individual's network

            WARNING: Ensure mutated comparators are still legal
                     (see SortingNetwork __init__)
        """
        MUTATION_RATE  = 1/NUM_COMPARATORS
        a =0
        for i in range(0, POPULATION_SIZE):
            for a in range(0, NUM_COMPARATORS):
                randy = random.random()
                if  randy< MUTATION_RATE:
                    while (a-1 >= 0 and self.individuals[i].network.comparators[a-1] == self.individuals[i].network.comparators[a]) or (a+1 < NUM_COMPARATORS and self.individuals[i].network.comparators[a+1] == self.individuals[i].network.comparators[a]):
                        x = randint(0, NUM_INPUTS-2)
                        y = randint(x+1, NUM_INPUTS-1)
                        z = (str(x) + str(y))
                        self.individuals[i].network.comparators[a] = z
                    #print("THIS THING WORKED HERE")
                    #print(self.individuals[i].network.comparators[a])
                    #print(tempnetwork.comparators[a])
        ### FILL THIS IN ###

def run_genetic_algorithm():
    """
        Runs a genetic algorithm to find a sorting network with
        NUM_COMPARATORS comparators that sorts all possible arrays
        of size NUM_INPUTS
    """

    print(str(myPopulation))
    myPopulation.evaluate()
    #print("AFTER EVALUATE")
    #print(str(myPopulation))
    myPopulation.select()
    #print("AFTER SELECT")
    #print(str(myPopulation))
    myPopulation.crossover()
    #print("AFTER CROSSOVER")
    #print(str(myPopulation))
    myPopulation.mutate()

    
    #print("AFTER MUTATE")

    ### FILL THIS IN ###
    

if __name__ == "__main__":

    myPopulation = Population()
    for a in range(0, 150):
        run_genetic_algorithm()
    #print(str(myPopulation))
