import sys
sys.setrecursionlimit(300000)   

def read_input():
    input = sys.stdin.readline

    v, e = map(int, input().split())
    G = [[] for _ in range(v + 1)] 
    G_T = [[] for _ in range(v + 1)]

    for _ in range(e):
        u, v = map(int, input().split())
        G[u].append(v)
        G_T[v].append(u)

    return v, e, G, G_T 

def dfs(G, order=None):
    visited = set()
    post = [] 
    forest = []

    if not order:
        order = range(1, len(G))

    for u in order: 
        if u in visited:
            continue
        visited.add(u)
        tree = [u]
        dfs_search(u, G, visited, post, tree)
        tree.sort()
        forest.append(tree)

    return post, forest

def dfs_search(u, G, visited, post, tree):
    for v in G[u]:
        if v not in visited:
            visited.add(v)
            tree.append(v)
            dfs_search(v, G, visited, post, tree)
    post.append(u)

def main():
    v,e,G,G_T = read_input()
    
    post, _ = dfs(G) # post-order traversal 
    post.reverse()
    _, forest = dfs(G_T, post) # generate a forest by decreasing order of finishing time of vertices
    forest.sort(key=lambda x: x[0])

    print(len(forest))
    for scc in forest:
        scc.sort()
        print(*scc, -1)


if __name__ == '__main__':
    main()