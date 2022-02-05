from time import sleep
import sys, os
from random import randint

clear = lambda: os.system("clear")

n = len(sys.argv)

alive = '\u2588'
dead = ' '

def check_args(n, args):
    if n != len(args) or n > 3:
        sys.exit(1)

def displayGrid(grid, gen):
    print(f'generation {gen} : ')
    for x in enumerate(grid):
        for y in enumerate(x[1]):
            print(y[1], end=" ")
        print()

def genGrid(rows, columns):
    grid = [ [ dead for x in range(columns) ] for y in range(rows) ]
    return grid

def testCenter(posx, posy, rows, columns):
    return posx == int(rows / 2) and posy == int(columns / 2)

def initLife(grid, rows, columns):
    for x in enumerate(grid):
        for y in enumerate(x[1]):
            if randint(0,1) == 1:
                grid[randint(0,rows-1)][randint(0,columns-1)] = alive
            #if testCenter(posx, posy, rows, columns) or testCenter(posx, posy, rows-1, columns-1) or testCenter(posx, posy, rows+1, columns+1) :
                #print("generating life")
                #grid[posx][posy] = "*"

def updateCell(grid, row, column, neighbours, actual):
    if actual == alive :
        if neighbours < 2 or neighbours > 3 :
            grid[row][column] = dead
    else:
        if neighbours == 3:
            grid[row][column] = alive

def is_within_boundaries(row, column, rows, columns):
    return row >= 0 and row < rows and column >= 0 and column < columns

def check_neighbours(grid, row, column, rows, columns):
    neighbours = 0
    to_test = [(row - 1, column -1), (row - 1, column), (row - 1, column + 1),
                ( row, column -1 ), (row, column +1),
                (row + 1, column - 1), (row + 1, column), (row + 1, column +1) ]
    for x in to_test:
        if is_within_boundaries(x[0], x[1], rows, columns):
            if grid[x[0]][x[1]] == alive:
                neighbours += 1
    updateCell(grid, row, column, neighbours, grid[row][column])

def check_for_life(grid, rows, columns):
    for x in enumerate(grid):
        for y in enumerate(x[1]):
            check_neighbours(grid, x[0], y[0], rows, columns)

def do_life(grid, rows, columns, gen):
    while(True):
        clear()
        displayGrid(grid, gen)
        check_for_life(grid, rows, columns)
        gen += 1
        sleep(0.05)
        #n = input("next gen...")

def run(args):
    clear()
    rows = int(args[1])
    columns = int(args[2])
    grid = genGrid(rows, columns)
    initLife(grid, rows, columns)
    do_life(grid, rows, columns, 0)

if __name__ == "__main__" :
    check_args(n, sys.argv)
    run(sys.argv)