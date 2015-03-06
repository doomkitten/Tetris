from time import sleep
from random import randint
import tkMessageBox
import sys
from BoardGUI import BoardGUI

#Yes, I realize importing with * is incredibly bad form. 
#But I am sooooo over Tetris. Over. Tetris.
from Tkinter import *


#Board Size (in Blocks)
Max_X = 10
Max_Y = 20

#Block Size for Scale (in Pixels)
BLOCK_SIZE = 30

#Padding for Edge
PADDING = 5

#Initial Delay from game (ms)
DELAY = 1000

'''
Class to display Score and Level (Frame with Label) 
'''
class status_bar( Frame ):


    def __init__(self, parent):
        Frame.__init__( self, parent )
        
        self.status = StringVar()
        		
        self.label = Label( self, bd=1, relief=SUNKEN, anchor=W, textvariable=self.status )
        self.label.pack(fill = X)
    '''
    Sets new status (score and level)
    '''
    def set( self, new_status ):
    	self.status.set(new_status)
 
'''
Tetris Game Controller 
'''       
class game_controller(object):

    def __init__(self, parent ):
    
        self.parent = parent
        self.delay = DELAY
		
        self.status_bar = status_bar(parent)
        self.status_bar.pack(fill=X)
        
        self.boardFrame = BoardGUI(x=Max_X, y=Max_Y, scale=30, padding=5)
        self.boardFrame.pack(side=BOTTOM)
        
        #Bindings for keys
        self.parent.bind("<Left>", self.left_callback)
        self.parent.bind("<Right>", self.right_callback)
        self.parent.bind("<Up>", self.up_callback)
        self.parent.bind("<Down>", self.down_callback)
        
        #Begins Game
        self.timed_move_down()
    
    '''
    Creates the timed move down of piece
    '''
    def timed_move_down( self ):
    
    	self.boardFrame.move('D')
    	
    	#If Level is "Game Over", end game
    	if type(self.boardFrame.level) is not int:
    		print self.boardFrame.level
    		new_status = self.boardFrame.level
    		self.status_bar.set(new_status)
    		
    	#Otherwise, display score and level, continue game	
    	else: 
    		new_status = "Score: " + str(self.boardFrame.score) + " Level: " + str(self.boardFrame.level)
    		self.status_bar.set(new_status)
    		self.parent.after( self.delay/self.boardFrame.level, self.timed_move_down )    			
		
    '''
    Methods to handle Key presses
    '''		
    def left_callback( self, event ):
    	self.handle_move('L')
    
    def right_callback( self, event ):
    	self.handle_move('R')
    
    def up_callback( self, event ):
        self.handle_move('CC')
        
    def down_callback( self, event ):
    	self.handle_move('D')
    
    def handle_move(self, direction):
    	self.boardFrame.move(direction)
    	
'''
Main Loop
'''		
def main():
    root = Tk()
    root.title("Alaina's Awesome Tetris!")
    theGame = game_controller( root )
    root.mainloop()


if __name__ == '__main__':
    main()  