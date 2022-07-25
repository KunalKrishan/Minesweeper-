import random


#1 
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        self.board = self.make_new_board()
        self.assign_values_to_board()

        self.dug = set()
    

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)]] for _ in range(self.dim_size)

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2-1)
            row = loc // self.dim_size
            col = loc % self.dim_size


            if board[row][col]=='*':
                continue
             

            board[row][col] = '*'
            bombs_planted += 1

        return board


            


#play the game 
def play(dim_size=10, num_bombs=10):
    #Step 1: make the board and plant the bombs
    # 2: Show the user the board and ask for where they want to dig 
    # 3a: If location is a bomb, show game over message
    # 3b: if location is not a bomb, dig recursively until each squarre is at least next to a bomb
    # 4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!
    pass 