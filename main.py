import tkinter as tk
import random

class FlashcardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Kwizlet")

        # Load the data from a file
        self.flashcards = []
        with open("flashcards.txt", "r", encoding="utf-8") as f:
            for line in f:
                word, translation = line.strip().split(",")
                self.flashcards.append({"word": word, "translation": translation})
              
        self.current_index = 0
        random.shuffle(self.flashcards)
        # Create the GUI
        self.word_label = tk.Label(self.master, text=self.flashcards[self.current_index]["word"], font=("TkDefaultFont", 40))
        self.word_label.pack(pady=10)

        self.translation_label = tk.Label(self.master, text="", font=("TkDefaultFont", 40))
        self.translation_label.pack(pady=10)

        self.show_translation_button = tk.Button(self.master, text="Show Translation", command=self.show_translation, font=("TkDefaultFont", 40))
        self.show_translation_button.pack(pady=10)

        self.next_button = tk.Button(self.master, text="Next", command=self.next, font=("TkDefaultFont", 40))
        self.next_button.pack(pady=10)

    def show_translation(self):
        self.translation_label.config(text=self.flashcards[self.current_index]["translation"])

    def next(self):
        self.current_index = (self.current_index + 1) % len(self.flashcards)
        self.word_label.config(text=self.flashcards[self.current_index]["word"])
        self.translation_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
