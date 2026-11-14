import random
import tkinter as tk
from tkinter import messagebox


class GuessingGame:
    """Game logic: no GUI code here."""
    def __init__(self):
        self.new_game()

    def new_game(self):
        self.secret = random.randint(1, 100)
        self.attempts = 0
        self.low = 1
        self.high = 100

    def guess(self, number):
        """Returns 'low', 'high' or 'correct'."""
        if not 1 <= number <= 100:
            raise ValueError("Out of range! Choose between 1 and 100.")
        self.attempts += 1
        if number < self.secret:
            self.low = max(self.low, number + 1)
            return "low"
        if number > self.secret:
            self.high = min(self.high, number - 1)
            return "high"
        return "correct"


class GuessingApp:
    """Graphical interface for the guessing game."""
    BG = "#0f172a"
    CARD = "#1e293b"
    TEXT = "#e2e8f0"
    MUTED = "#94a3b8"
    GREEN = "#22c55e"
    RED = "#ef4444"
    BLUE = "#3b82f6"
    YELLOW = "#facc15"
    BAR_W = 340

    def __init__(self, root, game):
        self.root = root
        self.game = game
        root.title("Number Guessing Game")
        root.geometry("420x600")
        root.configure(bg=self.BG)
        root.resizable(False, False)
        self._build_ui()
        self._reset_ui()

    def _build_ui(self):
        tk.Label(self.root, text="GUESS THE NUMBER", font=("Helvetica", 20, "bold"),
                 bg=self.BG, fg=self.TEXT).pack(pady=(20, 2))
        tk.Label(self.root, text="I'm thinking of a number between 1 and 100",
                 font=("Helvetica", 10), bg=self.BG, fg=self.MUTED).pack()

        # Hint card
        card = tk.Frame(self.root, bg=self.CARD)
        card.pack(padx=30, pady=15, fill="x")
        self.hint_label = tk.Label(card, text="", font=("Helvetica", 18, "bold"),
                                   bg=self.CARD, fg=self.YELLOW, height=2)
        self.hint_label.pack(pady=(10, 0))
        self.range_label = tk.Label(card, text="", font=("Helvetica", 11),
                                    bg=self.CARD, fg=self.MUTED)
        self.range_label.pack()

        # Range bar: shows how far the possible range has narrowed
        self.canvas = tk.Canvas(card, width=self.BAR_W, height=18, bg=self.CARD,
                                highlightthickness=0)
        self.canvas.pack(pady=(8, 5))
        self.attempts_label = tk.Label(card, text="", font=("Helvetica", 11, "bold"),
                                       bg=self.CARD, fg=self.TEXT)
        self.attempts_label.pack(pady=(0, 12))

        # Entry
        self.entry = tk.Entry(self.root, font=("Helvetica", 18), justify="center",
                              width=10, bg=self.CARD, fg=self.TEXT,
                              insertbackground=self.TEXT, relief="flat")
        self.entry.pack(ipady=6)
        self.entry.bind("<Return>", lambda e: self.make_guess())

        # Buttons
        btn_frame = tk.Frame(self.root, bg=self.BG)
        btn_frame.pack(pady=15)
        self.guess_btn = self._button(btn_frame, "Guess", self.BLUE, self.make_guess)
        self.guess_btn.grid(row=0, column=0, padx=6)
        self._button(btn_frame, "New Game", self.GREEN, self.new_game).grid(row=0, column=1, padx=6)

        # History
        tk.Label(self.root, text="Your Guesses", font=("Helvetica", 11, "bold"),
                 bg=self.BG, fg=self.TEXT).pack(pady=(5, 2))
        self.history = tk.Listbox(self.root, height=8, bg=self.CARD, fg=self.TEXT,
                                  font=("Courier", 11), relief="flat", highlightthickness=0)
        self.history.pack(padx=30, fill="x")

    def _button(self, parent, text, color, command):
        return tk.Button(parent, text=text, command=command, bg=color, fg="white",
                         font=("Helvetica", 12, "bold"), width=10, relief="flat",
                         activebackground=color, cursor="hand2")

    def _draw_bar(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 5, self.BAR_W, 13, fill="#334155", outline="")
        x1 = (self.game.low - 1) / 100 * self.BAR_W
        x2 = self.game.high / 100 * self.BAR_W
        self.canvas.create_rectangle(x1, 3, x2, 15, fill=self.GREEN, outline="")

    def _update_info(self):
        self.range_label.config(text=f"Number is between {self.game.low} and {self.game.high}")
        self.attempts_label.config(text=f"Attempts: {self.game.attempts}")
        self._draw_bar()

    def _reset_ui(self):
        self.hint_label.config(text="Make your first guess!", fg=self.YELLOW)
        self.history.delete(0, tk.END)
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.guess_btn.config(state="normal")
        self._update_info()
        self.entry.focus()

    def new_game(self):
        self.game.new_game()
        self._reset_ui()

    def make_guess(self):
        try:
            number = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid whole number.")
            return
        try:
            result = self.game.guess(number)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        self.entry.delete(0, tk.END)
        if result == "low":
            self.hint_label.config(text="Too low! Try again.", fg=self.BLUE)
            self.history.insert(0, f"{number:>3}  ->  Too low")
        elif result == "high":
            self.hint_label.config(text="Too high! Try again.", fg=self.RED)
            self.history.insert(0, f"{number:>3}  ->  Too high")
        else:
            self.hint_label.config(text="Correct!", fg=self.GREEN)
            self.history.insert(0, f"{number:>3}  ->  Correct!")
            self.entry.config(state="disabled")
            self.guess_btn.config(state="disabled")
            self._update_info()
            messagebox.showinfo("You won!",
                                f"You guessed it in {self.game.attempts} attempts.")
            return
        self._update_info()


if __name__ == "__main__":
    root = tk.Tk()
    GuessingApp(root, GuessingGame())
    root.mainloop()