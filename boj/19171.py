import sys
import math 

class Point:
    def __init__(self,x,y,z):
        self.x = []
        self.x.extend([x,y,z])

    def __str__(self):
        return str(self.x)

def read_input():
    input = sys.stdin.readline
    point = []
    for _ in range(3):
        x, y, z = map(int, input().split())
        point.append(Point(x,y,z))

    return point

def grad(c,p):
    dx = [0,0,0]
    for i in range(3): 
        dist = 0
        for j in range(3):
            dist += math.pow(c.x[j]-p[i].x[j], 2)
        if dist == 0:
            continue
        for j in range(3):
            dx[j] += ((c.x[j]-p[i].x[j])/math.sqrt(dist))
    return dx

def loss(c,p):
    sum = 0 
    for i in range(3):
        tmp = 0
        for j in range(3):
            tmp += math.pow(c.x[j]-p[i].x[j], 2)
        sum += math.sqrt(tmp)
    return sum 

def main():
    p = read_input()
    
    c = Point(0,0,0)
    a = loss(c, p)
    epoch = 1000000

    for step in range(epoch):
        if step % (epoch//30) == 0:
            a /= 10
        dx = grad(c,p)

        for i in range(3):
            c.x[i] -= a*dx[i]
        
    print(loss(c,p))
        
if __name__ == '__main__':
    main()
