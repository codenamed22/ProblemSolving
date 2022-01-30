"""

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""




class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        self.row = len(board)
        self.col = len(board[0])
        
        #create a list of border indexes , rows -> 0,0 to 0,n-1 and m,0 to m,n-1 , same for colms
        bordercells = list(product(range(self.row),[0,self.col-1])) + list(product([0,self.row-1],range(self.col)))
        
        #for each border cell find all cells adjacent to it, these will be marked safe
        for i,j in bordercells:
            self.markCells(board, i, j)
         
        #check all cells, if a cell is marked safe, replace it with O, all other O cells were not marked safe so delete it
        for i in range(self.row):
            for j in range(self.col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '$':
                    board[i][j] = 'O'
            
            
    #utility function to mark adjacent cells to the border Os       
    def markCells(self, board, i, j):
        if board[i][j] == 'O':
            board[i][j] = '$'
            if j < self.col-1: self.markCells(board,i, j+1)
            if i < self.row-1: self.markCells(board,i+1, j)
            if j > 0: self.markCells(board,i, j-1)
            if i > 0: self.markCells(board,i-1, j)
