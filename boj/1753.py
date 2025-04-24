import sys
import heapq

sys.setrecursionlimit(300000)   

class Graph:
    def __init__(self, v, s = None, direct=False, key_init=0):
        self._v = range(1, v+1)
        self._edge = [[] for _ in range(v + 1)]
        self._key = [key_init for _ in range(v+1)]
        self._weight = {}
        self.direct = direct 
        if s:
            self._key[s] = 0

    def _w_update(self, key, value):
        if key in self._weight:
            self._weight[key] = min(self._weight[key], value)
        else:
            self._weight[key] = value

    def w(self, key):
        return self._weight[key]

    def V(self):
        return self._v
    
    def relax(self, x, y, w):
        if self._key[x] + w < self._key[y]:
            self._key[y] = self._key[x] + w
            return True
        return False

    def key(self, x):
        return self._key[x]

    def add_edge(self, x, y, w=0):
        self._edge[x].append(y)
        self._w_update((x,y), w)
    
    def adj(self, u):
        return self._edge[u]
    
class PriorityQueue:
    def __init__(self, value):
        self._data = []
        heapq.heappush(self._data, value)
    
    def __len__(self):
        return len(self._data)

    def push(self, value):
        heapq.heappush(self._data, value)
    
    def pop(self):
        return heapq.heappop(self._data)

def read_input():
    input = sys.stdin.readline

    v, e = map(int, input().split())
    s = int(input())
    G = Graph(v, s=s, direct=True, key_init=float('inf'))

    for _ in range(e):
        x, y, w = map(int, input().split())
        G.add_edge(x,y,w)

    return G, s

def dijkstra(G,s):
    pq = PriorityQueue((G.key(s),s))
    visited = set()
    res = []

    while pq:
        _, u = pq.pop()
        visited.add(u)
        for v in G.adj(u):
            if v not in visited:
                if G.relax(u, v, G.w((u,v))):
                    pq.push((G.key(v), v))
        
    for v in G.V():
        res.append(G.key(v))
    
    return res 

def main():
    ans = []
    G, s = read_input()
    
    res = dijkstra(G,s)

    for ans in res:
        if ans == float('inf'):
            print("INF")
        else:
            print(ans)
            
if __name__ == '__main__':
    main()