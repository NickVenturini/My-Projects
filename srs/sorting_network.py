#! /usr/bin/python3
import math
import copy
from random import randint
# NUM_INPUTS        | 1 | 2 | 3 | 4 | 5 |  6 |  7 |
# NUM_COMPARATORS   | 0 | 1 | 3 | 5 | 9 | 12 | 16 |

NUM_INPUTS      = 3
NUM_COMPARATORS = 3

def is_sorted(array):
    """
        Returns True if array is sorted, otherwise False
    """
    for i in range(1,len(array)):
        if array[i] < array[i-1]:
            return False

    return True

def generate_evaluation_cases(): #NEED TO STORE AS A LIST OF LISTS
    """
        Returns a list of all possible unsorted lists of size NUM_INPUTS
        that contain only 0's and 1's.

        Example:
            NUM_INPUTS = 2, [[1,0]]
            NUM_INPUTS = 3, [[0,1,0],[1,0,0],[1,0,1],[1,1,0]]

        Hint: Think binary numbers
    """
    unsorted_lists = []
   
    for number in range(0, 2**NUM_INPUTS):    #from 0 to all possible combos
        bnumber = int(("{:0%db}"%NUM_INPUTS).format(number))   #create binary number
        bnumber = '{numbers:0{width}d}'.format(width=NUM_INPUTS, numbers=bnumber)
        for index in range(NUM_INPUTS-1, 0, -1):       #go through all bits
            mylist = []
            if bnumber[index] < bnumber[(index-1)]:    #if the bit is less than the one to its left
                for a in range(0,NUM_INPUTS):          #go through entire case length
                    mylist.append(bnumber[a])          #append each bit of the case to the list
                unsorted_lists.append(mylist)          #append the list of bits to the list of cases

    return unsorted_lists

class SortingNetwork:
    EVALUATION_CASES = generate_evaluation_cases()

    def __init__(self):
        """
            Creates a random sorting network with NUM_COMPARATORS comparators
            to sort an array of size NUM_INPUTS

            Note: For all comparators (x,y), x < y

            Example:
                (0,2) => correct
                (4,0) => incorrect
                (1,1) => incorrect

            Note: Consecutive comparators in list shouldn't be the the same

            Example:
                [(0,1),(0,2),(1,2)] => correct
                [(0,3),(0,3),(0,2)] => incorrect
                [(0,3),(0,2),(0,3)] => correct
        """
        self.comparators = []
        temp = str('00')
        index = 0
        while index <NUM_COMPARATORS:
            x = randint(0, NUM_INPUTS-2)
            y = randint(x+1, NUM_INPUTS-1)
            z = (str(x) + str(y))
            if z == temp:
                index = index-1
            else:
                self.comparators.append(z)
            index=index+1
            temp = z

    def __str__(self):
        return str(self.comparators)

    def apply_on(self, array):
        """
            Uses the sorting network to (try to) sort the array
        """
        temp=0;
        for comp in range(0, NUM_COMPARATORS): #for each comparitor
            comp1=int(self.comparators[comp][0])
            comp2=int(self.comparators[comp][1])
            if array[comp1] > array[comp2]:
                temp = array[comp1]
                array[comp1] = array[comp2]
                array[comp2] = temp
        return array


    def evaluate(self):
        """
            Evaluate sorting network over each case in EVALUATION_CASES.
            Returns the percentage that the sorting network correctly sorts.

            WARNING: Do not modify the evaluation cases
        """
        if len(self.EVALUATION_CASES) == 0:
            return 100
        evalcopy = copy.deepcopy(self.EVALUATION_CASES)
        sorted_lists = 0
        for i in evalcopy:    #from 0 to all possible combos
            if is_sorted(self.apply_on(i)):
                sorted_lists = sorted_lists+1

        return (100.0*sorted_lists/len(self.EVALUATION_CASES))

if __name__ == "__main__":
    network = SortingNetwork()
    percent_correct = network.evaluate()

    print(str(percent_correct) + "% of possible inputs sorted correctly")
    #print("AFTER EVALUATING---------------------")
   


