import random

class Minesweeper:
    # Initialize the grid and mines
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        # Check the amount of mines is valid or not
        if mines > rows * cols:
            raise ValueError(f"Number of mines ({mines}) exceeds total cells ({rows * cols})")
        # intialize empty grid
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]

    def generate_board(self):
        # Return the grid
        return self.board

    def place_mines(self, first_click):
        first_row, first_col = first_click
        
        if not (0 <= first_row < self.rows and 0 <= first_col < self.cols):
            raise ValueError("First click position is out of bounds")

        exclude_index = first_row * self.cols + first_col
        total_cells = self.rows * self.cols
        
        mine_positions = []
        while len(mine_positions) < self.mines:
            random_index = random.randint(0, total_cells - 1)
            row = random_index // self.cols
            col = random_index % self.cols
            
            if random_index != exclude_index and [row, col] not in mine_positions:
                mine_positions.append([row, col])
                self.board[row][col] = "M"

        return mine_positions

# Test
if __name__ == "__main__":
    try:
        game = Minesweeper(5, 5, 5)
        print("Initial board:")
        for row in game.generate_board():
            print(row)
        mines = game.place_mines([2, 2])
        print("\nMine positions:", mines)
        
        game_invalid = Minesweeper(2, 2, 5)
    except ValueError as e:
        print(f"Error: {e}")