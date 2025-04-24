import sys
import heapq
sys.setrecursionlimit(300000)   

class Union:
    def __init__(self, n):
        self.p = self._make(n)

    def _make(self, n):
        return [i for i in range(n+1)]

    def find(self, x):
        if x == self.p[x]:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        self.p[ry] = rx 
    
    def is_set(self, x, y):
        return self.find(x) == self.find(y)

def read_input():
    input = sys.stdin.readline

    v, e = map(int, input().split())
    pq = []

    for _ in range(e):
        x, y, w = map(int, input().split())
        heapq.heappush(pq, (w, (x,y)))

    return v, pq 

def kruskal(pq, U):
    sum = 0

    while pq:
        w, (x,y) = heapq.heappop(pq)
        if U.is_set(x,y):
            continue
        sum += w
        U.union(x,y)

    return sum 

def main():
    v, pq = read_input()
    U = Union(v)
    
    ans = kruskal(pq, U)
    print (ans)

if __name__ == '__main__':
    main()
