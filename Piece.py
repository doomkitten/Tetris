from Block import Block

class Piece( object ):
	
	def __init__( self, coords = [], color = "black" ):
	
	    #List of blocks in piece
	    self.blocks = self.initialize_blocks(coords, center_block = Block())
	    
	    self.color = color
	
	
	'''
	Creates blocks from coords, adds center block
	Initializes piece coords to place bottom, left block at (0,0)
	'''
	def initialize_blocks( self, coords, center_block = None ):
	    
	    blocks = []
	    
	    for coord in coords:
	        x,y = coord
	        blocks += [Block(x,y,center_block)]
	    
	    if center_block:
	        blocks += [center_block]
	    
	    dx = sorted([block.x for block in blocks])[0]
	    dy = sorted([block.y for block in blocks])[0]
	    
	    for block in blocks:
	        block.x -= dx
	        block.y += dy
	        
	    return blocks
	    
	'''
    Returns a list of block coordinates of move
    L - Left, R - Right, D - Down, CC - Rotate
    '''
	def move (self , direction ):
	    return [block.move(direction) for block in self.blocks]
			
	
	'''		
	Properties  
	''' 
	#Int - Width of piece, used later for randomizing drop location                 	
	@property
	def width( self ):
	    xvalues = sorted([block.x for block in self.blocks])
	    return xvalues[-1] - xvalues[0] 
	
	#Dict - Block coords(key) with corresponding ids (value) in Piece   
	@property
	def IDs( self ):
	    return dict(zip(self.coords, self.id_list))
     
     
    #List - Coordinates of blocks in Piece 		
	@property														
	def coords(self):
		return [block.coords for block in self.blocks]
	
	#List - ids of blocks in Piece
	@property 
	def id_list(self):
		return [block.id for block in self.blocks]	
	
		
	'''		
	Setters  
	''' 		
	#Sets piece coordinates with list of new_coords
	@coords.setter
	def coords(self, new_coords):
	    if len(new_coords) is len(self.blocks):
	        for new_coord, block in zip(new_coords, self.blocks):
	            block.coords = new_coord
	
	#Sets ids for each block
	@IDs.setter
	def IDs(self, ids):  
	    for block, id in zip(self.blocks, ids):
	        block.id = id
	
	
	'''
	Printing Methods
	'''		
	def __str__(self):
		return str(self.coords) + " " + self.color

'''
Unit Test
'''
if __name__ == '__main__':
	pass