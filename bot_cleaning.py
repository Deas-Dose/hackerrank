#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    # create a list to store all dirty positions
    d_pos = []
    # loop through the whole board to find the dirty positions
    for i in range(len(board)):
        for j in range(len(board)):
            # add the dirty position to the list if stambled on a dirty pos
            if board[i][j] == 'd':
                d_pos.append((i,j))
    # main stuff
    for pos in d_pos:
        x_diff = posr - pos[0]
        y_diff = posc - pos[1]
        for i in range(abs(x_diff)):
            for j in range(abs(y_diff)):
                if x_diff:
                    print('DOWN\n' if x_diff < 0 else 'UP\n')
                    posr = posr + 1 if x_diff < 0 else posr - 1
                if y_diff:
                    print('RIGHT\n' if y_diff < 0 else 'LEFT\n')
                    posc = posc + 1 if y_diff < 0 else posc - 1
                if board[posr][posc] == 'd':
                    print('CLEAN\n')
                    x_diff = posr - pos[0]
                    y_diff = posc - pos[1]
                    break
                x_diff = posr - pos[0]
                y_diff = posc - pos[1]
    

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)