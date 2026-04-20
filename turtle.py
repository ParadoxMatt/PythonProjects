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
        'a':(0,1),
        's':(0,-1),
        'd':(1,0)
    }

    if direction not in moves:
        return player, False

    dx, dy = moves[direction]
    x, y = player
    nx, ny = x + dx, y + dy

    if maze[nx][ny] == '#':
        return player, False

    if maze[nx][ny] == ' ':
        return [nx, ny], True

    maze[x][y] = '.'
    maze[nx][ny] = 'P'
    return [nx, ny], False

while True:
    drawmaze(maze)
    move = input("Move (WASD): ").lower()

    player, won = movement(player, maze, move)

    if won:
        drawmaze(maze)
        print("You escaped the maze!")
        break