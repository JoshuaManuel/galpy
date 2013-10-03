# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 07:05:40 2013

Genetic Algorithm class, written in Python.

__init__:
    initializes variables

save:
    save current state to a file /w extension ".ga"

trim:
    kill off last three

mutate:
    randomly mutate a player's genome


MUTATION GUIDELINES
Edited from the following url:

http://www.obitko.com/tutorials/genetic-algorithms/recommendations.php

Crossover rate generally should be high, about 80%-95%. (However some results show that for some problems crossover rate about 60% is the best.) 
On the other side, mutation rate should be very low. Best rates reported are about 0.5%-1%
It may be surprising, that very big population size usually does not improve performance of GA (in meaning of speed of finding solution). Good population size is about 20-30, however sometimes sizes 50-100 are reported as best. Some research also shows, that best population size depends on encoding, on size of encoded string. It means, if you have chromosome with 32 bits, the population should be say 32, but surely two times more than the best population size for chromosome with 16 bits. 


@author: jman
"""


class Ga:
    def __init__(self, best, pops=25, ps=-1, mchance=1):
        import random as r
        self.pops = pops
        self.pop = [[] for _ in range(self.pops)]
        self.mchance = mchance
        self.ps = ps
        self.best = best
        self.bottom = 32
        self.top = 127
        self.amtToTrim = .2
        print self.pop
        print self.pops
        
        if self.ps == -1:
            self.ps = len(self.best)
        
        for x in range(len(self.pop)):
            for a in range(self.ps):
                self.pop[x].append(str(unichr(r.randint(self.bottom,self.top)))) #Seed with all the common chars
        print self.pop
        print self.pops
        
    def save(self,filename):
        import cPickle as p
        try:
            filename += ".ga"
            p.dump(self, open(filename,"w"))
        except:
            return "Error: Couldn't save file"
            
    def load(self, filename):
        import cPickle as p
        try:
            filename += ".ga"
            self.pop = p.load(open(filename, "r"))
        except:
            return "Error: Couldn't load file"
        
    def trim(self, array): #Kill ~1/3 of population
        import math
        self.pops * self.amtToTrim
        a = int(math.floor(self.pops * self.amtToTrim))
        for x in range(0, a):
            self.pop.pop()
        if a == 0:
            self.pop.pop()
            
    def mutate(self, array):
        import random as r
        coord1 = r.randint(0, self.pops-1)
        coord2 = r.randint(0, self.ps-1)
        array[coord1][coord2] = str(unichr(r.randint(self.bottom,self.top)))
        return array
        
    def calculate(self):
        fitarray = [[] for _ in range(self.pops)]
        for x in range(0, self.pops):
            print "x =", x
            for y in range(0, x): # for x in best. THERE WE GO.
                print "y = " , y

a = Ga("Hi")
a.trim(a.pop)
a.calculate()

#if __name__ == "__main__":