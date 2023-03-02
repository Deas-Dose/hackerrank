#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    #print all the moves here
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                u_pos = (i,j)
            if grid[i][j] == 'p':
                p_pos = (i,j)
    x_off = u_pos[0] - p_pos[0]
    # print(x_off)
    y_off = u_pos[1] - p_pos[1]
    # print(y_off)
    x_dir = 'LEFT\n' * y_off if y_off > 0 else 'RIGHT\n' * -y_off
    y_dir = 'UP\n' * x_off if x_off > 0 else 'DOWN\n' * -x_off
    print(x_dir,y_dir)


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)