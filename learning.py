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
        selection = random.randint(-1,len(words)-1)
        self.secret_word = list(words[selection])
        self.answer = [' '] * len(self.secret_word)
        self.guess = ''
        self.num_guesses = 0
        self.num_wrong_guesses = 0

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
            if (len(new_text) == 1 and str.isalpha(new_text)):
                self.guess = new_text.lower()
                print("guess " + self.guess + " has been validated" )
                return True
            return False;

        except ValueError:
            return False

    def guess_letter(self):
        print("guess letter")
        print(str(self.guess))
        self.num_guesses += 1
        i = 0
        atLeastOneMatch = False
        while (i < len(self.secret_word)):
            if (self.secret_word[i] == self.guess):
                self.answer[i] == self.secret_word[i]
                atLeastOneMatch = True
            i += 1
        if (self.secret_word == self.answer):  #win
            suffix = '' if self.num_guesses == 1 else 'es'
            self.message = "You guessed the word after %d guess%s." % (self.num_guesses, suffix)
            self.guess_button.configure(state=DISABLED)
            self.reset_button.configure(state=NORMAL)
        elif self.num_wrong_guesses > 5:       #lose
            suffix = '' if self.num_guesses == 1 else 'es'
            self.message = "You failed to guess the word after %d total guess%s and %d wrong guess%s." % (self.num_guesses, suffix, self.num_wrong_guesses)
            self.message += "\nThe word was %s." % (self.secret_word.toString())
            self.guess_button.configure(state=DISABLED)
            self.reset_button.configure(state=NORMAL)
        else:                                  #keep playing
            self.message = "Guess a letter from a to z"
            if not atLeastOneMatch:
                self.num_wrong_guesses += 1
            self.num_guesses += 1

        if self.guess is None:
            self.message = "Guess a letter from a to z"

        self.label_text.set(self.message)

    def reset(self):
        self.entry.delete(0, END)
        self.secret_word = "python"
        self.guess = ''
        self.num_guesses = 0

        self.message = "Reset: Guess a Letter"
        self.label_text.set(self.message)

        self.guess_button.configure(state=NORMAL)
        self.reset_button.configure(state=DISABLED)

root = Tk()
my_gui = GuessingGame(root)
root.mainloop()