import random
from enum import Enum
import time


TOTAL_SCORE = 0


class Piece(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4
    EMPTY = 0


def create_table(n, m):
    table = []
    for i in range(n):
        table.append([])
        for _ in range(m):
            table[i].append(Piece.EMPTY)
    return table


def print_table(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            print(table[i][j].value, end=" ")
        print()


def make_move(table, start_x, start_y, end_x, end_y):
    color_start = table[start_x][start_y]


    # 5 in a row
    try:
        if color_start == table[end_x][end_y - 2] and color_start == table[end_x][end_y - 1] and color_start == table[end_x][end_y + 1] and color_start == table[end_x][end_y + 2]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x][end_y + 1] = table[end_x][end_y + 2] = table[end_x][end_y - 1] = table[end_x][end_y - 2] = Piece.EMPTY
            return 50
    except IndexError:
        pass

    try:
        if color_start == table[end_x - 2][end_y] and color_start == table[end_x - 1][end_y] and color_start == table[end_x + 1][end_y] and color_start == table[end_x + 2][end_y]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x + 1][end_y] = table[end_x + 2][end_y] = table[end_x - 1][end_y] = table[end_x - 2][end_y] = Piece.EMPTY
            return 50
    except IndexError:
        pass

    # T
    try:
        if color_start == table[end_x - 1][end_y] and color_start == table[end_x + 1][end_y] and color_start == table[end_x][end_y - 1] and color_start == table[end_x][end_y - 2]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x - 1][end_y] = table[end_x + 1][end_y] = table[end_x][end_y - 1] = table[end_x][end_y - 2] = Piece.EMPTY
            return 30
    except IndexError:
        pass

    try:
        if color_start == table[end_x - 1][end_y] and color_start == table[end_x + 1][end_y] and color_start == table[end_x][end_y + 1] and color_start == table[end_x][end_y + 2]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x - 1][end_y] = table[end_x + 1][end_y] = table[end_x][end_y + 1] = table[end_x][end_y + 2] = Piece.EMPTY
            return 30
    except IndexError:
        pass

    try:
        if color_start == table[end_x - 1][end_y] and color_start == table[end_x - 2][end_y] and color_start == table[end_x][end_y - 1] and color_start == table[end_x][end_y + 1]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x - 1][end_y] = table[end_x - 2][end_y] = table[end_x][end_y - 1] = table[end_x][end_y + 1] = Piece.EMPTY
            return 30
    except IndexError:
        pass

    try:
        if color_start == table[end_x + 1][end_y] and color_start == table[end_x + 2][end_y] and color_start == table[end_x][end_y - 1] and color_start == table[end_x][end_y + 1]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x + 1][end_y] = table[end_x + 2][end_y] = table[end_x][end_y - 1] = table[end_x][end_y + 1] = Piece.EMPTY
            return 30
    except IndexError:
        pass

    # L
    try:
        if color_start == table[end_x][end_y - 2] and color_start == table[end_x][end_y - 1] and color_start == table[end_x + 1][end_y] and color_start == table[end_x + 2][end_y]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x][end_y - 1] = table[end_x][end_y - 2] = table[end_x + 1][end_y] = table[end_x + 2][end_y] = Piece.EMPTY
            return 20
    except IndexError:
        pass

    try:
        if color_start == table[end_x][end_y + 2] and color_start == table[end_x][end_y + 1] and color_start == table[end_x + 1][end_y] and color_start == table[end_x + 2][end_y]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x][end_y + 1] = table[end_x][end_y + 2] = table[end_x + 1][end_y] = table[end_x + 2][end_y] = Piece.EMPTY
            return 20
    except IndexError:
        pass

    try:
        if color_start == table[end_x][end_y + 2] and color_start == table[end_x][end_y + 1] and color_start == table[end_x - 1][end_y] and color_start == table[end_x - 2][end_y]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x][end_y + 1] = table[end_x][end_y + 2] = table[end_x - 1][end_y] = table[end_x - 2][end_y] = Piece.EMPTY
            return 20
    except IndexError:
        pass

    try:
        if color_start == table[end_x][end_y - 2] and color_start == table[end_x][end_y - 1] and color_start == table[end_x - 1][end_y] and color_start == table[end_x - 2][end_y]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x][end_y - 1] = table[end_x][end_y - 2] = table[end_x - 1][end_y] = table[end_x - 2][end_y] = Piece.EMPTY
            return 20
    except IndexError:
        pass


    # 4 in a row
    try:
        if color_start == table[end_x][end_y + 1] and color_start == table[end_x][end_y + 2] and color_start == table[end_x][end_y - 1]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x][end_y + 1] = table[end_x][end_y + 2] = table[end_x][end_y - 1] = Piece.EMPTY
            return 10
    except IndexError:
        pass

    try:
        if color_start == table[end_x][end_y + 1] and color_start == table[end_x][end_y - 2] and color_start == table[end_x][end_y - 1]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x][end_y + 1] = table[end_x][end_y - 2] = table[end_x][end_y - 1] = Piece.EMPTY
            return 10
    except IndexError:
        pass

    try:
        if color_start == table[end_x + 1][end_y] and color_start == table[end_x + 2][end_y] and color_start == table[end_x - 1][end_y]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x + 1][end_y] = table[end_x + 2][end_y] = table[end_x - 1][end_y] = Piece.EMPTY
            return 10
    except IndexError:
        pass

    try:
        if color_start == table[end_x + 1][end_y] and color_start == table[end_x - 2][end_y] and color_start == table[end_x - 1][end_y]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x + 1][end_y] = table[end_x - 2][end_y] = table[end_x - 1][end_y] = Piece.EMPTY
            return 10
    except IndexError:
        pass
    
    #3 in a row
    # middle moved
    try:
        if color_start == table[end_x][end_y + 1] and color_start == table[end_x][end_y - 1]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x][end_y - 1] = table[end_x][end_y + 1] = Piece.EMPTY
            return 5
    except IndexError:
        pass
    
    try:
        if color_start == table[end_x - 1][end_y] and color_start == table[end_x + 1][end_y]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x - 1][end_y] = table[end_x + 1][end_y] = Piece.EMPTY
            return 5
    except IndexError:
        pass

    # check to left
    try:
        if color_start == table[end_x - 1][end_y] and color_start == table[end_x - 2][end_y]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x - 1][end_y] = table[end_x - 2][end_y] = Piece.EMPTY
            return 5
    except IndexError:
        pass

    # check to right
    try:
        if color_start == table[end_x + 1][end_y] and color_start == table[end_x + 2][end_y]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x + 1][end_y] = table[end_x + 2][end_y] = Piece.EMPTY
            return 5
    except IndexError:
        pass
    
    # check up
    try:
        if color_start == table[end_x][end_y - 1] and color_start == table[end_x][end_y - 2]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x][end_y - 1] = table[end_x][end_y - 2] = Piece.EMPTY
            return 5
    except IndexError:
        pass

    # check down
    try:
        if color_start == table[end_x][end_y + 1] and color_start == table[end_x][end_y + 2]:
            table[start_x][start_y] = table[end_x][end_y]
            table[end_x][end_y] = table[end_x][end_y + 1] = table[end_x][end_y + 2] = Piece.EMPTY
            return 5
    except IndexError:
        pass

    return -1
        

def fall_motion(table, i, j):
    if not table[i][j] == Piece.EMPTY:
        return None
    
    if i == 0 and table[i][j] == Piece.EMPTY:
        next_val = random.randrange(1, 5)
        if next_val == table[i + 1][j].value: 
            next_val -= 1
        if j > 0:
            if table[i][j - 1] == next_val:
                next_val -= 1
        if j < len(table[0]) - 1:
            if table[i][j + 1] == next_val:
                next_val -= 1
        if next_val == Piece.RED.value:
            table[i][j] = Piece.RED
        elif next_val == Piece.YELLOW.value:
            table[i][j] = Piece.YELLOW
        elif next_val == Piece.GREEN.value:
            table[i][j] = Piece.GREEN
        elif next_val == Piece.BLUE.value:
            table[i][j] = Piece.BLUE
        return None
    elif i == 0:
        return None
    elif table[i][j] == Piece.EMPTY:
        if table[i - 1][j] == Piece.EMPTY:
            fall_motion(table, i - 1, j)
        table[i][j] = table[i - 1][j]
        table[i - 1][j] = Piece.EMPTY
        fall_motion(table, i - 1, j)
        return None



def try_moves(table):
    found = False
    global TOTAL_SCORE
    for i in range(len(table)):
        for j in range(len(table[0])):
            if x := make_move(table, i, j, i + 1, j) != -1:
                TOTAL_SCORE += x
                found = True
                refill_table(table)
                print_table(table)
                break
            if x := make_move(table, i, j, i - 1, j) != -1:
                TOTAL_SCORE += x
                found = True
                refill_table(table)
                print_table(table)
                break
            if x := make_move(table, i, j, i, j + 1) != -1:
                TOTAL_SCORE += x
                found = True
                refill_table(table)
                print_table(table)
                break
            if x := make_move(table, i, j, i, j - 1) != -1:
                TOTAL_SCORE += x
                found = True
                refill_table(table)
                print_table(table)
                break
    if not found:
        return -1
    return 0



def refill_table(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == Piece.EMPTY:
                fall_motion(table, i, j)


def main():
    global TOTAL_SCORE
    for _ in range(1000):
        table = create_table(11, 11)
        refill_table(table)
        print_table(table)
        time.sleep(0.5)
        for _ in range(10000):
            try_moves(table)
            # print_table(table)
            # time.sleep(0.5)
    print(TOTAL_SCORE / 1000)
        

if __name__ == "__main__":
    main()