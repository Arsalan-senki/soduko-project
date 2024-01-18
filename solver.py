import random


COUNTER = 0 
    

def available_pos(grid, val, row, col):
    block_i = (row // 3) * 3
    block_j = (col // 3) * 3
        
    for b_i in range(block_i, block_i + 3):
        for b_j in range(block_j, block_j + 3):
            if grid[b_i][b_j] == val:
                return False
                
    for j in range(9):
        if grid[row][j] == val:
            return False
            
    for i in range(9):
        if grid[i][col] == val:
            return False
            
    return True
        
    
def start_element(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i,j
        
    return -1,-1
    

def solve(grid) :
    global COUNTER
    i, j = start_element(grid)
        
    if i == -1 and j == -1:
        counter = COUNTER
        COUNTER = 0
        return True, counter    
    
    for num in range(1, 10):
        if available_pos(grid,num, i, j):
            grid[i][j] = num

            if data := solve(grid):
                return grid, data[1]
                
            grid[i][j] = 0
        else : 
            COUNTER += 1
    return False
        
        
def print_grid(grid):   
    for row in grid:
        print(row)
  
  
def generate_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Fill in the diagonal boxes with random numbers
    for i in range(0, 9, 3):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(nums)
        for j in range(3):
            board[i+j][i+j] = nums[j]

    # Solve the puzzle to create a valid Sudoku solution
    solve(board)

    # Remove a certain number of cells to create a puzzle
    num_cells_to_remove = random.randint(40, 50)
    cells_removed = 0
    while cells_removed < num_cells_to_remove:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            cells_removed += 1

    return board
        
def has_duplicates(grid):
    # Check for duplicates in rows
    for row in grid:
        if has_duplicates_in_list(row):
            return True

    # Check for duplicates in columns
    for col in range(9):
        column = [grid[row][col] for row in range(9)]
        if has_duplicates_in_list(column):
            return True

    # Check for duplicates in blocks
    for block_i in range(0, 9, 3):
        for block_j in range(0, 9, 3):
            block = []
            for i in range(3):
                for j in range(3):
                    block.append(grid[block_i + i][block_j + j])
            if has_duplicates_in_list(block):
                return True

    return False


def has_duplicates_in_list(lst):
    counts = [0] * 10
    for num in lst:
        if num != 0 and counts[num] == 1:
            return True
        counts[num] += 1
    return False        
  
    
def main():
    pass
    # grid1=[
    # [1,1,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,1,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0]
    # ]
    # grid2 = [
    #     [1, 0, 3, 4, 0, 6, 7, 8, 9],
    #     [4, 5, 6, 7, 8, 9, 1, 2, 3],
    #     [7, 8, 9, 1, 2, 3, 4, 5, 6],
    #     [2, 1, 4, 3, 6, 5, 8, 9, 7],
    #     [3, 6, 7, 9, 1, 8, 2, 4, 5],
    #     [5, 9, 8, 2, 4, 7, 3, 6, 1],
    #     [6, 3, 1, 8, 9, 2, 5, 7, 4],
    #     [8, 4, 5, 6, 7, 1, 9, 3, 2],
    #     [9, 7, 2, 5, 3, 4, 6, 1, 8]]
    # generated_grid = Generate_Table()
    # generated_grid.Generate()
    

    
    

if __name__ == '__main__':
    main()


'''
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[4, 5, 6, 7, 8, 9, 1, 2, 3],
[7, 8, 9, 1, 2, 3, 4, 5, 6],
[2, 1, 4, 3, 6, 5, 8, 9, 7],
[3, 6, 7, 9, 1, 8, 2, 4, 5],
[5, 9, 8, 2, 4, 7, 3, 6, 1],
[6, 3, 1, 8, 9, 2, 5, 7, 4],
[8, 4, 5, 6, 7, 1, 9, 3, 2],
[9, 7, 2, 5, 3, 4, 6, 1, 8]
'''