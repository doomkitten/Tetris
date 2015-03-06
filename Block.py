#Individual Block
#A relative center block (used for rotation) can be passed 
#If no center block is passed, the block as it's own center block  

class Block(object):

	def __init__( self, x = 0, y = 0, center_block = None ):
		
		self.x = x
		self.y = y
		
		#Block id, intended use for tkinter 
		self.id = None
		
		#Center block
		self.center = center_block if center_block else self
	
	
	'''
	Selects type of move, returns new coordinates	
	'''
	def move(self, direction):
	    if direction is 'CC' or direction is 'C':
	        return self.rotate(direction)
	    else:
	        return self.move_adjacent(direction)
	
	'''
	Returns coordinates for an adjacent move
	'''
	def move_adjacent(self, direction):
	    dx, dy = { 	'L' : (-1, 0), 'R' : (1, 0), 'D' : (0, 1)}.get(direction)
	    x = dx + self.x
	    y = dy + self.y
	    return x,y
	
	'''
	Returns coordinates for a rotational move
	'''						
	def rotate(self, direction):
	    dx, dy = { 	'CC' : (1, -1), 'C' : (-1,1)}.get(direction)
	    x = dx*self.dy + self.center.x
	    y = dy*self.dx + self.center.y
	    
	    return x,y
	
	
	'''
	Returns coords (x,y)
	'''	
	@property
	def coords( self ):
		return self.x, self.y
	
	'''
	Sets coords (x,y)
	'''
	@coords.setter	
	def coords( self, coord ):
	    newx, newy = coord
	    self.x = newx
	    self.y = newy
		
		
	'''
	Properties
	'''
	#x distance from center block (x)
	@property
	def dx( self ):
		return self.x - self.center.x
	
	#y distance from center block (y)
	@property
	def dy( self ):
		return self.y - self.center.y
		
		
	'''
	Printing Methods
	'''			
	def __str__( self ):
		return str(self.coords) + " id: " + str(self.id)
		
		
'''
Unit Test
'''
if __name__ == '__main__':
	center = Block()
	myBlock = Block(1,0,center)
	myBlock.id = 5
	print myBlock
	print myBlock.center
