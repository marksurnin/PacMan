import random
import time

#adding comment
class Board:
    def __init__(self, textfile):
        self.textfile = textfile
        fp = open(textfile, 'r+')
        self.board = []
        self.pacmanx = 0
        self.pacmany = 0
        self.pacman = Pacman(0,0)

        for line in fp:
            self.board.append(list(line.strip()))

        
    def draw_board(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 'X':
                    fill(0,0,150)
                    rect(30*col, row*30, 30, 30)
                elif self.board[row][col] == 'o':
                    fill(200,200,200)
                    rect(30*col, row*30, 30, 30)
                elif self.board[row][col] == '_':
                    fill(0,0,0)
                    rect(30*col, row*30, 30, 30)
                elif self.board[row][col] == '@':
                    fill(255,255,0)
                    rect(30*col, row*30, 30, 30)
                    self.pacman.update(col,row,self.pacman.cur_direction)
        #print(self.pacman.x, self.pacman.y)
        '''
                elif self.board[row][col] == 'M':
                    self.monster = Monster(col,row)
                    fill(255,0,0)
                    rect(30*col, row*30, 30, 30)'''
                
        
    def can_pacman_move(self, direction):
        self.direction = direction
        if direction == 'left':
            if self.board[self.pacman.y][self.pacman.x - 1] != 'X':
                return True
                
        if direction == 'right':
            if self.board[self.pacman.y][self.pacman.x + 1] != 'X':
                return True
    
        if direction == 'up':
            if self.board[self.pacman.y - 1][self.pacman.x] != 'X':
                return True

        if direction == 'down':
            if self.board[self.pacman.y + 1][self.pacman.x] != 'X':
                return True

    def move_pacman(self, move_direction):
        self.move_direction = move_direction
        if move_direction == 'left':
            self.board[self.pacman.y][self.pacman.x] = '_'                
            self.board[self.pacman.y][self.pacman.x - 1] = '@'
            self.pacman.x -= 1
            
        if move_direction == 'right':
            self.board[self.pacman.y][self.pacman.x] = '_'                
            self.board[self.pacman.y][self.pacman.x + 1] = '@'
            self.pacman.x += 1
    
        if move_direction == 'up':
            self.board[self.pacman.y][self.pacman.x] = '_'                
            self.board[self.pacman.y - 1][self.pacman.x] = '@'
            self.pacman.y -= 1

        if move_direction == 'down':
            self.board[self.pacman.y][self.pacman.x] = '_'                
            self.board[self.pacman.y + 1][self.pacman.x] = '@'
            self.pacman.y += 1
             

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cur_direction = None
        self.next_direction = None

    def update(self, row, col, dir):
        self.x = row
        self.y = col
        self.cur_direction = dir
'''                
class Monster:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def is_monster_at_junction(self):
        choices = 0
        if self.board[self.monster.y][self.monster.x - 1] != 'X':
            choices += 1
        if self.board[self.monster.y][self.monster.x + 1] != 'X':
            choices += 1
        if self.board[self.monster.y - 1][self.monster.x] != 'X':
            choices += 1
        if self.board[self.monster.y + 1][self.monster.x] != 'X':
            choices += 1
            
        return choices
        
     def move_monster(self):
        direction = random.choice(['left', 'right', 'up', 'down'])
        if direction == 'left':
            if self.board[self.monster.y][self.pacman.x - 1] != 'X':
                self.board[self.pacman.y][self.pacman.x] = '_'                
                self.board[self.pacman.y][self.pacman.x - 1] = '@'
                self.pacman.x -= 1 
'''                        

def setup():
    size(750, 450)
    background(200, 200, 210)
    frameRate(5)
    global board
    board = Board('board.txt')
    


def keyTyped():
    if key == 'a':
        board.pacman.next_direction = 'left'
    elif key == 'd':
        board.pacman.next_direction = 'right'
    elif key == 'w':
        board.pacman.next_direction = 'up'
    elif key == 's':
        board.pacman.next_direction = 'down'
        
def draw():
    board.draw_board()
    if board.pacman.next_direction:
        #print(board.pacman.cur_direction, board.pacman.next_direction)
        if board.can_pacman_move(board.pacman.next_direction):
            board.pacman.cur_direction = board.pacman.next_direction
            board.pacman.next_direction = None
            board.move_pacman(board.pacman.cur_direction)
        else:
            if board.can_pacman_move(board.pacman.cur_direction):
                board.move_pacman(board.pacman.cur_direction)
    else:
        if board.can_pacman_move(board.pacman.cur_direction):
            board.move_pacman(board.pacman.cur_direction)
        
