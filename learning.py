import random
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Hangman Game")
        path = "words.txt"
        words = []
        with open(path) as f:
            lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            words.append(line)


        self.secret_word = "python"
        self.guess = None
        self.num_guesses = 0

        self.message = "Guess a Letter"
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.guess_button = Button(master, text="Guess Letter", command=self.guess_letter)
        self.reset_button = Button(master, text="Reset", command=self.reset, state=DISABLED)

        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.guess_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=1)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.guess = None
            return True
        try:
            if (len(new_text) == 1):
                return True
            return False;


        except ValueError:
            return False

    def guess_letter(self):
        self.num_guesses += 1

        if self.guess is None:
            self.message = "Guess a letter from a to z"

        elif self.guess == self.secret_number:
            suffix = '' if self.num_guesses == 1 else 'es'
            self.message = "You guessed the word after %d guess%s." % (self.num_guesses, suffix)
            self.guess_button.configure(state=DISABLED)
            self.reset_button.configure(state=NORMAL)

        self.message = "Wrong!!!"

        self.label_text.set(self.message)

    def reset(self):
        self.entry.delete(0, END)
        self.secret_word = "python"
        self.guess = 0
        self.num_guesses = 0

        self.message = "Reset: Guess a Letter"
        self.label_text.set(self.message)

        self.guess_button.configure(state=NORMAL)
        self.reset_button.configure(state=DISABLED)

root = Tk()
my_gui = GuessingGame(root)
root.mainloop()