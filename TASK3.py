def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def find_empty_location(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)  
    return None

def is_safe(grid, row, col, num):
   
    for x in range(9):
        if grid[row][x] == num:
            return False
   
 
    for x in range(9):
        if grid[x][col] == num:
            return False
   

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
   
    return True

def solve_sudoku(grid):
    empty_loc = find_empty_location(grid)
    if not empty_loc:
        return True  
   
    row, col = empty_loc
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
           
            if solve_sudoku(grid):
                return True
           
            grid[row][col] = 0  
   
    return False


if __name__ == "__main__":
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
   
    print("Original Sudoku Grid:")
    print_grid(sudoku_grid)
   
    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku Grid:")
        print_grid(sudoku_grid)
    else:
        print("No solution exists")