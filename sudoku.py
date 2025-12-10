import tkinter as tk
from tkinter import messagebox

def is_valid(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def solve_puzzle():
    grid = []
    try:
        for i in range(9):
            row = []
            for j in range(9):
                val = entries[i][j].get()
                if val == '':
                    row.append(0)
                else:
                    num = int(val)
                    if num < 0 or num > 9:
                        raise ValueError
                    row.append(num)
            grid.append(row)

        if solve_sudoku(grid):
            for i in range(9):
                for j in range(9):
                    entries[i][j].delete(0, tk.END)
                    entries[i][j].insert(0, str(grid[i][j]))
        else:
            messagebox.showerror("Sudoku Solver", "No solution exists for the given Sudoku.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter only numbers from 0 to 9.")

# GUI setup
root = tk.Tk()
root.title("Sudoku Solver")

entries = [[None for _ in range(9)] for _ in range(9)]

main_frame = tk.Frame(root, bg="black", padx=2, pady=2)
main_frame.pack(pady=20)

# Create 9 subframes for each 3x3 block
for block_row in range(3):
    for block_col in range(3):
        block = tk.Frame(main_frame, bg="black", bd=2, relief="solid")
        block.grid(row=block_row, column=block_col, padx=1, pady=1)
        for i in range(3):
            for j in range(3):
                global_row = block_row * 3 + i
                global_col = block_col * 3 + j
                e = tk.Entry(block, width=3, font=('Arial', 18), justify='center', bd=1, relief='ridge')
                e.grid(row=i, column=j, padx=1, pady=1)
                entries[global_row][global_col] = e

solve_button = tk.Button(root, text="Solve", font=('Arial', 14), command=solve_puzzle)
solve_button.pack(pady=10)

root.mainloop()