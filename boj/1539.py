import sys
import bisect 

sys.setrecursionlimit(300000)   

class QuasiNode:
    def __init__(self, key, depth):
        self.key = key
        self.depth = depth

    def __lt__(self, comp):
        return self.key < comp.key

class QuasiBinarySearchTree:
    def __init__(self):
        self.data = []
        self.cnt = 0

    def __len__(self):
        return len(self.data)
    
    def parent(self, node):
        pos = bisect.bisect_left(self.data, node)

        if pos == 0:
            right = 1
            left = 0
        else:
            left = pos - 1
            right = pos
                
        max_depth = 0 
        if len(self) > left and left >= 0:
            max_depth = max(max_depth, self.data[left].depth)
        if len(self) > right and pos != 0:
            max_depth = max(max_depth, self.data[right].depth)
        return max_depth, pos

    def insert(self, x):
        node = QuasiNode(x, 0)
        depth, pos = self.parent(node)
        node.depth = (depth+1)
        self.data.insert(pos, node)

        self.cnt += node.depth


def read_input():
    input = sys.stdin.readline

    n = int(input())
    q = []
    for _ in range (n):
        query = int(input())
        q.append(query)
    return q

def main():
    q = read_input()
    bst = QuasiBinarySearchTree()

    for x in q:
        bst.insert(x)
    
    print(bst.cnt)

if __name__ == '__main__':
    main()