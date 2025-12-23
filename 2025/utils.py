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

INF = 10**18
class Min_Cost_Max_Flow:

    def __init__(self, V):
        self.V = V
        self.EL = []
        self.AL = [list() for _ in range(V)]
        self.vis = [False] * V
        self.total_cost = 0
        self.d = None
        self.last = None

    def SPFA(self, s, t):
        self.d = [INF] * self.V
        self.d[s] = 0
        self.vis[s] = True
        q = [s]
        while len(q) != 0:
            u = q[0]
            q.pop(0)
            self.vis[u] = False
            for idx in self.AL[u]:
                v, cap, flow, cost = self.EL[idx]
                if cap-flow > 0 and self.d[v] > self.d[u]+cost:
                    self.d[v] = self.d[u]+cost
                    if not self.vis[v]:
                        q.append(v)
                        self.vis[v] = True
        return self.d[t] != INF

    def DFS(self, u, t, f=INF):
        if u == t or f == 0:
            return f
        self.vis[u] = True
        for i in range(self.last[u], len(self.AL[u])):
            v, cap, flow, cost = self.EL[self.AL[u][i]]
            if not self.vis[v] and self.d[v] == self.d[u]+cost:
                pushed = self.DFS(v, t, min(f, cap-flow))
                if pushed != 0:
                    self.total_cost += pushed * cost
                    flow += pushed
                    self.EL[self.AL[u][i]][2] = flow
                    rv, rcap, rflow, rcost = self.EL[self.AL[u][i]^1]
                    rflow -= pushed
                    self.EL[self.AL[u][i]^1][2] = rflow
                    self.vis[u] = False
                    self.last[u] = i
                    return pushed
        self.vis[u] = False
        return 0

    def add_edge(self, u, v, w, c, directed=True):
        if u == v:
            return
        self.EL.append([v, w, 0, c])
        self.AL[u].append(len(self.EL)-1)
        self.EL.append([u, 0 if directed else w, 0, -c])
        self.AL[v].append(len(self.EL)-1)

    def mcmf(self, s, t):
        mf = 0
        while self.SPFA(s, t):
            self.last = [0] * self.V
            f = self.DFS(s, t)
            while f != 0:
                mf += f
                f = self.DFS(s, t)
        return mf, self.total_cost

'''
V=3 #number of vertexes
E=3 #number of edges
s=0 #number for source
t=2 #number for sink
mf = Min_Cost_Max_Flow(V)
uvwc = [[0,1,2,1],[1,2,2,1],[0,2,1,1]]
for i in range(E):
    u, v, w, c = uvwc[i] #starting vertex, ending vertex, width, cost
    mf.add_edge(u, v, w, c)
res = mf.mcmf(s, t) #max flow, min cost
print('%d %d' % (res[0], res[1]))
'''