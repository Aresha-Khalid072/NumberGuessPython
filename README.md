# Number Guessing Game (GUI)

A graphical number guessing game built with Python and Tkinter. The computer picks a random number between 1 and 100, and you try to guess it. After each guess you get a color-coded hint, and a range bar shows how much the possible range has narrowed.

The project separates the game logic (`GuessingGame`) from the interface (`GuessingApp`), following basic Object-Oriented Programming (OOP) principles.

## Features

- Random secret number between 1 and 100 in every game
- Color-coded hints: blue for "Too low!", red for "Too high!", green for "Correct!"
- Range label and green range bar that shrink as you narrow down the number
- Attempts counter
- Guess history list showing every guess and its result
- Input validation with error popups for:
  - Non-numeric input
  - Numbers outside 1 to 100
- Winning popup showing how many attempts you took
- **New Game** button to restart at any time
- Press **Enter** to submit a guess

## Requirements

- Python 3.6 or higher
- Tkinter (included with Python on Windows and macOS)
- No external libraries needed, only the built-in `random` and `tkinter` modules

On Linux, if Tkinter is missing:

```bash
sudo apt install python3-tk
```

## How to Run

1. Save the code as `NumberGuess.py`.
2. Open a terminal in the same folder.
3. Run:

```bash
python NumberGuess.py
```

On some systems, use `python3` instead of `python`.

## How to Play

1. Type a whole number between 1 and 100 in the entry box.
2. Click **Guess** or press Enter.
3. Read the hint and check the range bar to see where the number can still be.
4. Keep guessing until you find the number. A popup shows your attempt count.
5. Click **New Game** to play again.

## Project Structure

| Class | Responsibility |
|-------|----------------|
| `GuessingGame` | Game logic: picks the secret number, validates guesses, counts attempts, tracks the remaining range |
| `GuessingApp` | GUI: builds the window, reads input, calls the game logic, shows hints, history and errors |

Because the logic contains no GUI code, `GuessingGame` can be reused with a console version or any other interface.

## How It Works

- `random.randint(1, 100)` selects the secret number in `new_game()`.
- `guess()` raises a `ValueError` for out-of-range numbers, otherwise it returns `"low"`, `"high"` or `"correct"`.
- Each wrong guess updates `low` or `high`, so the range shrinks.
- `_draw_bar()` draws the range on a Tkinter `Canvas`.
- `try/except ValueError` in `make_guess()` catches invalid input and shows it in a `messagebox`.
- After a win, the entry box and Guess button are disabled until a new game starts.

## Possible Improvements

- Difficulty levels (different number ranges)
- Limit the number of attempts
- High score tracking (fewest attempts)
- Sound effects or animations
- Option to play multiple rounds with a scoreboard

## Author

Aresha Khalid
Python Development Intern, Arch Technologies