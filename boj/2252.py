import sys

def read_input():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    dag = [[] for _ in range(n + 1)] 

    for _ in range(m):
        u, v = map(int, input().split())
        dag[u].append(v)

    return dag 

def dfs(graph):
    visited = set()
    res = [] 

    for u in range(1, len(graph)): 
        if u in visited:
            continue
        visited.add(u)
        dfs_search(u, graph, visited, res)
        
    return res

def dfs_search(u, graph, visited, res):
    for v in graph[u]:
        if v not in visited:
            visited.add(v)
            dfs_search(v, graph, visited, res)
    res.insert(0,u)

def main():
    dag = read_input()
    res = dfs(dag)
    print(*res)

if __name__ == '__main__':
    main()