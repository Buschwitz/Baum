import random
from Tree import Tree

class Simulation:
    def __init__(self):
        self.trees = []
        self.grid = []
        for x in range(100):
            row = []
            for y in range (100):
                row.append (None)
                
            self.grid.append(row)
            
        self.year = 0

    def __repr__(self):
        return "Simulation Anzahl der Bäume = %d,  Anzahl der Jahre = %d" % (len(self.trees), self.year)

    def __len__(self):
        return len(self.trees)
    
    def isfree(self, x, y):
        return self.treeat(x, y) is None

    def treeat(self, x, y):
        return self.grid[y][x]

    """
        for t in self.trees:
            if t.x==x and t.y==y:
                return t

        return None
    """
    
    def addtreeat(self, x, y):
        t = Tree(x, y)
        self.addtree(t)
        
    def addtree(self, t):
        #print ("add", t)
        self.trees.append(t)
        self.grid[t.y][t.x] = t
        
    def reset(self):
        self.trees = []
        self.addtreeat(50, 50)

    def agetree(self):
        agetree = [] # kein Unterschied?, warum alle ages = 0?
        ages = [t.age for t in self.trees]
        
        for t in self.trees:
            agetree.append(ages.count(t.age))

        print(ages)
        print (agetree)

        lastage = None # außerhalb der Schleife unten
        
        for age, count in zip(ages, agetree):
            if lastage != age:
                print(age, "kommt", count, "mal vor")
                
            lastage = age
 
    def flash(self):
        # bei Negativformulierung: or statt and: not(a and b) == not a or not b
        if self.year %5 != 0 or self.year < 15:                                             
            return
        
        if random.random()>0.1:
            return

        if len(self.trees) == 0:
            return

        
        index=random.randint(0, len(self.trees)-1)
        t=self.trees[index]
        t.flash = True
        t.dead = True
        print ("%d, Blitz eingeschlagen: %s" % (self.year, t.info()))

    def step(self, stepyears=1):
        for i in range (stepyears):      # i mal = Anzahl der Jahre
            self.stepyear()

    def stepyear(self):
        #self.flash()
        
        seeds = self.steptrees()

        for s in seeds:
            self.addtree(s)

        self.year += 1

    def steptrees(self):
        seeds = []
        for t in self.trees:
            if t.dead:
                t.decay += 1
                if t.decay >= 20:
                    self.removetree(t)
                    
                continue
            
            t.height += 1
            t.age += 1
            if t.age > 10 and t.age < 50 and t.age % 20 == 0:
                sx=t.x+random.randint(-2, 2)
                sy=t.y+random.randint(-3, 3)
                if sx < 0 or sy < 0 or sx >= 100 or sy >= 100:
                    #print ("Samen verloren")
                    pass
                elif self.isfree(sx, sy):
                    seeds.append(Tree(sx, sy))          # append = fügt ein Element dran

            if t.age >= 100:
                if random.random()<0.01:
                    t.dead=True

        return seeds

    def removetree(self, t):
        index = self.trees.index(t)
        #print ("remove:", t, index)
        del(self.trees[index])
        self.grid[t.y][t.x] = None

        
    def info(self):
        for t in self.trees:
            print("Baum mit Alter", t.age, "und Höhe", t.height,"Baum tot", t.dead, t.x, t.y)

    def draw(self):
        if len(self.trees) == 0:
            return
        
        pad = 0
        xfrom = min([t.x for t in self.trees]) - pad
        xto = max([t.x for t in self.trees]) + 1 + pad
        yfrom = min([t.y for t in self.trees]) - pad
        yto = max([t.y for t in self.trees]) + 1 + pad
        
        for y in range(yfrom, yto):
            for x in range(xfrom, xto):
                t = self.treeat(x, y)
                if t is None:
                    symbol = "."
                elif t.dead:
                    symbol = "o"
                elif t.age < 15:
                    symbol = "r"
                else:
                    symbol = "T"
                    
                print(symbol, end="")

            print("")
