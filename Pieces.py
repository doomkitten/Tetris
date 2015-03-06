from Piece import Piece

T_COLOR = "Blue"
O_COLOR = "Yellow"
I_COLOR = "Purple"
J_COLOR = "Red"
L_COLOR = "Green"
Z_COLOR = "Pink"
S_COLOR = "Orange"

'''
A subclass of Piece
Only two iterations make a full rotation (I,S,Z)
'''

class limited_Rotate_Piece(Piece):
	def __init__(self, coords, color):
		super(limited_Rotate_Piece, self).__init__(coords,color)
		
		self.direction = 'CC'
	'''
	Overrides rotate method
	'''
	def move( self, direction ):
	    if direction is 'CC' or direction is 'C':
	        if self.direction is 'C':
	            self.direction = 'CC'
	        else:
	            self.direction = 'C'
	        return super(limited_Rotate_Piece, self).move(self.direction)
	    else:
	    	return super(limited_Rotate_Piece, self).move(direction)
	  
	    	
'''
A subclass of Piece
No rotation pieces (O)
'''	        
class no_Rotate_Piece(Piece):
	def __init__(self, coords, color):
		super(no_Rotate_Piece, self).__init__(coords, color)
	
	#Over rides rotate to do nothing
	def move( self, direction ):
	    if direction is 'CC':
	        return super(no_Rotate_Piece, self).coords
	    else: 
	        return super(no_Rotate_Piece, self).move(direction)


'''
Tetris Piece Classes
Subclasses of Piece (or no_Rotate_Piece, limited_Rotate_Piece)
'''	
				
class T(Piece):
	def __init__(self):
		super(T, self).__init__([(1,0),(0,1),(-1,0)],T_COLOR)

class O(no_Rotate_Piece):
	def __init__(self):
		super(O, self).__init__([(1,0),(0,1),(1,1)], O_COLOR)
		
class I(limited_Rotate_Piece):
	def __init__(self):
		super(I, self).__init__([(1,0),(-1,0),(-2,0)], I_COLOR)
			
class J(Piece):
	def __init__(self):
		super(J, self).__init__([(-1,1),(0,1),(0,-1)], J_COLOR)
		
class L(Piece):
	def __init__(self):
		super(L, self).__init__([(1,1),(0,1),(0,-1)], L_COLOR)
		
class Z(limited_Rotate_Piece):
	def __init__(self):
		super(Z, self).__init__([(1,1),(-1,0),(0,1)], Z_COLOR)
	
class S(limited_Rotate_Piece):
	
	def __init__(self):
		super(S, self).__init__([(0,1),(1,0),(-1,1)], S_COLOR)
		
'''
Unit Test
'''		
if __name__ == '__main__':
    pass
    myPiece = T()
    print myPiece
    print myPiece.width    
