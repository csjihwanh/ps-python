import sys
from collections import deque

def read_input():
    args = sys.stdin.readline

    n, m, s = map(int, input().split())
    graph = [[] for _ in range(n + 1)] 

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for adj in graph:
        adj.sort()

    return n, m, s, graph 

def dfs(s, graph):
    visited = set()
    visited.add(s)

    tr = []
    dfs_search(s, graph, visited, tr)
    return tr

def dfs_search(u, graph, visited, tr):
    tr.append(u)
    for v in graph[u]:
        if v not in visited:
            visited.add(v)
            dfs_search(v, graph, visited, tr)

def bfs(s, graph):
    visited = set() 
    visited.add(s) 
    q = deque()
    q.append(s) 

    tr = []
    while q:
        u = q.popleft()
        tr.append(u)
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)

    return tr 

def main():
    n, m, s, graph = read_input()
    dfs_tr, bfs_tr = [], []
    
    dfs_tr = dfs(s, graph)
    bfs_tr = bfs(s, graph)
    print(*dfs_tr)
    print(*bfs_tr)

if __name__ == '__main__':
    main()