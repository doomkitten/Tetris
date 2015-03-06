from Tkinter import Frame, Canvas
from Board import Board

class BoardGUI( Frame ):
	
	def __init__(self, parent = None, x=10 , y=20, scale=30, padding=5):
		
		self.parent = parent
		
		#Size of Blocks in pixels
		self.scale = scale
		
		#Amount of padding in pixels
		self.padding = padding
		
		#Playing board	
		self.board = Board(x, y)
			
		Frame.__init__(self, parent)
		
		self.canvas = Canvas(parent, 
							 height= (y * scale)+padding, 
							 width = (x * scale)+padding)
		
		self.canvas.pack()
		
		#Draw First Piece
		self.draw()
				
	'''
	Move Blocks on board
	'''				
	def move( self, direction ):
		if type(self.level) is int:
			self.board.move(direction)
			self.draw()
	
	'''
	Draws a piece (either new or currently in play)
	'''
	def draw( self ):
		if self.board.piece is None:
			self.delete_blocks(self.board.deleted_blocks)
			self.redraw_board()
			self.draw_piece()
		else:
			self.redraw_piece()
	
	'''
	Draws a new piece
	Adds tkinter ids to piece blocks
	'''	
	def draw_piece( self ):
		self.board.new_piece()
		color = self.board.color
		
		new_ids = {}
		
		for coord in self.board.coords:
			x0, y0, x1, y1 = self.drawingCoordinates(coord)
			new_ids[coord] = self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
		
		self.board.ids = new_ids
	
	'''
	Re-Draws piece with existing tkinter ids
	'''
	def redraw_piece( self ):
		for coord in self.board.ids:
			x0, y0, x1, y1 = self.drawingCoordinates(coord)
			id = self.board.ids[coord]
			self.canvas.coords(id, x0, y0, x1, y1)
	
	'''	
	Deletes lists of blocks from canvas
	'''
	def delete_blocks( self, blocks_to_delete ):
		for id in blocks_to_delete:
			self.canvas.delete(id)
	
	'''
	Redraws the landed pieces
	'''
	def redraw_board( self ):
		for y in range(len(self.board.landed)):
			for x in range(len(self.board.landed[y])):
				x0, y0, x1, y1 = self.drawingCoordinates((x,y))
				id = self.board.landed[y][x]
				if id is not None:
					self.canvas.coords(self.board.landed[y][x], x0, y0, x1, y1)
	
	'''
	Creates drawing coordinates from (x,y) block coordinates
	'''
	def drawingCoordinates( self, coords ):
		x,y = coords
		x0 = (x * self.scale) + self.padding
		y0 = (y * self.scale) + self.padding
		x1 = x0 + self.scale
		y1 = y0 + self.scale
		return (x0, y0, x1, y1)  
	
	'''
	Properties
	'''
	#Current Score
	@property
	def score( self ):
		return self.board.score
	
	#Current Level	
	@property
	def level( self ):
		return self.board.level
			 	
'''
Unit Test 
'''
if __name__ == '__main__':
	root = Tk()
	root.title("Alaina's Super Awesome Tetris")
	game = BoardGUI(root)
	root.mainloop() 
	