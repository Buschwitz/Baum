from Simulation import Simulation
from Tree import Tree

def saveSimulationToFile(sim, filename):
    f = open(filename, "w")
    f.write("# tree simulation v0.1\n")
    for t in sim.trees:
        f.write("tree %d %d %f %d %d %d %d\n" % (t.x, t.y, t.height, t.age, t.decay, int(t.dead), int(t.flash)))

    f.close()

def readSimulationFromFile(filename):
    try:
        f = open(filename)
        lines = f.read().split("\n")
        f.close()
    except Exception as e:
        print("failed to open/read simulation filename '%s'" % filename)
        raise e

    sim = Simulation()

    for line in lines:
        if line.startswith('#'):
            # ignore comments
            continue

        if line == "":
            # ignore empty lines
            continue

        if line.startswith('tree '):
            s = line.split(" ")
            s = s[1:] # drop the first string 'tree'
            if len(s) != 7:
                raise ValueError("cannot read tree from line '%s'. need 7 components" % line)

            try:
                x = int(s[0])
                y = int(s[1])
                height = float(s[2])
                age = int(s[3])
                decay = int(s[4])
                dead = bool(int(s[5]))
                flash = bool(int(s[6]))
            except Exception as e:
                print("cannot read tree from line '%s'")
                raise e

            try:
                tree = Tree(x, y)
                tree.height = height
                tree.age = age
                tree.decay = decay
                tree.dead = dead
                tree.flash = flash

            except Exception as e:
                print("cannot create tree")
                raise e

            try:
                sim.addtree(tree)
            except Exception as e:
                print("cannot add tree to simulation")
                raise e
        else:
            raise ValueError("invalid in simulation file: '%s'" % line)

    return sim
