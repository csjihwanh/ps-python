import sys
import math 

class Point:
    def __init__(self,x,y):
        self.x = []
        self.x.extend([x,y])
    
    def __len__(self):
        return len(self.x)

    def __str__(self):
        return str(self.x)

def read_input():
    input = sys.stdin.readline

    n = int(input())
    point = []
    for _ in range(n):
        x, y = map(int, input().split())
        point.append(Point(x,y))

    return n, point

def grad(n, c,p):
    dx = [0,0,0]
    for i in range(n): 
        dist = 0
        for j in range(len(c)):
            dist += math.pow(c.x[j]-p[i].x[j], 2)
        if dist == 0:
            continue
        for j in range(len(c)):
            dx[j] += ((c.x[j]-p[i].x[j])/math.sqrt(dist))
    return dx

def loss(n, c,p):
    sum = 0 
    for i in range(n):
        tmp = 0
        for j in range(len(c)):
            tmp += math.pow(c.x[j]-p[i].x[j], 2)
        sum += math.sqrt(tmp)
    return sum 

def main():
    n, p = read_input()

    c = Point(0,0)
    a = loss(n, c, p)
    epoch = 10000

    for step in range(epoch):
        if step % (epoch//30) == 0:
            a /= 10
        dx = grad(n,c,p)

        for i in range(len(c)):
            c.x[i] -= a*dx[i]
        
    print(round(loss(n,c,p)))
        
if __name__ == '__main__':
    main()
