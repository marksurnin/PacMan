# Final Intro to CS project created by NYU Abu Dhabi '18 students Peter Hadvab (@jozozchrenovej)and Mark Surnin (@marksurnin).
# To be continued...

import random

class Board:
    def __init__(self, textfile):
        '''
        Board is represented as a textfile that is in the same directory as this file.
        This method creates a board, which is a list of lists, where every sublist represents
            a row and every element in a sublist represents an individual square, which is denoted
            either by 'X' (wall), 'o' (unvisited square), '_' (visited square), '@' (PacMan) or 'M' (monster).
            Note: Monster can also be represented by a lowecase 'm', which signifies that the monster is on a visited square.
        PacMan and monster objects are created within this method; score and lives counters are also initialized.
        '''
        self.textfile = textfile
        fp = open(textfile, 'r+')
        self.board = []
        self.pacman = Pacman(0,0)
        self.score = 0
        self.lives = 3
        self.monster = Monster(0, 0)

        for line in fp:
            self.board.append(list(line.strip())) # Reading the file and creating a list of lists.

        
    def draw_board(self):
        '''
        This method goes through the list of lists (board) and draws elements
            in corresponding positions as the board is being updated. 
        '''
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 'X': # Drawing a wall.
                    fill(0,0,150)
                    noStroke()
                    rect(30*col, row*30, 30, 30)
                elif self.board[row][col] == 'o': # Drawing an unvisited square with a dot.
                    fill(0)
                    rect(30*col, row*30, 30, 30)
                    fill(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                    ellipse(30*col+15, 30*row+15, 10, 10)
                elif self.board[row][col] == '_': # Drawing a visited square without a dot.
                    fill(0, 0, 0)
                    rect(30*col, row*30, 30, 30)
                elif self.board[row][col] == '@': # Drawing the PacMan (a yellow square for now, animation is in progress).
                    fill(255,255,0)
                    rect(30*col, row*30, 30, 30)
                    self.pacman.update(col,row,self.pacman.cur_direction)
                elif self.board[row][col].upper() == 'M': # Drawing the monster (one monster for now, in progress).
                    fill(255,50,0)
                    rect(30*col, row*30, 30, 30)
                    self.monster.update(col,row)

        textSize(32)
        fill(0,102,153)
        text('Score: ' + str(self.score), 500, 430) # Printing the score.
        if self.lives > 0:
            text('Lives: ' + str(self.lives), 680, 430) #Printing remaining lives.
        # else:
        #     self.board[1][1] = '_'
        #     self.board[1][2] = '_'
        #     self.board[2][1] = '_'
        #     text('Game Over', 330, 450)
                
        
    def can_pacman_move(self, direction):
        '''
        This method checks if the Pacman can move in a specified direction.
        '''
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
        '''
        This method moves the PacMan in a specified direction, updating a number of values in the list of lists.
        '''
        if move_direction == 'left':
            if self.board[self.pacman.y][self.pacman.x - 1] == 'o': # Checking if there is an unvisited square (with a dot) on the left.
                self.board[self.pacman.y][self.pacman.x] = '_'      # Making the previous coordinates a visited square (without a dot).
                self.board[self.pacman.y][self.pacman.x - 1] = '@'  # Moving the PacMan to the left.
                self.pacman.x -= 1                                  # Decrementing the PacMan's X coordinate by 1.
                self.score += 1                                     # Incrementing the player's score by 1 when he lands on an unvisited square.
                
            elif self.board[self.pacman.y][self.pacman.x - 1] == '_': # Similar procedure if moving to a VISITED square. No incrementing of the score.
                self.board[self.pacman.y][self.pacman.x] = '_'                
                self.board[self.pacman.y][self.pacman.x - 1] = '@'
                self.pacman.x -= 1
                
            elif self.board[self.pacman.y][self.pacman.x - 1] == 'M' or self.board[self.pacman.y][self.pacman.x - 1] == 'm':
                self.pacman.x = 1                                   # If the sqaure on the left is a monster, reset PacMan's coordinates to (1,1).
                self.pacman.y = 1
                self.board[1][1] = '@'            
            
        if move_direction == 'right':                               # Analogous algorithm for PacMan moving right, down and up.
            if self.board[self.pacman.y][self.pacman.x + 1] == 'o':
                self.board[self.pacman.y][self.pacman.x] = '_'                
                self.board[self.pacman.y][self.pacman.x + 1] = '@'
                self.pacman.x += 1
                self.score += 1
                
            elif self.board[self.pacman.y][self.pacman.x + 1] == '_':
                self.board[self.pacman.y][self.pacman.x] = '_'                
                self.board[self.pacman.y][self.pacman.x + 1] = '@'
                self.pacman.x += 1
                
            elif self.board[self.pacman.y][self.pacman.x + 1] == 'M' or self.board[self.pacman.y][self.pacman.x + 1] == 'm':
                self.pacman.x = 1
                self.pacman.y = 1
                self.board[1][1] = '@'
    
        if move_direction == 'up':
            if self.board[self.pacman.y - 1][self.pacman.x] == 'o':
                self.board[self.pacman.y][self.pacman.x] = '_'                
                self.board[self.pacman.y - 1][self.pacman.x] = '@'
                self.pacman.y -= 1
                self.score += 1
                
            elif self.board[self.pacman.y - 1][self.pacman.x] == '_':
                self.board[self.pacman.y][self.pacman.x] = '_'                
                self.board[self.pacman.y - 1][self.pacman.x] = '@'
                self.pacman.y -= 1
                
            elif self.board[self.pacman.y - 1][self.pacman.x] == 'M' or self.board[self.pacman.y - 1][self.pacman.x] == 'm':
                self.pacman.x = 1
                self.pacman.y = 1
                self.board[1][1] = '@'

        if move_direction == 'down':
            if self.board[self.pacman.y + 1][self.pacman.x] == 'o':
                self.board[self.pacman.y][self.pacman.x] = '_'                
                self.board[self.pacman.y + 1][self.pacman.x] = '@'
                self.pacman.y += 1
                self.score += 1
                
            elif self.board[self.pacman.y + 1][self.pacman.x] == '_':
                self.board[self.pacman.y][self.pacman.x] = '_'                
                self.board[self.pacman.y + 1][self.pacman.x] = '@'
                self.pacman.y += 1
                
            elif self.board[self.pacman.y + 1][self.pacman.x] == 'M' or self.board[self.pacman.y + 1][self.pacman.x] == 'm':
                self.pacman.x = 1
                self.pacman.y = 1
                self.board[1][1] = '@'
    
         
    def find_possible_directions_monster(self):
        '''
        By counting the number of possible directions after every iteration, the program records whether the monster is at a junction.
        If there is not a wall to the left, for example, left is added to the list of possible directions.
        The number of choices is returned.
        '''
        self.monster.pos_directions = []
        choices = 0
        if self.board[self.monster.y][self.monster.x - 1] != 'X':
            choices += 1
            self.monster.pos_directions.append("left")
        if self.board[self.monster.y][self.monster.x + 1] != 'X':
            choices += 1
            self.monster.pos_directions.append("right")
        if self.board[self.monster.y - 1][self.monster.x] != 'X':
            choices += 1
            self.monster.pos_directions.append("up")
        if self.board[self.monster.y + 1][self.monster.x] != 'X':
            choices += 1
            self.monster.pos_directions.append("down")
        return choices
        
    def change_direction_monster(self):
        '''
        If there is only one possible direction, it means there is a dead end, need to reverse direction.

            Note: a list of directions = ['left', 'up', 'right', 'down'] is initialized in the setup() function.
            The program takes the current direction of the PacMan (ex. 'right'), finds the index of 'right' in the directions list.
            In our case it is 2. Note that the opposite directions are 1 apart from each other in the list.
            We add 2 to the index, get 4. The modulo operator makes sure we move to the next element in the list, creating a loop.
            In this case it directs us to 4 % 4 = 0 ('left').

        If there are two directions:
            The PacMan is either moving in a straight line (keep going).
            The Pacman is at a 90-degree angle junction (randomly choose a direction from the list of possible directions.)

        If there are more than two directions:
            Randomly choose a direction from the list of possible directions.
        '''
        if self.find_possible_directions_monster() == 1:
            self.monster.cur_direction = directions[(directions.index(self.monster.cur_direction)+2)%4]
        elif self.find_possible_directions_monster() == 2:
            if self.monster.pos_directions[1] != directions[(directions.index(self.monster.pos_directions[0])+2)%4]: # If the monster is NOT moving in a straight line
                self.monster.cur_direction = random.choice(self.monster.pos_directions)
        elif self.find_possible_directions_monster() > 2:
            self.monster.cur_direction = random.choice(self.monster.pos_directions)

    def move_monster(self):
        '''
        A monster move function similar to the PacMan move function, with a minor tweak with upper or lowercase 'm'/'M',
        which signifies whether the moster is moving from a visited square or not.
        '''
        
        if self.monster.cur_direction == 'left':
   
            if self.board[self.monster.y][self.monster.x] == 'm':
                self.board[self.monster.y][self.monster.x] = '_' 
                
            elif self.board[self.monster.y][self.monster.x] == 'M':     
                self.board[self.monster.y][self.monster.x] = 'o'  
            
            if self.board[self.monster.y][self.monster.x-1] == '_':               
                self.board[self.monster.y][self.monster.x - 1] = 'm'
            
            elif self.board[self.monster.y][self.monster.x-1] == 'o':
                self.board[self.monster.y][self.monster.x-1] = 'M'
                
            elif self.board[self.monster.y][self.monster.x-1] == '@':   # The following lines are executed if the Pacman is moving to a square with the PacMan!
                self.board[self.monster.y][self.monster.x-1] = 'm'      # Make the square to the left a lowercase 'm' (monster standing on a visited square).
                self.pacman.x = 1                                       # Make PacMan's coordinates (1,1) - resetting position.
                self.pacman.y = 1
                self.board[1][1] = '@'                                  # Place the '@' symbol in board[1][1].
                self.lives -= 1                                         # Decrement the number of lives by 1.
                    
            self.monster.x -= 1                                         # Decrement the monster's x coordinate by 1 (if moving to the left).
            
        if self.monster.cur_direction == 'right':                       # Analogous algorithm for the monster moving right, down and up.
            
            if self.board[self.monster.y][self.monster.x] == 'm':
                self.board[self.monster.y][self.monster.x] = '_' 
                
            elif self.board[self.monster.y][self.monster.x] == 'M':     
                self.board[self.monster.y][self.monster.x] = 'o'  
            
            if self.board[self.monster.y][self.monster.x+1] == '_':               
                self.board[self.monster.y][self.monster.x+1] = 'm'
            
            elif self.board[self.monster.y][self.monster.x+1] == 'o':
                self.board[self.monster.y][self.monster.x+1] = 'M'
                
            elif self.board[self.monster.y][self.monster.x+1] == '@':
                self.board[self.monster.y][self.monster.x+1] = 'm'
                self.pacman.x = 1
                self.pacman.y = 1
                self.board[1][1] = '@'
                self.lives -= 1                

            self.monster.x += 1
            
    
        if self.monster.cur_direction == 'up':
    
            
            if self.board[self.monster.y][self.monster.x] == 'm':
                self.board[self.monster.y][self.monster.x] = '_' 
                
            elif self.board[self.monster.y][self.monster.x] == 'M':     
                self.board[self.monster.y][self.monster.x] = 'o'  
            
            if self.board[self.monster.y-1][self.monster.x] == '_':               
                self.board[self.monster.y-1][self.monster.x] = 'm'
            
            elif self.board[self.monster.y-1][self.monster.x] == 'o':
                self.board[self.monster.y-1][self.monster.x] = 'M'
                
            elif self.board[self.monster.y-1][self.monster.x] == '@':
                self.board[self.monster.y-1][self.monster.x] = 'm' 
                self.pacman.x = 1
                self.pacman.y = 1
                self.board[1][1] = '@'  
                self.lives -= 1              

            self.monster.y -= 1
            

        if self.monster.cur_direction == 'down':
            if self.board[self.monster.y][self.monster.x] == 'm':
                self.board[self.monster.y][self.monster.x] = '_' 
                    
            elif self.board[self.monster.y][self.monster.x] == 'M':     
                self.board[self.monster.y][self.monster.x] = 'o'  
                
            if self.board[self.monster.y+1][self.monster.x] == '_':               
                self.board[self.monster.y+1][self.monster.x] = 'm'
                
            elif self.board[self.monster.y+1][self.monster.x] == 'o':
                self.board[self.monster.y+1][self.monster.x] = 'M'
            
            elif self.board[self.monster.y+1][self.monster.x] == '@':
                self.board[self.monster.y+1][self.monster.x] = 'm' 
                self.pacman.x = 1
                self.pacman.y = 1
                self.board[1][1] = '@'  
                self.lives -= 1           

            self.monster.y += 1
       

class Pacman:
    '''
    Pacman class. Purpose: storing current and next directions. Next direction is determined by which arrow key is pressed.
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cur_direction = None
        self.next_direction = None

    def update(self, row, col, dir): # Updating the current direction to the value of the passed variable.
        self.x = row
        self.y = col
        self.cur_direction = dir
            
class Monster:
    '''
    Monster class. Purpose: storing current direction and the list of possible directions at every iteration.
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos_directions = []
        self.cur_direction = 'up'
    
    def update(self, row, col):
        self.x = row
        self.y = col
        
        
def setup():
    size(1260, 510)
    background(200, 200, 210)
    frameRate(6)
    global board
    global directions
    directions = ['left', 'up', 'right', 'down'] # The direction list referred to in change_direction_monster() function documentation.
    board = Board('board.txt')                   # The board file, has to be in the same directory.
    
def keyPressed():
    '''
    Updates next_direction according to which arrow key is pressed.
    '''
    if keyCode == LEFT:
        board.pacman.next_direction = 'left'
    elif keyCode == RIGHT:
        board.pacman.next_direction = 'right'
    elif keyCode == UP:
        board.pacman.next_direction = 'up'
    elif keyCode == DOWN:
        board.pacman.next_direction = 'down'
    elif keyCode == SHIFT:                      # New game - reset all values and positions.
        for row in range(len(board.board)):
            for col in range(len(board.board[0])):
                if board.board[row][col] == '_' or board.board[row][col] == '@' or board.board[row][col] == 'M' or board.board[row][col] == 'm':
                    board.board[row][col] = 'o' # Make all squares unvisited.
        board.board[1][1] = '@'                 # Place the PacMan at board[1][1].
        board.board[11][21] = 'M'               # Place the monster at board[11][21]. Row is the first sublist, so the coordinates are in the form (y,x).
        board.pacman.x = 1
        board.pacman.y = 1
        board.monster.x = 21
        board.monster.y = 11
        board.monster.cur_direction = 'up'      # Reset monster's current direction to 'up'. Make sure there is actually space for it to move up.
        board.score = 0                         # Reset the score and lives.
        board.lives = 3
                
        
def draw():
    if board.lives == 0:                        # Game over image if there are no lives left.
        img = loadImage('game_over.jpg')
        image(img, 0, 0, 1260, 510)
        
    elif board.score == 219:                    # Winner image if all dots have been eaten.
        img = loadImage('winner.png')
        image(img, 0, 0, 1260, 510)
        
    else:                                                                   # Main move function. 
        if board.pacman.next_direction:                                     # If there is a next direction (some arrow key was pressed):
            if board.can_pacman_move(board.pacman.next_direction):          #     Check if the PacMan can move in that direction.
                board.pacman.cur_direction = board.pacman.next_direction    #         If yes, make that the current direction.
                board.pacman.next_direction = None                          #         Set next direction to None.
                board.move_pacman(board.pacman.cur_direction)               #         Move the PacMan in that direction.
            else:                                                           #     If the PacMan can't move in the next direction yet:
                if board.can_pacman_move(board.pacman.cur_direction):       #         If the PacMan can move in the direction it was going in:
                    board.move_pacman(board.pacman.cur_direction)           #             Move the PacMan in that direction. (Basically, keep moving the PacMan where it was going until it can go in the next direction).
        else:                                                               # If there is no specified next direction (no arrow keys were pressed):
            if board.can_pacman_move(board.pacman.cur_direction):           #         (Repeat the logic) If the PacMan can move in the direction it was going in:
                board.move_pacman(board.pacman.cur_direction)               #         Move the PacMan in that direction.
    
        board.change_direction_monster()                                    # Changes the direction of the monster if it is at a junction or a dead end. Keeps it going if it is going in a straight line, passing no junction.
        board.move_monster()                                                # Moves the monster in that very direction.
        board.draw_board()                                                  # Draw the board.
