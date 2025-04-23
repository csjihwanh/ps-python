import sys

def read_input():
    input = sys.stdin.readline

    n = int(input())
    arr = [int(input()) for _ in range(n)]

    return n, arr 

def merge(l, mid, r, arr):
    res = []
    lp = l
    rp = mid + 1

    while lp <= mid and rp <= r:
        if arr[lp] < arr[rp]:
            res.append(arr[lp])
            lp += 1
        else :
            res.append(arr[rp])
            rp += 1
    res.extend(arr[lp:mid+1])
    res.extend(arr[rp:r+1])
    return res

def merge_sort(l, r, arr):
    if l == r:
        return 
    
    mid = (r+l)//2
    merge_sort(l,mid,arr)
    merge_sort(mid+1, r, arr)
    res = merge(l,mid,r,arr)
    arr[l:r+1] = res 

def main():
    n, arr = read_input()
    merge_sort(0,n-1,arr)
    for i in arr:
        print(i)

if __name__ == '__main__':
    main()