from tkinter import *

maze = [
        ['#','#','#','#','#','#','#','#','#','#'],
        ['#','P','#','.','.','.','.','#','#','#'],
        ['#','.','#','.','#','#','.','#','#','#'],
        ['#','.','#','.','#','#','.','#','#','#'],
        ['#','.','#','.','.','#','.','#','#','#'],
        ['#','.','#','#','.','#','.','.','.','#'],
        ['#','.','#','#','.','#','#','#','.','#'],
        ['#','.','#','#','.','#','#','#','.','#'],
        ['#','.','.','.','.','#','#','#','.','#'],
        ['#','#','#','#','#','#','#','#',' ','#']
    ]

def drawmaze(maze):
    for row in maze:
        print(' '.join(row))

player = [1,1]

def movement(player, maze, direction):
    moves = {
        'w':(-1,0),
        'a':(0,-1),
        's':(1,0),
        'd':(0,1)
    }

    if direction not in moves:
        return player, False

    dx, dy = moves[direction]
    x, y = player
    nx, ny = x + dx, y + dy

    if maze[nx][ny] == '#':
        print("You bumped into a wall...")
        return player, False

    if maze[nx][ny] == ' ':
        return [nx, ny], True

    maze[x][y] = '.'
    maze[nx][ny] = 'P'
    return [nx, ny], False

'''
SOLUTIONS TO POSITION PROBLEM
1. Track the grid manually and set the pathways in code
2. (mostlikely) Track the Player and use if statements to change where they passed into dots
3. Redraw the maze after changes
'''

def postion(player, playerposition, moves):
    playerposition = player 
    pass




def gamewidget():  
    window = Tk()
    window.title("MAZE")
    window.geometry("600x400")
    
    label = Label(
        text = 'Matt' ,
        postion = '' ,
        font= 'calibri, '
    )

    label.pack()
    window.mainloop()