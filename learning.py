import random
from tkinter import *


class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.minsize(width=800, height=500)
        master.title("Hangman Game")
        path = "words.txt"
        self.words = []
        with open(path) as f:
            lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            self.words.append(line)
        selection = random.randint(-1,len(self.words)-1)
        self.secret_word = list(self.words[selection])
        self.answer = ['_'] * len(self.secret_word)
        self.guess = ''
        self.num_guesses = 0
        self.num_wrong_guesses = 0

        self.message = "Guess a Letter"
        self.answer_display_string = "__"
        self.set_answer_display_string()

        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)
        self.figureImage1 = PhotoImage(file="1.gif")
        self.current_figure = self.figureImage1
        self.figure = Label(master,image=self.current_figure)

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.guess_button = Button(master, text="Guess Letter", command=self.guess_letter)
        self.reset_button = Button(master, text="Reset", command=self.reset, state=DISABLED)

        self.answer_display_string_text = StringVar()
        self.answer_display_string_text.set(self.answer_display_string)
        self.answer_display_string_label = Label(master, textvariable=self.answer_display_string_text)

        self.label.pack()
        self.entry.pack()
        self.guess_button.pack()
        self.reset_button.pack()
        self.answer_display_string_label.pack()
        self.figure.pack()

        # self.label.grid(row=0, column=0, columnspan=2)
        # self.entry.grid(row=2, column=0, columnspan=2)
        # self.guess_button.grid(row=3, column=0)
        # self.reset_button.grid(row=3, column=1)
        # self.answer_display_string_label.grid(row=1, column=0, columnspan=2)
        # self.figure.grid(row=4,column=0, columnspan=2)

    def set_image(self):
        file_string = str(self.num_wrong_guesses + 1) + ".gif"
        self.figureImage = PhotoImage(file=file_string)
        self.figure.configure(image = self.figureImage)

    def set_answer_display_string(self):
        self.answer_display_string = ""
        for c in self.answer:
            self.answer_display_string += c
            self.answer_display_string += ' '
        self.answer_display_string.rstrip()

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
                self.answer[i] = str(self.secret_word[i])
                atLeastOneMatch = True
            i += 1
        if not atLeastOneMatch:
            self.num_wrong_guesses += 1
        self.set_answer_display_string()
        if (self.secret_word == self.answer):  #win
            suffix = '' if self.num_guesses == 1 else 'es'
            self.message = "You guessed the word after %d guess%s." % (self.num_guesses, suffix)
            self.guess_button.configure(state=DISABLED)
            self.reset_button.configure(state=NORMAL)
        elif self.num_wrong_guesses > 3:       #lose
            suffix = '' if self.num_guesses == 1 else 'es'
            self.message = "You failed to guess the word after %d total guess%s and %d wrong guess%s." % (self.num_guesses, suffix, self.num_wrong_guesses, suffix)
            self.message += " The word was %s." % (''.join(self.secret_word))
            self.answer = []
            self.guess_button.configure(state=DISABLED)
            self.reset_button.configure(state=NORMAL)
        else:                                  #keep playing
            self.message = "Guess a letter from a to z"


        if self.guess is None:
            self.message = "Guess a letter from a to z"
        print("number of wrong guesses: " + str(self.num_wrong_guesses))
        #self.current_figure = PhotoImage(self.figureImage2)
        #self.figure.configure(image = self.figureImage2)
        self.answer_display_string_text.set(self.answer_display_string)
        self.entry.delete(0, END)
        self.set_image()
        self.label_text.set(self.message)

    def reset(self):
        selection = random.randint(-1,len(self.words)-1)
        self.secret_word = list(self.words[selection])
        self.answer = ['_'] * len(self.secret_word)
        self.set_answer_display_string()
        self.guess = ''
        self.num_guesses = 0
        self.num_wrong_guesses = 0
        self.entry.delete(0, END)
        self.guess = ''
        self.num_guesses = 0
        self.message = "Reset: Guess a Letter"
        self.label_text.set(self.message)
        self.answer_display_string_text.set(self.answer_display_string)
        self.guess_button.configure(state=NORMAL)
        self.reset_button.configure(state=DISABLED)

root = Tk()
my_gui = GuessingGame(root)
root.geometry("600x500")
root.resizable(width=False, height=False)
root.mainloop()