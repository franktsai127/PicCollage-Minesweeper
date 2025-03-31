# PicCollage-Minesweeper

A implementation of the classic Minesweeper game logic in **Python**.  
This project creates a **2D board** with randomly placed mines, ensuring the first click is always safe.

## Features

- Generate a customizable grid (rows × cols)
- Place a specific number of mines randomly
- Ensure **the first clicked cell** is **never** a mine
- Return the mine positions for testing/debugging
- Lightweight and easy to expand

## How It Works

- The board is represented as a 2D list (`self.board`)
- Mines are placed **after** the first click to ensure safety
- The first-clicked cell is excluded from mine placement
- The mine cells are marked with `"M"`, others are `0` initially

## Example Run

```bash
python minesweeper.py
```

## Author

Created by **Frank Tsai**
