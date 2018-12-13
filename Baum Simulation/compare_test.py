#!/usr/bin/env python3
from Simulation import Simulation
from Tree import Tree
from Storage import saveSimulationToFile, readSimulationFromFile

t = Tree(20, 30)
t.age = 17
t.height = 5.21

sim1 = Simulation()
sim1.addtree(t)

#sim1.info()
saveSimulationToFile(sim1, "output/test.txt")

sim2 = readSimulationFromFile("output/test.txt")
#sim2.info()

sim3 = Simulation()
sim4 = Simulation()
sim4.addtreeat(10, 20)
sim4.addtreeat(30, 20)

print("sim1 vs. sim2:", sim1 == sim2)
print("empty Simulation vs. sim1:", sim1 == sim3)
print("empty Simulation vs. sim2:", sim1 == sim3)
print("different Simulation vs. sim2:", sim4 == sim3)
