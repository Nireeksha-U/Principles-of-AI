import numpy as np
import string
import random

def generate_crossword(words):
    max_length = max(len(word) for word in words)
    grid_size = max_length + 2
    
    grid = np.full((grid_size, grid_size), " ", dtype=str)
    
    for word in words:
        placement = random.choice(["horizontal", "vertical"])
        row, col = (np.random.randint(1, grid_size - 1), np.random.randint(1, grid_size - len(word))) if placement == "horizontal" else (np.random.randint(1, grid_size - len(word)), np.random.randint(1, grid_size - 1))
        
        if all(grid[row+i, col] == " " or grid[row+i, col] == word[i] for i in range(len(word))) if placement == "vertical" else all(grid[row, col+i] == " " or grid[row, col+i] == word[i] for i in range(len(word))):
            grid[row:row+len(word), col] = list(word) if placement == "vertical" else list(word)

    return grid

def generate_random_char():
    return random.choice(string.ascii_lowercase)

def display_crossword(grid, reveal=False):
    for row in grid:
        print(" ".join(row if reveal else [generate_random_char() if cell == " " else cell for cell in row]))

def play_crossword(words):
    repeated, w = [], 0
    while w < len(words):
        guess = input("Enter the word: ").lower()
        if guess in repeated:
            print(f"{guess} is repeated. Try other strings as well :-)")
            continue
        if guess in words:
            print(f"Correct! {guess} is the right word.")
            repeated.append(guess)
            w += 1
        else:
            print(f"{guess} is incorrect!")

if __name__ == "__main__":
    words = ["python", "programming", "crossword", "puzzle", "hello"]
    crossword = generate_crossword(words)
    
    print("Welcome to the Crossword Puzzle Game!")
    print("Try to guess the words and fill in the blanks.")

    display_crossword(crossword)
    play_crossword(words)

    print("Thanks for playing!")
