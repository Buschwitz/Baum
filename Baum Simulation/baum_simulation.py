print("start")

from Simulation import Simulation
from Tree import Tree
s = Simulation()

def main():
    s.reset()
    s.step(50)
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

s.agetree()
