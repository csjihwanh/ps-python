import sys

def read_input():
    input = sys.stdin.readline

    n = int(input())
    arr = [int(input()) for _ in range(n)]

    return n, arr

class Heap:
    def __init__(self):
        self._data = [] 

    def __len__(self):
        return len(self._data)

    @staticmethod 
    def _parent(idx):
        return (idx-1)// 2

    def _swap(self, i, j):
        temp = self._data[i]
        self._data[i] = self._data[j]
        self._data[j] = temp

    def _get(self, idx):
        if idx >= len(self):
            return float('-inf')
        elif idx < 0:
            return float('inf')
        return self._data[idx]

    def get_value(self):
        return self._data.copy()

    def max_heapify(self, idx):
        left = self._get(idx * 2 + 1)
        right = self._get(idx * 2 + 2)
        
        if left > right:
            max_idx = idx * 2 + 1
        else: 
            max_idx = idx * 2 + 2 
        
        if self._get(max_idx) > self._get(idx):
            self._swap(max_idx, idx)
            idx = max_idx
            self.max_heapify(idx)

    def insert(self, x):
        self._data.append(x)
        idx = len(self) - 1
        parent = self._parent(idx)

        while self._get(parent) < self._get(idx):
            self._swap(idx, parent)
            idx = parent 
            parent = self._parent(idx)
    
    def extract(self):
        if not self:
            return 0
        res = self._data[0]
        last = self._data.pop()
        if self: 
            self._data[0] = last
            self.max_heapify(0)
        return res 
            

def main():
    n, arr = read_input()
    heap = Heap()
    res = []

    for task in arr:
        if task == 0:
            res.append(heap.extract())
        else:
            heap.insert(task)

    for ans in res:
        print(ans)

if __name__ == '__main__':
    main()