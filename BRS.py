import turtle as t
import queue as q
import time
def readMazeFile(filePath):
    li = [];
    f=open(filePath, "r")
    li = f.read().splitlines()
    f.close()
    for i,j in enumerate(li):
        li[i] = [ch for ch in j]
    maxLength = len(max(li))
    for i in range(len(li)):
        while len(li[i]) < maxLength:
            li[i].append(0);
    return li

def turtleMaze(li, scale = 8):
    D =1;
    t.speed(10);
    t.penup()
    t.pendown()
    for i in range(2):
        t.forward(len(li[1])*scale);
        t.right(90);
        t.forward(len(li)*scale);
        t.right(90);
    t.penup()
    for i in li:
        if D == 1:
            for j in i:
                if j == "0":
                    t.forward(scale);
                elif j == "#":
                    t.color("black", "black")
                    t.begin_fill();
                    t.pendown() 
                    for i in range(4):
                        t.forward(scale);
                        t.right(90);
                    t.penup()
                    t.end_fill();
                    t.forward(scale);
                elif j == "S":
                    t.color("green", "green")
                    t.begin_fill();
                    t.pendown() 
                    for i in range(4):
                        t.forward(scale);
                        t.right(90);
                    t.penup()
                    t.end_fill();
                    t.forward(scale);
                elif j == "X":
                    t.color("red", "red")
                    t.begin_fill();
                    t.pendown() 
                    for i in range(4):
                        t.forward(scale);
                        t.right(90);
                    t.penup()
                    t.end_fill();
                    t.forward(scale);
            t.right(90);
            t.forward(scale);
            t.right(90);
            D = 2
            continue;
        if D == 2:
            for j in reversed(i):
                if j == "0":
                    t.forward(scale);
                elif j == "#":
                    t.color("black", "black")
                    t.begin_fill();
                    t.pendown() 
                    for i in range(4):
                        t.forward(scale);
                        t.left(90);
                    t.penup()
                    t.end_fill();
                    t.forward(scale);
                elif j == "S":
                    t.color("green", "green")
                    t.begin_fill();
                    t.pendown() 
                    for i in range(4):
                        t.forward(scale);
                        t.left(90);
                    t.penup()
                    t.end_fill();
                    t.forward(scale);
                elif j == "X":
                    t.color("red", "red")
                    t.begin_fill();
                    t.pendown() 
                    for i in range(4):
                        t.forward(scale);
                        t.left(90);
                    t.penup()
                    t.end_fill();
                    t.forward(scale);
            t.left(90);
            t.forward(scale);
            t.left(90);
            D = 1;
def turtleGoToStart(maze, start, scale=8):
    t.penup()
    t.goto((start[1]+1)*scale -(scale/2), (-start[0]-1)*scale +(scale/2))
    t.setheading(0);
    t.left(90);
def turtleLeft(scale):
    t.left(90)
    t.forward(scale)
    t.right(90)
def turtleRight(scale):
    t.right(90)
    t.forward(scale)
    t.left(90)
def turtleUp(scale):
    t.forward(scale)
def turtleDown(scale):
    t.right(180)
    t.forward(scale)
    t.left(180)
def turtlePath(moves, scale=8):
    t.color("green")
    t.pendown();
    for i in moves:
        if i == "L":
            turtleLeft(scale);
        elif i=="R":
            turtleRight(scale);
        elif i=="U":
            turtleUp(scale);
        else:
            turtleDown(scale);
    t.penup();
def getInputInt(querry, error):
    while True:
        try:
            i=int(input(querry))
            break;
        except:
            print(error);
    return i;
def getStartEnd(li):
    start=[]
    end=[]
    for i,ei in enumerate(li):
        for j,ej in enumerate(ei):
            if ej == "S":
                start.append(i)
                start.append(j)
            if ej == "X":
                end.append(j)
                end.append(i)
    if(len(start)<2):
        while True:
            start.append(getInputInt("Start not defined, enter X coord: ", "Invalid input, please try again"));
            start.append(getInputInt("Start not defined, enter Y coord: ", "Invalid input, please try again"));
            if len(li) > start[0] and len(max(li)) > start[1]:
                break;
            print( "Input invalid, are is out of maze bounds")
            start.clear();
    if(len(end)<2):
        while True:
            end.append(getInputInt("End not defined, enter X coord: ", "Invalid inputi, please try again"));
            end.append(getInputInt("End not defined, enter Y coord: ", "Invalid input, please try again"));
            if len(li) > start[0] and len(max(li)) > start[1]:
                break;
            print( "Input invalid, are is out of maze bounds")
            end.clear();
    return start, end;
def checkValid(maze, start, end, moves):
    i,j = checkMoves(moves)    
    if start[0]+i > len(maze[0]) or start[1]+j > len(maze):
        return False
    if start[0]+i < 0 or start[1]+j < 0:
        return False
    if maze[start[0]+i][start[1]+j] == "#":
        return False
    return True;
def checkEnd(maze, start, end, moves):
    i, j = checkMoves(moves)
    if( maze[start[0] + i][start[1] + j] == "X" ):    
        return True
    return False
def checkMoves( moves ):
    i=0
    j=0
    for move in moves:
        if move =="L":
            j -= 1
        elif move=="R":
            j += 1
        elif move=="U":
            i -= 1
        elif move=="D":
            i += 1
    return i, j;
def findPath( maze, start, end): 
    moves = q.Queue()
    moves.put("")
    add = ""
    while not checkEnd( maze, start, end, add):
        add = moves.get()
        for j in ["L", "R", "U", "D"]:
            move = add + j
            if checkValid(maze, start, end, move):
                moves.put(move)
    return (add);
def main():
    maze = readMazeFile("list");
    mazeStart, mazeEnd = getStartEnd(maze);
    print("Maze Start: \nX:{0:} Y:{1:}\nMaze End: \nX:{2:} Y:{3:}".format(mazeStart[0], mazeStart[1], mazeEnd[0], mazeEnd[1]));
    turtleMaze(maze, 20);
    turtleGoToStart(maze, mazeStart, 20);
    path = findPath( maze, mazeStart, mazeEnd)
    turtlePath(path, 20);
    print("Maze solved in: ", len(path), " moves");
    time.sleep(10);
main();
