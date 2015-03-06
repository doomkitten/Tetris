from Pieces import T,O,I,J,L,Z,S
from random import choice
from math import factorial

PIECES_LIST = [T,O,I,J,L,Z,S]
LEVEL_UP_ROWS = 2
SCORE_BASE = 40 

class Board( object ):
	
	def __init__(self, x=10 , y=20, piecesList=PIECES_LIST):
	
		#Size of Board in blocks
		self.x = x
		self.y = y
		
		#List of Pieces for game
		self.piecesList = piecesList
		
		#Current piece in play
		self._piece = None
		
		#The playing board with each landed piece in corresponding
		#coordinate. Empty spaces are occupied by None
		self.landed = [[None for i in range(x)]for j in range(y)]
		
		#Number occupied (landed blocks) in each row
		self.rowCount = y*[0]
		
		#List of blocks to be deleted
		self.deleted_blocks = []
		
		#Score, level, and total number of rows cleared
		self.score = 0
		self.level = 1
		self.rows_removed = 0

		
	'''	
	Create new Piece, randomize drop location 
	'''
	def new_piece( self ):
	
		new = choice(self.piecesList)()
		
		dx = choice(range(self.x - new.width))			
		
		for block in new.blocks:
			block.x += dx 
			
		self.piece = new	
	
	'''	
	Move piece in direction
	Return False if move is not possible
	'''
	def move(self, direction):
	
		new_coords = self.piece.move(direction)
		
		#Test new block coordinates
		for coord in new_coords:
			x,y = coord
			if not self.check_bounds(x,y, direction): 
				return False
			
		#No bounds issues? Change location and move block.	
		self.coords = new_coords
		if direction is 'D':
			return True
	
	'''	
	Check if (x,y) board location is available
	Return False if (x,y) is out of bounds or full
	'''
	def check_bounds( self, x , y, direction ):
	
		#If too far right or left, don't move
		if x < 0 or x >= self.x :
			return False
		
		#If the space is occupied, don't move
		elif not self.empty_space(x,y):
		
		#If moving down into an occupied space, land the piece
			if direction is 'D':
				self.land_piece()
			return False
		
		#Otherwise, move
		else: 
			return True
	
	'''
	Check if space is empty on board
	'''
	def empty_space( self, x , y ):
		if y < 0:
			return True
		elif y >= self.y:
			return False
		elif self.landed[y][x] is not None:
			return False
		else:
			return True
 
	'''
	Land Piece on Board
	''' 
 	def land_piece( self ):
 	
 		rows_removed = 0 
 		
 		#Check if Game is over
 		for coord in self.ids:
 			x,y = coord
 			if y <= 0:
 				self.game_over()
 				return False
		
		#If not, land piece on the board		
		for coord in self.ids:
			x,y = coord
			self.landed[y][x] = self.ids[coord]
			self.rowCount[y] += 1
 		
 		#Check if rows can be deleted
		self.delete_rows()
		
		self.piece = None
	
	'''			
	Delete full rows from board
	'''
	def delete_rows( self ):
		
		self.deleted_blocks = []
		rows_removed = 0
		
		#Remove full rows from the board
		for y,x in enumerate(self.rowCount):
			if x >= self.x:	
				del self.rowCount[y]
				self.rowCount.insert(0,0)
				self.deleted_blocks.extend(self.landed.pop(y))
				self.landed.insert(0, [None for x in range(self.x)])
				rows_removed += 1
		
		#Add new score, the new number of rows cleared, and the new level
		if rows_removed:
			self.score += self.new_score(rows_removed)
			self.rows_removed += rows_removed
			self.level = self.new_level()
	
	'''
	Ends Game
	'''	
	def game_over( self ):
		self.level = "Game Over"
	
	'''
	Calculate score from last landed piece and deleted rows
	'''
	def new_score( self, rows_removed ):
		new_score = (self.level+1) * factorial(rows_removed)*SCORE_BASE
		if rows_removed is not 1:
			new_score += factorial(rows_removed)*10
		return new_score
	
	'''
	Calculate level 
	'''
	def new_level( self ):
		return self.rows_removed/LEVEL_UP_ROWS + 1
		

	'''		
	Properties
	'''
	#Piece - piece on board
	@property
	def piece( self ):
		return self._piece
	
	#List - Coordinate list (x,y) piece	
	@property 
	def coords( self ):
		return self.piece.coords
	
	#Dict - Piece coords (key) and corresponding ids (value)
	@property 
	def ids( self ):
		return self.piece.IDs
	
	#String - Color of current Piece
	@property 
	def color( self ):
		return self.piece.color
		
		
	'''		
	Setters
	'''		
	#Sets current piece in play
	@piece.setter
	def piece( self, value ):
		self._piece = value
		
	#Sets piece coords
	@coords.setter
	def coords( self, new_coords):
		self.piece.coords = new_coords
	
	#Takes a dictionary with corresponding coords (key) and ids (value) and
	# sets block ids for a new piece
	@ids.setter
	def ids( self, id_dict ):
		ids = []
		for coord in id_dict:
			ids += [id_dict[coord]]
		self.piece.IDs = ids
		
	'''
	Printing Methods
	'''			
	def __str__( self ):
		board_string = "Board: \n"
		for i in range(len(self.landed)):
			board_string += str(self.landed[i])
			board_string += "\n"
		board_string += "Piece: " + str(self.piece) + "\n"
		return board_string


'''		
Unit Test 
'''	 
if __name__ == '__main__':

	myBoard = Board()
	myBoard.new_piece()
	myBoard.move('D')
	print myBoard
	
	myBoard.land_piece()
	print myBoard

	myBoard.new_piece()
	myBoard.ids = {(8, 1): 2, (9, 0): 1, (8, 0): 4, (7, 0): 3}
	print myBoard.ids