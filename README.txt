5/13/2016
Project - Hangman Game
Brennan Wallace - bgw2119
Stanislav Peceny - skp2140
Everything has been implemented as provided in the project proposal.
The game is fully functional and graphically convenient to use for the user.
The graphical interface has been implemented using tkinter.

Resources Used:

http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html
http://effbot.org/tkinterbook
https://www.youtube.com/watch?v=O12aT42okYE&index=13&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d
Various stack overflow python posts for small python issues.
And of course class notes.

We started a new virtual enviorment after installing anaconda with:
    conda create --name vin python=3

And activated with:
    source activate vin

We found that we needed no pip installs.
Pip freeze did not contradict this as it returned no requirements.

Then we ran:
    python hangman.py

And the project ran correctly.
Following these steps should yield the same result for anyone else.
Also, the new virtual environment is probably not required.

Motivation for the project:

Brennan and I wanted to learn how to use the graphical interface offered by Python - tkinter.
Hence we decided to create a hangman game where knowledge of tkinter could be utilized.

Modules used (along with any relevant information about installing dependencies if necessary, i.e.if you didn't use pip)
No need to install anything.  We are using tkinter for the game to display window.

A rundown of how your program works, how you structured your code, any interesting design decisions you made:

At the end of the program we initialize a window and call a class which represents the hangman game created.
Consequently, the entire program is dependent on a reset function where everything is updated.

Problems/Obstacles:

We had difficulties including images in the tkinter window.
Furthermore, it was a challenge to update the pictures as the game progressed.
We inserted the pictures using a label and further created a helper function to help us reset the pictures.