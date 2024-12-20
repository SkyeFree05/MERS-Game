import tkinter as tk
from tkinter import Canvas, Label, messagebox
from game_brain import QuizBrain
import os
import pygame


class QuizGame:
    def __init__(self, master):
        pygame.init() #Initialize Pygame before loading sounds
        self.master = master
        master.title("MERS Quiz Game")

        self.quiz_brain = QuizBrain()
        self.player_name = ""
        self.high_scores = []
        self.game_high_score_label = tk.Label(self.master, text="")
        self.difficulty = ""
        self.unlocked_levels = {"easy": True, "normal": False, "hard": False}

        # Load high scores
        self.load_high_scores()

        # Load sounds
        self.background_music = pygame.mixer.Sound(os.path.join("sounds", "background_music.mp3"))
        self.easy_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "sounds", "easy_sound.mp3"))
        self.normal_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "sounds", "normal_sound.mp3"))
        self.hard_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "sounds", "hard_sound.mp3"))
        self.enter_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "sounds", "enter_sound.mp3"))
        self.correct_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "sounds", "correct_sound.mp3"))
        self.incorrect_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "sounds", "incorrect_sound.mp3"))
        self.difficulty_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "sounds", "difficulty_sound.mp3"))
        self.game_over_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "sounds", "game_over_sound.mp3"))
        self.back_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "sounds", "back_sound.mp3"))
        self.try_again_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "sounds", "try_again_sound.mp3"))

        # Play background music
        self.background_music.play(-1)  # Play on loop

        #===================GUI===================#

        #===================Title Image===================#

        self.title_canvas = Canvas(master, width=800, height=400) #Adjusted width and height
        self.title_canvas.grid(row=0, column=1, pady=20, sticky="n")
        try:
            image_path = os.path.join(os.path.dirname(__file__),"sai.png") 
            image = tk.PhotoImage(file=image_path)
            self.title_canvas.create_image(400, 210, image=image) # Adjusted position for center
            self.title_canvas.image = image
            self.master.update() #Force update to show image

        except tk.TclError as e:
            messagebox.showerror("Error", f"Could not load image: {e}")
            

            #Hide the canvas when the question frame is shown

        #===================High Scores Display===================#
        self.high_score_label = tk.Label(master, text="High Scores:", font=("Times New Roman", 18))
        self.high_score_label.grid(row=0, column=1, sticky="ne", padx=10, pady=10)

        self.highscore_display = tk.Label(master, text="", font=("Gagalin", 14), wraplength=200, anchor="w", justify="left")
        self.highscore_display.grid(row=1, column=2, padx=10, pady=20, sticky="ne")
        self.update_high_scores()

       #===================Difficulty Buttons===================#
        self.difficulty_frame = tk.Frame(master)
        self.difficulty_frame.grid(row=1, column=1, pady=10, sticky="n") #Difficulty buttons below canvas

        self.easy_button = tk.Button(self.difficulty_frame, text="EASY", command=lambda: self.set_difficulty("easy"), width=15, font=("Times New Roman", 20), bg="#4CAF50", fg="white")
        self.easy_button.grid(row=0, column=0, padx=20, pady=5, sticky="ew")

        self.normal_button = tk.Button(self.difficulty_frame, text="NORMAL", command=lambda: self.set_difficulty("normal"), width=15, font=("Times New Roman", 20), bg="#008CBA", fg="white")
        self.normal_button.grid(row=1, column=0, padx=20, pady=5, sticky="ew")
        self.normal_button.config(state=tk.DISABLED)

        self.hard_button = tk.Button(self.difficulty_frame, text="DIFFICULT", command=lambda: self.set_difficulty("hard"), width=15, font=("Times New Roman", 20), bg="#f44336", fg="white")
        self.hard_button.grid(row=2, column=0, padx=20, pady=5, sticky="ew")
        self.hard_button.config(state=tk.DISABLED)

        #==================="About Us" Button===================#
        self.about_us_button = tk.Button(master, text="About Us", command=self.show_about_us, width=8, font=("Times New Roman", 16), bg="#007bff", fg="white", justify="right")
        self.about_us_button.grid(row=2, column=0, pady=20, sticky="e")  # Right-aligned in a separate column

        # Question Frame and Canvas
        self.question_frame = tk.Frame(master)
        self.question_frame.grid(row=1, column=1, pady=45, padx=20, sticky="nsew") #Centered and sticky
        self.question_canvas = Canvas(self.question_frame, bg="white", width=600, height=100, highlightthickness=2, highlightbackground="black") #Rectangle for questions
        self.question_canvas.pack(pady=10)
        self.question_label = tk.Label(self.question_frame, text="", font=("Arial", 20),anchor="center") #Centered text
        self.question_canvas.create_window(300, 60, window=self.question_label)
        self.question_frame.grid_remove()

        #Options Frame and Buttons

        self.options_frame = tk.Frame(self.question_frame)
        self.options_frame.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.options_frame, text="", command=lambda i=i: self.check_answer(i), width=25, font=("Arial", 16), bg="#e0e0e0")
            button.grid(row=i, column=0, pady=5, sticky="ew")
            self.option_buttons.append(button)

        self.score_lives_frame = tk.Frame(master)
        self.score_lives_frame.grid(row=3, column=1, sticky="n") #spans all columns
        self.score_lives_frame.grid_remove() # Hide the frame

        self.lives_label = tk.Label(self.score_lives_frame, text=f"Lives: {self.quiz_brain.lives}", font=("Arial", 18))
        self.lives_label.grid(row=3, column=0)

        self.score_label = tk.Label(self.score_lives_frame, text=f"Score: {self.quiz_brain.score}", font=("Arial", 18))
        self.score_label.grid(row=3, column=2, padx=20) #Moved to column 2 for better spacing

        # Name Entry Frame (adjust row)
        self.name_frame = tk.Frame(master)
        self.name_frame.grid(row=2, column=1, pady=10, sticky="n")
        self.name_frame.grid_remove()

        self.name_label = tk.Label(self.name_frame, text="Enter your name:", font=("Arial", 16))
        self.name_label.grid(row=3, column=0, padx=5)

        self.name_entry = tk.Entry(self.name_frame, width=20, font=("Arial", 16))
        self.name_entry.grid(row=3, column=1, padx=5)
        self.name_entry.bind("<Return>", lambda event: self.get_player_name())

        self.enter_name_button = tk.Button(self.name_frame, text="Enter", command=self.get_player_name, width=10, font=("Arial", 16), bg="#007bff", fg="white")
        self.enter_name_button.grid(row=3, column=2, padx=5)
        self.enter_name_button.bind("Button-1>", lambda event: self.enter_sound.play())


        # Show the canvas again when the game over is shown
        # Game Over Frame (adjust row)
        self.game_over_frame = tk.Frame(master)
        self.game_over_frame.grid(row=7, column=0, columnspan=3, pady=30)
        self.game_over_frame.grid_remove()
        self.title_canvas.grid() #Show the canvas

        self.game_over_label = tk.Label(self.game_over_frame, text="", font=("Arial", 20), wraplength=500, bg="#f0f0f0", borderwidth=2, relief="solid")
        self.game_over_label.grid(row=0, column=0, columnspan=2, pady=15)

        self.back_button = tk.Button(self.game_over_frame, text="Back to Menu", command=self.back_to_menu, width=15, font=("Arial", 16), bg="#007bff", fg="white")
        self.back_button.grid(row=1, column=0, padx=20)

        self.try_again_button = tk.Button(self.game_over_frame, text="Try Again", command=self.try_again, width=15, font=("Arial", 16), bg="#007bff", fg="white")
        self.try_again_button.grid(row=1, column=1, padx=20)

        self.disable_options()
        self.update_high_scores() 

    def load_high_scores(self):
        try:
            with open("high_scores.txt", "r") as f:
                for line in f:
                    name, score = line.strip().split(",")
                    self.high_scores.append((name, int(score)))
        except FileNotFoundError:
            pass

    def set_difficulty(self, difficulty):
        if self.unlocked_levels[difficulty]:
            self.background_music.stop()
            if difficulty == "easy":
                self.easy_sound.play(-1)
            elif difficulty == "normal":
                self.normal_sound.play(-1)
            elif difficulty == "hard":
                self.hard_sound.play(-1)

            self.difficulty_sound.play()  # Play sound when difficulty is selected
            self.difficulty = difficulty
            self.difficulty_frame.grid_remove()
            self.highscore_display.grid_remove()  # Hide high score
            self.name_frame.grid()  # Show the "Enter your name" frame
            self.update_high_scores()
            self.highscore_display.grid()
            self.name_entry.focus_set()  # Set focus to the name entry
        else:
            messagebox.showerror("Error", f"Level {difficulty} is locked!")

    def show_about_us(self):
        about_us_message = """About Us:

        Mers Quiz Game is a fun and engaging game designed to test your knowledge on a variety of topics. Whether you're a trivia buff or just looking for a quick brain teaser, Mers Quiz has something for everyone.

        We developed this game with the goal of creating a fun and interactive experience for players of all ages. Whether you're playing solo or challenging your friends, Mers Quiz offers a lighthearted way to learn and explore new things.

        The Name: Our name, Mers, is a simple yet memorable combination of the first letters from the creators' names: Mark Reinz, Eunelyn, Russel, and Syckey.

        So, put on your thinking cap, gather your friends, and get ready to test your wits with Mers Quiz!"""
        messagebox.showinfo("About Us", about_us_message)

    def get_player_name(self):
        self.player_name = self.name_entry.get()
        if self.player_name:
            self.name_frame.grid_remove()
            self.question_frame.grid()
            self.score_lives_frame.grid()
            self.start_quiz()
            self.update_high_scores()
        else:
            messagebox.showwarning("Warning", "Please enter your name.")

    def start_quiz(self):
        if self.difficulty:
            self.quiz_brain.start_quiz(self.difficulty)
            self.update_lives_label()
            self.update_score_label()
            self.title_canvas.grid_remove() 
            self.next_question()
            self.enable_options()
            self.about_us_button.grid_remove()
            self.highscore_display.grid()
            self.update_high_scores(show_top_1=True)
        else:
            messagebox.showerror("Error", "Please select a difficulty level.")

    def next_question(self):
        if self.quiz_brain.has_next_question():
            question_data = self.quiz_brain.get_next_question()
            self.question_label.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option, state=tk.NORMAL)
        else:
            self.game_over()

    def check_answer(self, option_index):
        is_correct = self.quiz_brain.check_answer(option_index)
        self.update_lives_label()
        self.update_score_label()
        if is_correct:
            self.correct_sound.play()
        else:
            self.incorrect_sound.play()
        if self.quiz_brain.lives <= 0 or not self.quiz_brain.has_next_question():
            self.game_over()
        else:
            self.next_question()

    def next_question(self):
        if self.quiz_brain.has_next_question():
            question_data = self.quiz_brain.get_next_question()
            self.question_label.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option, bg="#e0e0e0", state=tk.NORMAL) # Reset button colors
        else:
            self.game_over()


    def game_over(self):
        if self.difficulty == "easy":
            self.easy_sound.stop()
        elif self.difficulty == "normal":
            self.normal_sound.stop()
        elif self.difficulty == "hard":
            self.hard_sound.stop()
        self.game_over_sound.play() #Play game over sound
        self.question_frame.grid_remove()
        self.score_lives_frame.grid_remove()
        self.game_over_frame.grid()

        score = self.quiz_brain.score
        total_questions = len(self.quiz_brain.questions_list)
        message = f"Game Over!\nFinal Score: {score}/{total_questions}\nLives Remaining: {self.quiz_brain.lives}"

        if self.difficulty == "easy" and score >= 8:
            message += "\nCongratulations! You unlocked the Normal Level!"
            self.unlocked_levels["normal"] = True
        elif self.difficulty == "normal" and score >= 15:
            message += "\nCongratulations! You unlocked the Hard Level!"
            self.unlocked_levels["hard"] = True

        self.game_over_label.config(text=message)
        self.save_high_score()
        self.disable_options()
        self.title_canvas.grid() # Show the canvas again
        self.update_high_scores(show_top_3=True) #Update the high score display

    def back_to_menu(self):
        self.back_sound.play() #Play sound for back menu
        if self.difficulty == "easy":
            self.easy_sound.stop()
        elif self.difficulty == "normal":
            self.normal_sound.stop()
        elif self.difficulty == "hard":
            self.hard_sound.stop()
        self.background_music.play(-1)

        self.game_over_frame.grid_remove()
        self.difficulty_frame.grid()
        self.highscore_display.grid() #Show high scores again
        self.reset_game()
        self.update_button_states()
        self.title_canvas.grid() # Show the canvas again
        self.update_high_scores(show_top_3=True) #Update the high score display

    def update_button_states(self):
        self.normal_button.config(state=tk.NORMAL if self.unlocked_levels["normal"] else tk.DISABLED)
        self.hard_button.config(state=tk.NORMAL if self.unlocked_levels["hard"] else tk.DISABLED)

    def try_again(self):
        self.try_again_sound.play()
        if self.difficulty == "easy":
            self.easy_sound.stop()
        elif self.difficulty == "normal":
            self.normal_sound.stop()
        elif self.difficulty == "hard":
            self.hard_sound.stop()
        self.game_over_frame.grid_remove()
        self.reset_game()
        if self.difficulty:
            self.quiz_brain.start_quiz(self.difficulty)
            if self.difficulty == "easy":
                self.easy_sound.play(-1)
            elif self.difficulty == "normal":
                self.normal_sound.play(-1)
            elif self.difficulty == "hard":
                self.hard_sound.play(-1)
        

            # Show frames BEFORE calling next_question
            self.question_frame.grid()
            self.score_lives_frame.grid()
            self.title_canvas.grid_remove()
            self.next_question()
            self.enable_options()
            self.update_high_scores()
            self.update_lives_label()
            self.update_score_label()
            for button in  self.option_buttons:
                button.config(bg="#e0e0e0")
        else:
            self.difficulty_frame.grid()
            self.title_canvas.grid_remove()
            self.update_high_scores(show_top_3=True)


    def update_lives_label(self):
        self.lives_label.config(text=f"Lives: {self.quiz_brain.lives}")

    def update_score_label(self):
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")

    def update_high_scores(self, show_top_3=False):  
        top_scores = sorted(self.high_scores, key=lambda x: x[1], reverse=True)[:3] # Sort here to avoid redundant sorting
        top_scores = self.high_scores[:3] if show_top_3 else self.high_scores

        if show_top_3:
                unique_top_scores = [] #Initialize the list here
                last_score = -1
                for name, score in top_scores:
                    if score != last_score:
                        unique_top_scores.append(f"{name}: {score}")
                        last_score = score
                        highscore_text = "\n".join(unique_top_scores) if unique_top_scores else "No high scores yet!"
                        self.highscore_display.config(text=highscore_text)
        else:  
            self.highscore_display.config(text="\n".join([f"{name}: {score}" for name, score in self.high_scores]) or "No high scores yet!")

            #self.game_high_score_label = Label(root, text="Top Score: 0: 0")  # Ensure this is done in your _init_ method
            #self.game_high_score_label.pack()
            #self.highscore_display = Label(root, text="")
            #self.highscore_display.pack()


    def save_high_score(self):
        if self.player_name:
            self.high_scores.append((self.player_name, self.quiz_brain.score))
            self.high_scores.sort(key=lambda x: x[1], reverse=True)
            self.high_scores = self.high_scores[:5]
            with open("high_scores.txt", "w") as f:
                for name, score in self.high_scores:
                    f.write(f"{name},{score}\n")
            self.update_high_scores()

    def enable_options(self):
        for button in self.option_buttons:
            button.config(state=tk.NORMAL)

    def disable_options(self):
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)

    def reset_game(self):
        self.quiz_brain.reset()
        self.player_name = ""
        self.update_lives_label()
        self.update_score_label()
        self.disable_options()
        self.highscore_display.grid() #Show high scores on reset
        self.update_high_scores(show_top_3=True) #Update high score display for the menu
      


# Main application setup 
root = tk.Tk() 
root.grid_rowconfigure(0, weight=1) 
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1) 
root.grid_rowconfigure(3, weight=1) 
root.grid_columnconfigure(0, weight=1) 
root.grid_columnconfigure(1, weight=1) 
root.grid_columnconfigure(2, weight=1) 
game = QuizGame(root) 
root.mainloop()