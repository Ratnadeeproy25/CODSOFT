import tkinter as tk
from tkinter import ttk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")

        self.user_score = 0
        self.computer_score = 0

        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=('Helvetica', 14))
        self.style.configure("TButton", font=('Helvetica', 12), padding=10)
        
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        title_label = ttk.Label(frame, text="Rock-Paper-Scissors", font=('Helvetica', 18, 'bold'))
        title_label.pack(pady=10)
        
        self.instruction_label = ttk.Label(frame, text="Choose Rock, Paper, or Scissors:")
        self.instruction_label.pack(pady=10)
        
        self.button_frame = ttk.Frame(frame)
        self.button_frame.pack(pady=10)
        
        self.rock_button = ttk.Button(self.button_frame, text="Rock", command=lambda: self.play('rock'))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = ttk.Button(self.button_frame, text="Paper", command=lambda: self.play('paper'))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = ttk.Button(self.button_frame, text="Scissors", command=lambda: self.play('scissors'))
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.result_label = ttk.Label(frame, text="", font=('Helvetica', 14, 'italic'))
        self.result_label.pack(pady=20)

        self.score_label = ttk.Label(frame, text="Score: You 0 - 0 Computer")
        self.score_label.pack(pady=10)

        self.play_again_button = ttk.Button(frame, text="Play Again", command=self.play_again)
        self.play_again_button.pack(pady=5)
        self.play_again_button.pack_forget()  # Hide the button initially

    def play(self, user_choice):
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        winner = self.determine_winner(user_choice, computer_choice)
        self.display_result(user_choice, computer_choice, winner)
        self.update_score(winner)
        self.update_score_label()
        self.show_play_again_button()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return 'user'
        else:
            return 'computer'

    def display_result(self, user_choice, computer_choice, winner):
        result = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n"
        if winner == 'tie':
            result += "It's a tie!"
        elif winner == 'user':
            result += "You win!"
        else:
            result += "You lose!"
        self.result_label.config(text=result)

    def update_score(self, winner):
        if winner == 'user':
            self.user_score += 1
        elif winner == 'computer':
            self.computer_score += 1

    def update_score_label(self):
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")

    def show_play_again_button(self):
        self.play_again_button.pack()

    def reset_game(self):
        self.result_label.config(text="")
        self.play_again_button.pack_forget()
        self.instruction_label.config(text="Choose Rock, Paper, or Scissors:")
        self.update_score_label()

    def play_again(self):
        self.user_score = 0
        self.computer_score = 0
        self.reset_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
