import sys

sys.setrecursionlimit(300000)   

class Graph:
    def __init__(self, v, s = None, direct=False, key_init=0):
        self._v = range(1, v+1)
        self._edge = [[] for _ in range(v + 1)]
        self.direct = direct 
        self._key = [key_init for _ in range(v+1)]
        if s:
            self._key[s] = 0
    
    def V(self):
        return self._v
    
    def E(self):
        edges = []
        for u, edge_u in enumerate(self._edge):
            for v, w in edge_u:
                edges.append((u,v,w))
        return edges 
    
    def relax(self, x, y, w):
        if self._key[x] + w < self._key[y]:
            self._key[y] = self._key[x] + w
            return True
        return False

    def key(self):
        return self._key[1:].copy()

    def add_edge(self, x, y, w=0):
        self._edge[x].append((y,w))
        if not self.direct:
            self._edge[y].append((x,w))
    
    def adj(self, u):
        return self.edge[u]

def read_input():
    input = sys.stdin.readline

    v, e = map(int, input().split())
    G = Graph(v, s=1, direct=True, key_init=float('inf'))

    for _ in range(e):
        x, y, w = map(int, input().split())
        G.add_edge(x,y,w)

    return G

def bellman_ford(G):
    for i in range(len(G.V())):
        for u, v, w in G.E():
            G.relax(u,v,w)
    for u,v,w in G.E():
        if G.relax(u,v,w):
            return False
    return True
                

def main():
    ans = []
    G = read_input()
    
    res = bellman_ford(G)

    if res:
        ans = G.key()[1:]
    else:
        ans = [-1]
    
    for a in ans:
        if a == float('inf'):
            print(-1)
        else:
            print(a)
            
if __name__ == '__main__':
    main()