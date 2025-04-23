import sys
sys.setrecursionlimit(300000)   

def read_input():
    input = sys.stdin.readline

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    return n, k, arr

class Swapper:
    def __init__(self, k):
        self.cnt = 0
        self.k = k

    def __call__(self, i, j, arr):
        self.cnt += 1
        if self.cnt == self.k:
            self.res = sorted([arr[i], arr[j]])
        self._swap(i,j,arr)

    def _swap(self, i, j, arr):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def out(self):
        if self.k > self.cnt:
            return [-1]
        else:
            return self.res

def partition(l, r, arr, swap):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            swap(i, j, arr)
            i += 1 
    if i != r:
        swap(i, r, arr)
    return i 

def quicksort(l, r, arr, swap):
    if l < r:
        p = partition(l,r, arr, swap)
        quicksort(l, p-1, arr, swap)
        quicksort(p+1, r, arr, swap)

def main():
    n, k, arr = read_input()
    swap = Swapper(k)
    quicksort(0, n-1, arr, swap)
    print (*swap.out())

if __name__ == '__main__':
    main()