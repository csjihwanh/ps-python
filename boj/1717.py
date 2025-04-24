import sys
sys.setrecursionlimit(300000)   

def read_input():
    input = sys.stdin.readline

    arr = []
    n, m = map(int, input().split())
    for _ in range(m):
        q, x, y = map(int, input().split())
        arr.append([q,x,y])

    return n, arr

def make_set(n):
    return [i for i in range(n+1)]

def find_set(x, p):
    if x == p[x]:
        return x
    p[x] = find_set(p[x], p)
    return p[x]
    
def union(x, y, p):
    rx = find_set(x,p)
    ry = find_set(y,p)
    if rx == ry:
        return
    p[ry] = rx 

def main():
    n, task = read_input()
    res = []

    p = make_set(n)

    for q, x, y in task:
        if q == 0:
            union(x,y,p)
        else:
            rx = find_set(x,p)
            ry = find_set(y,p)
            if rx == ry:
                res.append("YES")
            else:
                res.append("NO")
    
    for ans in res:
        print(ans)

if __name__ == '__main__':
    main()
