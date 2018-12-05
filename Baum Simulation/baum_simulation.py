#!/usr/bin/env python3
import sys

from Simulation import Simulation
from Tree import Tree

s = Simulation()

def main():
    s.reset()
    totalYears = 200
    maxStep = 100

    # parse the total years from command line argument #1 (if set)
    if len(sys.argv) > 1:
        totalYears = int(sys.argv[1])

    print("simulate %d years (one step = %d years)" % (totalYears, maxStep))

    while totalYears > 0:
        step = min(maxStep, totalYears)
        s.step(step)
        totalYears -= maxStep
        print(".", end="", flush=True)

    print("Done!")

    s.draw()

def test():
    t = Tree(50, 50)
    t.age = 50
    s.addtree(t)

    t = Tree (20, 20)
    t.age = 50
    s.addtree(t)
    
    s.step(30)
    s.draw()


main()

#s.agetree()
