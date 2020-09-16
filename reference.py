
# from processing import *
# import webaudio
# from random import randint



# moveGhostCounter = 1

# """ this 2-dimensional array stores whether each block in
#     the grid is walkable, a wall, or a chip.
#     0 = Walkable
#     1 = Wall
#     2 = Chip & Walkable
# """
# walls = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
#          [0, 0, 1, 0, 2, 1, 0, 0, 0, 1, 2, 0, 1, 0, 0],
#          [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#          [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
#          [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0],
#          [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0],
#          [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
#          [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#          [0, 0, 1, 0, 2, 1, 0, 0, 0, 1, 2, 0, 1, 0, 0],
#          [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# # these are the sound effects we will use as we collect 
# # each item
# openDoorSound = webaudio.loadAudio("http://www.soundjay.com/door/sounds/door-lock-1.mp3")
# collectChipSound = webaudio.loadAudio("http://www.soundjay.com/misc/sounds/coin-drop-4.mp3")
# winSound = webaudio.loadAudio("http://www.soundjay.com/misc/sounds/magic-chime-06.mp3")
# looseSound = webaudio.loadAudio("http://www.soundjay.com/misc/sounds/fail-trombone-01.mp3")
# robbedSound = webaudio.loadAudio("http://www.soundjay.com/human/sounds/man-laughing-04.mp3")
# Robber = None
# """ This list stores each door in the level as a dictionary.
#     For each door, we need to know it's row, column, and what
#     color it will be since red keys open red doors, blue keys
#     open blue doors, etc.
# """
# doors = [{
#         'row': 3, 
#         'col': 5, 
#         'color': 'r',
#         'fill': (204, 0, 0),
#         'stroke': (128, 0, 0)
#       }, 
#       {
#         'row': 10, 
#         'col': 5, 
#         'color': 'b',
#         'fill': (0, 0, 204),
#         'stroke': (0, 0, 128)
#       }, 
#        {
#         'row': 3, 
#         'col': 9, 
#         'color': 'y',
#         'fill': (255, 204, 0),
#         'stroke': (204, 163, 0)
#       }, 
#          {
#         'row': 1, 
#         'col': 4, 
#         'color': 'y',
#         'fill': (255, 204, 0),
#         'stroke': (204, 163, 0)
#       }, 
#          {
#         'row': 8, 
#         'col': 12, 
#         'color': 'y',
#         'fill': (255, 204, 0),
#         'stroke': (204, 163, 0)
#       }, 
#       {
#         'row':10, 
#         'col': 9, 
#         'color': 'g',
#         'fill': (0, 204, 0),
#         'stroke': (0, 128, 0)
#       }]
     

# """ This list stores each key in the level as a dictionary.
#     For each key, we need to know it's row, column, and what
#     color it will be since red keys open red doors, blue keys
#     open blue doors, etc.
# """
# keys = [{
#         'row': 5, 
#         'col': 3, 
#         'color': 'r',
#         'fill': (204, 0, 0),
#         'stroke': (128, 0, 0)
#       }, 
#        {'row': 2, 
#        'col': 3, 
#        'color': 'b',
#         'fill': (0, 0, 204),
#         'stroke': (0, 0, 128)
#       },
#        {'row': 11, 
#        'col': 3, 
#        'color': 'y',
#         'fill': (255, 204, 0),
#        'stroke': (204, 163, 0)
#       },
#         {'row': 8, 
#          'col': 0, 
#          'color': 'y',
#          'fill': (255, 204, 0),
#          'stroke': (204, 163, 0)
#       },
#         {'row': 3, 
#          'col': 3, 
#          'color': 'y',
#          'fill': (255, 204, 0),
#          'stroke': (204, 163, 0)
#       },
#        {'row': 2, 
#        'col': 11, 
#        'color': 'g',
#         'fill': (0, 204, 0),
#        'stroke': (0, 128, 0)
#       }]

# # this is the dictionary storing all data related to the 
# # exit door
# exitLock = {'row': 6,
#             'col': 2,
#             'isOpen': False}

# # this is the dictionary storing all data related to the 
# # exit portal
# exitPortal = {'row': 6,
#               'col': 1,
#               'color': [85, 170, 255],
#               'colorInc': [1, 1, -1]}

# #this is the dictionary storing all data relate to the
# # robber
# robber = {"row": 3,
#           "col": 4
#           }

# # this is the total number of chips to be collected in this
# # level
# totalChips = 6

# side = 36
# width = 540
# height = 504
# numRows = (height/side)-1
# numCols = (width/side)-1

# """ This function draws the lines of the grid.
# """
# def drawLines():
#     stroke(128, 128, 128)
#     for x in range(0, 541, 36):
#         line(x, 0, x, 504)
#     for y in range(0, 510, 36):
#         line(0, y, 540, y)

# """ This function goes through each row and column of our
#     walls 2-dimensional array and draws each wall and chip.
# """
# def drawWallsArray():
#     for y in range(len(walls)):
#         for x in range(len(walls[y])):
#             if walls[y][x] == 1:
#                 stroke(64, 64, 64)
#                 fill(128, 128, 128)
#                 rect(side * x, side * y, side, side)
#             if walls[y][x] == 2: #it's a chip
#                 stroke(230, 230, 230)
#                 strokeWeight(2)
#                 fill(100,100,100)
#                 y1 = (y * side) + 10
#                 x1 = (x * side) + 3
#                 rect(x1, y1, 30, 16)
#                 strokeWeight(1)
                
# def YOUWIN():
#     text("You Win",200,200)
#     text("http://ebay.eu/2aWBgmq", 250,250)
                
# """ This function draws all the doors in the door list as
#     squares filled in with their corresponding colors.
# """
# def drawDoors():
#     for door in doors:
#         stroke(door['stroke'][0], door['stroke'][1], door['stroke'][2])
#         fill(door['fill'][0], door['fill'][1], door['fill'][2])
#         rect(door['col'] * side, door['row'] * side, side, side)
#         stroke(0, 0, 0)
#         fill(0, 0, 0)
#         ellipse((door['col'] * side) + 18, (door['row'] * side) + 18, 10, 10)

# """ This function draws all the keys in the key list as
#     circles.
# """
# def drawKeys():
#     for key in keys:
#         stroke(key['stroke'][0], key['stroke'][1], key['stroke'][2])
#         fill(key['fill'][0], key['fill'][1], key['fill'][2])
#         ellipse((key['col'] * 36) + 18, (key['row'] * 36) + 18, 15, 15)

# """ This function draws the exit lock and the exit portal.
#     If the exit lock has been opened, it will not be drawn.
# """
# def drawExit():
#     # draw lock
#     global exitPortal
#     stroke(51, 0, 51)
#     fill(102, 0, 102)
#     if not exitLock['isOpen']:
#         rect(36 * exitLock['col'], 36 * exitLock['row'], 36, 36)
#         stroke(0, 0, 0)
#         fill(0, 0, 0)
#         ellipse((exitLock['col'] * 36) + 18, (exitLock['row'] * 36) + 18, 10, 10)
#     exitPortal['color'][0] = exitPortal['color'][0] + exitPortal['colorInc'][0]
#     exitPortal['color'][1] = exitPortal['color'][1] + exitPortal['colorInc'][1]
#     exitPortal['color'][2] = exitPortal['color'][2] + exitPortal['colorInc'][2]
#     if exitPortal['color'][0] > 255 or exitPortal['color'][0] < 0:
#         exitPortal['colorInc'][0] *= -1
#     if exitPortal['color'][1] > 255 or exitPortal['color'][1] < 0:
#         exitPortal['colorInc'][1] *= -1
#     if exitPortal['color'][2] > 255 or exitPortal['color'][2] < 0:
#         exitPortal['colorInc'][2] *= -1
#     stroke(exitPortal['color'][0], exitPortal['color'][1], exitPortal['color'][2])
#     fill(exitPortal['color'][0], exitPortal['color'][1], exitPortal['color'][2])
#     rect(36 * exitPortal['col'] + 4, 36 * exitPortal['row'] + 4, 28, 28)

# """ This function draws all the text on the screen. This
#     includes the timer, the number of chips collected,
#     and the number of each key collected.
# """
# def drawData():
#     global timeString, secinverse
#     # draw time
#     fill(0, 0, 0)
#     mil = millis()
#     sec = mil / 1000
#     sec = sec %  60
#     secinverse =  45 - sec
#     timeString = "Time: %02d" % (45 - sec)
#     textSize(25)
#     text(timeString, 10, 30)
#     if secinverse == 0:
#         text("Game Over", 504/2 - 44, 540/2 - 36*2)
#         looseSound.play()
#         exitp()
#     # draw num chips collected
#     text("Chips: " + str(character.chips), 425, 30)
#     # draw num blue keys and num red keys
#     fill(0, 0, 0)
#     text("Keys: ", 10,485)
#     fill(255, 0, 0)
#     text(str(character.rk), 85, 485)
#     fill(0, 0, 255)
#     text(str(character.bk), 115, 485)
#     fill(0, 255, 0)
#     text(str(character.gk), 145, 485)
#     fill(255, 204, 0)
#     text(str(character.yk), 175, 485)

# class Ghost:
#     def __init__(self, row, column, color, direction):
#         self.row = row
#         self.column = column
#         self.color = color
#         self.fill = [0, 0, 0]
#         if self.color == "r":
#             self.fill = [128, 0, 0]
#         elif self.color == "y":
#             self.fill = [204, 153, 0]
#         elif self.color == "g":
#             self.fill = [0, 204, 153]
#         elif self.color == "b":
#             self.fill = [0, 51, 153]
#         self.direction = direction
        
#     def draw(self):
#         fill(self.fill[0], self.fill[1], self.fill[2])
#         x1 = (self.column * 36) + (36/2)
#         y1 = ((self.row + 1) * 36) - 3
#         x2 = (self.column * 36) + 3
#         y2 = (self.row * 36) + 3
#         x3 = ((self.column + 1) * 36) - 3
#         y3 = y2
#         triangle(x1, y1, x2, y2, x3,y3)
        
#     def move(self):
#         up = self.row - 1
#         down = self.row + 1
#         left = self.column - 1
#         right = self.column + 1
#         possibleDirs = []
#         if self.column == character.col and self.row < character.row and walls[down][self.column] != 1:
#             self.row += 1
#         elif self.column == character.col and self.row < character.row and walls[up][self.column] != 1:
#             self.row -= 1
#         elif self.row == character.row and self.column > character.col and walls[self.row][left] != 1:
#             self.column -= 1
#         elif self.row == character.row and self.column < character.col and walls[self.row][right] != 1:
#             self.column += 1
#         elif self.direction == 1:
#             if up >= 0 and walls[up][self.column] != 1:
#                 possibleDirs.append(1)
#             elif walls[down][self.column] != 1:
#                 possibleDirs.append(2)
#             if left >= 0 and walls[self.row][left] != 1:
#                 possibleDirs.append(3)
#             if right <= numCols and walls[self.row][right] != 1:
#                 possibleDirs.append(4)
#         elif self.direction == 2:
#             if down <= numRows and walls[down][self.column] != 1:
#                 possibleDirs.append(2)
#             elif walls[down][self.column] != 1:
#                 possibleDirs.append(1)
#             if left >= 0 and walls[self.row][left] != 1:
#                 possibleDirs.append(3)
#             if right <= numCols and walls[self.row][right] != 1:
#                 possibleDirs.append(4)
#         elif self.direction == 3:
#             if up >= 0 and walls[up][self.column] != 1:
#                 possibleDirs.append(1)
#             if down <= numRows and walls[down][self.column] != 1:
#                 possibleDirs.append(2)
#             if left >= 0 and walls[self.row][left] != 1:
#                 possibleDirs.append(3)
#             elif walls[self.row][right] != 1:
#                 possibleDirs.append(4)
#         elif self.direction == 4:
#             if up >= 0 and walls[up][self.column] != 1:
#                 possibleDirs.append(1)
#             if down <= numRows and walls[down][self.column] != 1:
#                 possibleDirs.append(2)
#             if right <= numCols and walls[self.row][right] != 1:
#                 possibleDirs.append(4)
#             elif walls[self.row][left] != 1:
#                 possibleDirs.append(3)
                
#         if len(possibleDirs) > 0:
#             go = randint(0, len(possibleDirs)-1)
#             if possibleDirs[go] == 1:
#                 self.row = up
#                 self.direction = 1
#             elif possibleDirs[go] == 2:
#                 self.row = down
#                 self.direction = 2
#             elif possibleDirs[go] == 3:
#                 self.column = left
#                 self.direction = 3
#             elif possibleDirs[go] == 4:
#                 self.column = right
#                 self.direction = 4
#         self.checkDoors()
#     def checkDoors(self):
#         up = self.row - 2
#         down = self.row + 2
#         left = self.column - 2
#         right = self.column + 2
#         """for door in doors:
#             if (self.row == door["row"] and
#                self.column == door["col"]):
#                 if self.direction == 1:
#                     self.row = down
#                     self.direction = 2
#                     break
#                 if self.direction == 2:
#                     self.row = up
#                     self.direction = 1
#                     break
#                 if self.direction == 3:
#                     self.column = right
#                     self.direction = 4
#                     break
#                 if self.direction == 4:
#                     self.column = left
#                     self.direction = 3
#                     break"""
#         if self.row == exitLock["row"] and self.column == exitLock["col"]:
#             self.row = down
#             self.direction = 2   
            
#     """def GhostClearPath(self):
#         GhostClearPath = True
#         for loop"""
    
    
# class Char:
#     global initRow, initCol
#     """ This is the constructor. When you create a 
#         character object, you initialize all of its values.
#         Note that the __init__ function and all functions
#         in this class, have at least one parameter, which is
#         'self'. This is so all the data is saved to the
#         object itself.
#         Instead of creating variables as row = initRow, 
#         we must do self.row = initRow, this way the variable
#         can be used by all functions inside the class.
#     """
#     def __init__(self, initRow, initCol):
#         self.row = initRow
#         self.col = initCol
#         self.x = [(36 * self.col) + 18, (36 * self.col) + 3, (36 * (self.col + 1)) - 3]
#         self.y = [(36 * self.row) + 3, (36 * (self.row + 1)) - 3, (36 * (self.row + 1)) - 3]
#         self.bk = 0 #num blue keys owned
#         self.rk = 0 # num red keys owned
#         self.gk = 0 # num green keys owned
#         self.yk = 0 # num yellow keys owned
#         self.chips = 0 #num chips collected
#         self.direction = 0
        
#     """ This function draws the player character. """
#     def draw(self):
#         stroke(0, 51, 0)
#         fill(0, 102, 0)
#         triangle(self.x[0], self.y[0], self.x[1], self.y[1], self.x[2], self.y[2])
#         self.complete()
        
#     """ This function moves the player character based 
#         on the direction the player wishes to move. 
#         1 = UP
#         2 = DOWN
#         3 = LEFT
#         4 = RIGHT
#         After we move the player, we check where they are
#         standing. We have to check if they are standing
#         on a door, a key, a chip, and if they have collected 
#         all the chips.
#     """
#     def move(self, direction):
#         global walls
#         if direction == 1: #going up
#             if self.row > 0 and walls[self.row - 1][self.col] != 1:
#                 self.direction = 1
#                 self.row -= 1
#                 self.y = [(36 * self.row) + 3, (36 * (self.row + 1)) - 3, (36 * (self.row + 1)) - 3]
#         elif direction == 2: #going down
#             if self.row < 13 and walls[self.row + 1][self.col] != 1:
#                 self.direction = 2
#                 self.row += 1
#                 self.y = [(36 * self.row) + 3, (36 * (self.row + 1)) - 3, (36 * (self.row + 1)) - 3]
#         elif direction == 3: #going left
#             if self.col > 0 and walls[self.row][self.col - 1] != 1:
#                 self.direction = 3
#                 self.col -= 1
#                 self.x = [(36 * self.col) + 18, (36 * self.col) + 3, (36 * (self.col + 1)) - 3]
#         elif direction == 4: #going right
#             if self.col < 14 and walls[self.row][self.col + 1] != 1:
#                 self.direction = 4
#                 self.col += 1
#                 self.x = [(36 * self.col) + 18, (36 * self.col) + 3, (36 * (self.col + 1)) - 3]
#         self.collectKeys()
#         self.openDoors()
#         self.collectChip()
#         self.unlock()
#         self.robber()
                
#     """ This function checks if the player is standing on
#         a space with a key. If they are, the player collects
#         that key and the key is removed from the list of keys
#         so it will not be drawn in the next frame.
#     """
    
#     def collectKeys(self):
#         global keys
#         keyToRemove = -1
#         for i in range(len(keys)):
#             key = keys[i]
#             if self.row == key['row'] and self.col == key['col']:
#                 if key['color'] == 'b':
#                     self.bk += 1
#                     keyToRemove = i
#                     break
#                 elif key['color'] == 'r':
#                     self.rk += 1
#                     keyToRemove = i
#                     break
#                 elif key['color'] == 'y':
#                     self.yk += 1
#                     keyToRemove = i
#                     break
#                 elif key['color'] == 'g':
#                     self.gk += 1
#                     keyToRemove = i
#                     break
#         if keyToRemove > -1:
#             del keys[keyToRemove]
        
#     """ This function checks if the player is standing
#         on a space with a door. If they have a key that
#         is the same color as the door, then the door will 
#         open and, unless the color is green, the player's
#         number of keys in that color decreases by 1.
#     """
#     def openDoors(self):
#         global doors, openDoorSound
#         doorToRemove = -1
#         for i in range(len(doors)):
#             door = doors[i]
#             if self.row == door['row'] and self.col == door['col']:#and not door['isOpen']:
#                 if door['color'] == 'b':
#                     if self.bk > 0:
#                         self.bk -= 1
#                         doorToRemove = i
#                         break
#                     else:
#                         # THIS ONLY CHECKS IF WALKING 
#                         # INTO BLUE DOOR FROM LEFT
#                         # OR RIGHT
#                         if self.direction == 3:
#                             # approaching blue door from right
#                             self.col += 1
#                             self.x = [(36 * self.col) + 18, (36 * self.col) + 3, (36 * (self.col + 1)) - 3]
#                         elif self.direction == 4:
#                             # approaching blue door from left
#                             self.col -= 1
#                             self.x = [(36 * self.col) + 18, (36 * self.col) + 3, (36 * (self.col + 1)) - 3]
#                 if door['color'] == 'r':
#                     if self.rk > 0:
#                         self.rk -= 1
#                         doorToRemove = i
#                         break
#                     else:
#                         # THIS ONLY CHECKS IF WALKING 
#                         # INTO RED DOOR FROM LEFT
#                         # OR RIGHT
#                         if self.direction == 3:
#                             # approaching red door from right
#                             self.col += 1
#                             self.x = [(36 * self.col) + 18, (36 * self.col) + 3, (36 * (self.col + 1)) - 3]
#                         elif self.direction == 4:
#                             # approaching red door from left
#                             self.col -= 1
#                             self.x = [(36 * self.col) + 18, (36 * self.col) + 3, (36 * (self.col + 1)) - 3]
#                 if door['color'] == 'y':
#                     if self.yk > 0:
#                         self.yk -= 1
#                         doorToRemove = i
#                         break
#                     else:
#                         # THIS IS ONLY IF THE YELLOW DOOR
#                         # IS APPROACHED WHEN PLAYER GOES RIGHT, LEFT OR UP
#                         if self.direction == 3:
#                             # approaching yellow door from right
#                             self.col += 1
#                             self.x = [(36 * self.col) + 18, (36 * self.col) + 3, (36 * (self.col + 1)) - 3]
#                         elif self.direction == 4:
#                             # approaching yellow door from left
#                             self.col -= 1
#                             self.x = [(36 * self.col) + 18, (36 * self.col) + 3, (36 * (self.col + 1)) - 3]
#                         elif self.direction == 1:
#                             # approaching yellow door from below
#                             self.row += 1
#                         self.y = [(36 * self.row) + 3, (36 * (self.row + 1)) - 3, (36 * (self.row + 1)) - 3]
#                 if door['color'] == 'g':
#                     if self.gk > 0:
#                         doorToRemove = i
#                         break
#                     else:
#                         # THIS IS ONLY IF THE GREEN DOOR
#                         # IS APPROACHED WHEN PLAYER GOES RIGHT OR LEFT
#                         if self.direction == 3:
#                             # approaching red door from right
#                             self.col += 1
#                             self.x = [(36 * self.col) + 18, (36 * self.col) + 3, (36 * (self.col + 1)) - 3]
#                         elif self.direction == 4:
#                             # approaching red door from left
#                             self.col -= 1
#                             self.x = [(36 * self.col) + 18, (36 * self.col) + 3, (36 * (self.col + 1)) - 3]
#         if doorToRemove > -1:
#             del doors[doorToRemove]
#             openDoorSound.play()
#     def robber(self):
#         if self.row == robber["row"] and self.col == robber["col"]: 
#             self.bk =0
#             self.rk =0
#             self.yk =0
#             self.gk =0 
#             robbedSound.play()
#     def Youwin(self):
#         text("youwin",100,100)
#         text("http://bit.ly/2b4vS1h",150,150)

#     """ This function checks if the player has collected all
#         the keys in the level. If they have, then the exit
#         lock opens and the player can go to the portal to 
#         complete the level.    
#     """
#     def unlock(self):
#         global exitLock
#         if self.row == exitLock['row'] and self.col == exitLock['col']:
#             if self.chips == totalChips:
#                 exitLock['isOpen'] = True
#                 openDoorSound.play()
#             else:
#                 self.col += 1
#                 self.x = [(36 * self.col) + 18, (36 * self.col) + 3, (36 * (self.col + 1)) - 3]
#     """ This function checks if the player is on the portal.
#         If they are, it will play a sound effect, tell the 
#         player that they have won, and display the time 
#         they took to complete the level. It will also
#         exit the program.
#     """
#     def complete(self):
#         if self.row == exitPortal['row'] and self.col == exitPortal['col']:
#             winSound.play()
#             stroke(0, 0, 0)
#             fill(0, 0, 0)
#             rect(150, 175, 275, 100)
#             stroke(0, 255, 0)
#             fill(0, 255, 0)
#             textSize(25)
#             text("You Win!!", 225, 200)
#             text("Time You Had Left: " + str(secinverse), 160, 245)
#             exitp()
            
#     """ This function checks if the player is standing
#         on a tile with a chip. If they are, it will 
#         play a sound effect, add it to the number of chips
#         the player has collected, and will change the value
#         in the walls array where the chip was placed to 0, 
#         so the chip will not be drawn.
#     """
#     def collectChip(self):
#         chipToRemove = -1
#         for y in range(len(walls)):
#             for x in range(len(walls[y])):
#                 if walls[self.row][self.col] == 2:
#                     self.chips += 1
#                     collectChipSound.play()
#                     walls[self.row][self.col] = 0
#                     break
                    
                    
#     def checkGhostCollision(self):
#         kill = False
#         for ghost in ghosts:
#             if (self.row == ghost.row and self.col == ghost.column):
#                 kill = True
#                 break
#         return kill
                    
#     def getCol():
#         return self.col
    
#     def getRow():
#         return self.row

# """ This is the processing package's setup function.
#     In it, I set the size of the map, the background
#     color, and I create the character.
    
#     Note that in the Char class's __init__ function,
#     there are 3 parameters: self, initRow, and initCol.
#     We only pass 2 in, because self is the object.
# """
# def setup():
#     global character, Robber, ghosts
#     size(540, 504)
#     background(191, 191, 191)
#     character = Char(6, 7)
#     ghost1 = Ghost(4,7,"r",1)
#     ghosts = [ghost1]
#     Robber = loadImage("http://t13.deviantart.net/5h8S7mkLDTMacr_bsTYQM0XxL1g=/fit-in/700x350/filters:fixed_height(100,100):origin()/pre13/cd6b/th/pre/f/2013/049/c/e/mario_wants_his_life_back__be_a_robber_by_porno_bookstore-d5vfk6z.png")
    
# """ This is the processing package's draw function.
#     It is called once every frame. This will re-draw 
#     the background to clear the previous frame from the
#     canvas, then draw the lines for the grid. It then
#     draws all the data from the walls 2-D array, the doors,
#     the keys, the exit, the player, and then all the data
#     (the time, keys collected and chips collected).
    
#     Note that to draw the player character, I had to write
#     'character.draw()'. The draw() function in the class 
#     Char has one parameter: self. The variable 'character' 
#     is of type Char. Thus, the 'self' that is referred to 
#     is the 'character' variable we created since it holds 
#     all the data related to that object.
# """
# def draw():
#     global moveGhostCounter
#     background(191, 191, 191)
#     drawLines()
#     drawWallsArray()
#     drawDoors()
#     drawKeys()
#     drawExit()
#     image(Robber, 142, 108, 36, 36)
#     drawData()
#     character.draw()
#     for ghost in ghosts:
#         ghost.draw()
#     if character.checkGhostCollision():
#         textSize(40)
#         fill(255,0,0)
#         text("YOU LOSE!!", (width/2)-100, height/2)
#         exitp()
#     if moveGhostCounter == 0:
#         for ghost in ghosts:
#             ghost.move()
#         moveGhostCounter = 50
#     moveGhostCounter -= 1
# """ This processing function listens for key press events.
#     Since the player moves when the key is pressed, they
#     are able to hold the corresponding arrow key down and
#     continue to move in that direction until hitting a wall.
    
#     The keyCode 32 is the space bar. When it is pressed, 
#     we exit the program.
# """
# def keyPressed():
#     if keyboard.keyCode == LEFT: 
#         character.move(3)
#     elif keyboard.keyCode == RIGHT: 
#         character.move(4)
#     elif keyboard.keyCode == UP:
#         character.move(1)
#     elif keyboard.keyCode == DOWN: 
#         character.move(2)
#     elif keyboard.keyCode == 32: # space key pressed
#          exitp()
    
# run()
