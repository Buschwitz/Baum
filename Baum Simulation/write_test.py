#!/usr/bin/env python3
from Simulation import Simulation
from Tree import Tree
from Storage import saveSimulationToFile

sim = Simulation()
sim.addtreeat(20, 20)
saveSimulationToFile(sim, "output/test_year0.txt")

sim.step(50)
saveSimulationToFile(sim, "output/test_year50.txt")

sim.step(100)
saveSimulationToFile(sim, "output/test_year100.txt")
