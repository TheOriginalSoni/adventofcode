class DSU:
    #Disjoint set union, implementation copied from https://github.com/stevenhalim/cpbook-code/blob/master/ch2/ourown/unionfind_ds.py
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.numdisjoint = n

    def find(self, x):
        xp = x
        children = []
        while xp != self.parents[xp]:
            children.append(xp)
            xp = self.parents[xp]
        for c in children:
            self.parents[c] = xp
        return xp

    def union(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
            return

        if self.ranks[ap] < self.ranks[bp]:
            self.parents[ap] = bp
            self.sizes[bp] += self.sizes[ap]
        elif self.ranks[bp] < self.ranks[ap]:
            self.parents[bp] = ap
            self.sizes[ap] += self.sizes[bp]
        else:
            self.parents[bp] = ap
            self.ranks[ap] += 1
            self.sizes[ap] += self.sizes[bp]

        self.numdisjoint -= 1

    def size(self, x):
        return self.sizes[self.find(x)]

'''
u = DSU(10)
print(u.numdisjoint == 10)
u.union(1,2)
print(u.find(1) == u.find(2))
print(u.find(1) != u.find(3))
print(u.size(1))                #2
print(u.parents)                #[0, 1, 1, 3, 4, 5, 6, 7, 8, 9]
print(u.ranks)                  #[0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
print(u.sizes)                  #[1, 2, 1, 1, 1, 1, 1, 1, 1, 1]
print(u.numdisjoint)            #9
'''