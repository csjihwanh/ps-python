import sys
import heapq
sys.setrecursionlimit(300000)   

class Graph:
    def __init__(self, v, direct=False, key_init=0):
        self.edge = [[] for _ in range(v + 1)]
        self.direct = direct 
        self._key = [key_init for _ in range(v+1)]

    def add_edge(self, x, y, w=0):
        self.edge[x].append((y,w))
        if not self.direct:
            self.edge[y].append((x,w))
    
    def adj(self, u):
        return self.edge[u]

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

    v = int(input())
    e = int(input())
    G = Graph(v)

    for _ in range(e):
        x, y, w = map(int, input().split())
        G.add_edge(x,y,w)

    return G

def prim(G):
    sum = 0
    s = 1
    node = set()
    pq = PriorityQueue((0, (s,s)))

    while pq:
        w_u, (_,u) = pq.pop()
        if u in node:
            continue
        node.add(u)
        sum += w_u
        
        # update adj 
        for v, w_uv in G.adj(u):
            pq.push((w_uv, (u,v)))

    return sum
    
def main():
    G = read_input()
    res = prim(G)
    print(res)

if __name__ == '__main__':
    main()
