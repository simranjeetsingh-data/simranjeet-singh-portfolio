"""Simple command-line Tic Tac Toe game for two players.

Players take turns entering numbers 1-9 corresponding to board positions:
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9

The first player to align three of their marks horizontally, vertically,
or diagonally wins.
"""
from __future__ import annotations

from typing import List, Optional


def display_board(board: List[str]) -> None:
    """Print the game board."""
    rows = [" | ".join(board[i : i + 3]) for i in range(0, 9, 3)]
    print("\n---------\n".join(rows))


def check_winner(board: List[str]) -> Optional[str]:
    """Return the winning marker if there's a winner."""
    win_conditions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None


def board_full(board: List[str]) -> bool:
    """Return True if the board has no empty spaces."""
    return all(space != " " for space in board)


def get_move(player: str, board: List[str]) -> int:
    """Prompt the current player for a move."""
    while True:
        try:
            move = int(input(f"Player {player}, choose your move (1-9): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")
            continue
        if move not in range(9):
            print("Move must be between 1 and 9.")
        elif board[move] != " ":
            print("That position is already taken. Try again.")
        else:
            return move


def main() -> None:
    """Run the Tic Tac Toe game."""
    board = [" "] * 9
    current_player = "X"

    print("Welcome to Tic Tac Toe!\n")
    while True:
        display_board(board)
        move = get_move(current_player, board)
        board[move] = current_player

        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            break
        if board_full(board):
            display_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
