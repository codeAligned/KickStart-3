"""
Arsh recently found an old rectangular circuit board that he would like to recycle. 
The circuit board has R rows and C columns of squares.

Each square of the circuit board has a thickness, measured in millimetres. 
The square in the r-th row and c-th column has thickness Vr,c. 
A circuit board is good if in each row, the difference between the thickest square and the least thick square is no greater than K.

Since the original circuit board might not be good, Arsh would like to find a good subcircuit board.
A subcircuit board can be obtained by choosing an axis-aligned subrectangle from the original board and taking the squares in that subrectangle. 
Arsh would like your help in finding the number of squares in the largest good subrectangle of his original board.

Similar to leetcode 134
"""

import numpy as np

"""
3
1 4 0
3 1 3 3
2 3 0
4 4 5
7 6 6
4 5 0
2 2 4 4 20
8 3 3 3 12
6 6 3 3 3
1 6 8 6 4
"""


def parse_input(T, rows, cols, acceptable_difference, board):
    result = []
    t = 0
    while t < T:
        pass
    return result
    

class Solution(object):
    def __init__(self, test_case_id, board_rows, board_cols, acceptable_difference, thicknesses):
        self.test_case_id = test_case_id
        self.rows = board_rows
        self.cols = board_cols
        self.K = acceptable_difference
        self.thickness_matrix = thicknesses
    
    def solve(self):
        row_ptr=0
        col_ptr=0
        result = 0 
        while row_ptr<self.rows:
            row_thickness = self.thickness_matrix[row_ptr][col_ptr]
            while col_ptr < self.cols:
                if row_thickness == self.thickness_matrix[row_ptr][col_ptr]:
                    col_ptr += 1
                



    
    

if __name__ == "__main__":
    T = 3

    # Case #1: 2
    s = Solution(1, 1, 4, 0, [[3, 1, 3, 3]])

    # Case #2: 2
    s = Solution(2, 2, 3, 0, [[4, 4, 5],[7, 6, 6]])

    # Case #3: 6
    s = Solution(3, 4, 5, 0, [[2,2,4,4,20], [8,3,3,3,12], [6,6,3,3,3], [1,6,8,6,4]])
    






#     T = 3
# 1 4 2
# 3 1 3 3
# 3 3 2
# 0 5 0
# 8 12 3
# 7 10 1
# 4 4 8
# 20 10 20 10
# 10 4 5 20
# 20 5 4 10
# 10 20 10 20
  
# Case #1: 4
# Case #2: 3
# Case #3: 4

  