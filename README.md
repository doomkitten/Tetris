# Tetris

A Tetris clone in Python. Tkinter used for graphics.  

##Personal Goals

* **Re-Learn Python** - I wanted to re-familiarize myself with Python and basic Python data structures. 
* **MVC** - This was a (pretty sad) attempt to use a modified MVC design with Python and Tkinter.
* **Modularity** - Create independent modules for use in future games (Block, Piece, and Board)

##Critique

* **Waaaaay Too Many Iterations** - Wow, talk about using a 'for' loop. This Tetris clone is definitely not easy on the iterations. But hey, it's Tetris. Whatevs.
* **Board** - The Board module isn't generic enough. I should have probably created a Board class, then a TetrisBoard class
* **Drop Piece** - I need to add a 'soft drop' function for continuous down key press. I'm just over Tetris right now.
* **Game Over** - Not happy how I end the game. Testing the board level instance variable for a string ("Game Over") seems really awkward.
* **Long** - Code is overly verbose.

#### Over Tetris...
![alt text](http://media.giphy.com/media/Odnr4cLZA3iqA/giphy.gif "Frustrated cat can't believe this is the 12th time he's clicked on an auto-linked README.md URL")
