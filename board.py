from const import *
from square import Square
from piece import *
from move import Move

class board: 

    def __init__(self) :
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range (COLS)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')
    
    def calc_moves(self, piece, row, col):
        '''
            this is going to calculate all the possible moves of a specific piece
            on a specific position
        '''
        
        def pawn_moves():
            # steps
            steps = 1 if piece.moved else 2
            
            # vertical moves
            start = row + piece.dir
            end = row + (piece.dir * (1+steps))
            for possible_move_row in range(start, end, piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].is_empty():
                        #create initial and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)
                        #create a new move
                        move = Move(initial, final)
                        piece.add_move(move)
                    else: break
                #not in range
                else: break 
                
            #diagonal moves
            possible_move_row = row + piece.dir
            possible_move_cols = [col - 1, col + 1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_cols):
                    if self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                        #create initial and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        #create a new move
                        move = Move(initial, final)
                        #append new move
                        piece.add_move(move)
                        
            
        def knight_moves():
            #8 possible moves
            possible_moves = [
                (row - 2 , col + 1),
                (row - 1 , col + 2),
                (row + 1 , col + 2),
                (row + 2 , col + 1),
                (row + 2 , col - 1),
                (row + 1 , col - 2),
                (row - 1 , col - 2),
                (row - 2 , col - 1),
            ]
            
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row] [possible_move_col].isempty_or_rival(piece.color):
                        #create squares of new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        #create new move
                        move = Move(initial, final)
                        #append new valid move
                        piece.add_move(move)
        
        def straightline_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr
                
                while True:
                    if Square.in_range(possible_move_row,possible_move_col):
                        #create squares of possible new move
                        initial  = Square(row,col)
                        final = Square(possible_move_row, possible_move_col)
                        
                        move = Move(initial, final)
                        # is empty
                        if self.squares[possible_move_row][possible_move_col].isempty():
                            piece.add_move(move)
                        #has enemy piece
                        if self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                            piece.add_move(move)
                            break
                        
                        #has team piece
                        if self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break
                    
                    else: break
                    
                    #incrementing incrs   
                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr
                        
        
        if isinstance(piece, Pawn): pawn_moves()
            
        
        elif isinstance(piece, Knight): knight_moves()
            
        elif isinstance(piece, Bishop): 
            straightline_moves([
                (-1, 1),(-1, -1),(1, 1),(1,-1)
                 ])
        
        elif isinstance(piece, Rook): 
            straightline_moves([
                (-1, 0),(1, 0),(0, 1),(0,-1)
                 ])
        
        elif isinstance(piece, Queen): straightline_moves([
                (-1, 1),(-1, -1),(1, 1),(1,-1),(-1, 0),(1, 0),(0, 1),(0,-1)
                 ])
        
        elif isinstance(piece, King): pass
        
        
        
            

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row,col)


    def _add_pieces(self, color):
        row_pawn, row_other = (6,7) if color == 'white' else (1,0)
        
        # pawns
        for col in range (COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
            
        
        #knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        
        #bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))
        
        #rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
        
        #queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        
        #king
        self.squares[row_other][4] = Square(row_other, 4, King(color))
        