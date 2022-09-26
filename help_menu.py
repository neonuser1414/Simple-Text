from tkinter import *
from tkinter.messagebox import *
import sys


class Help():
    def about(root):
        showinfo(title="About", message="Simple Text editor. \n This program has been created on Python \n Version 1.0")
    def GitHub(root):
        showinfo(title="GitHub", message="GitHub page of Simple Text: \n https://bit.ly/3DUF2NK")


def main(root, text, menubar):

    help = Help()

    helpMenu = Menu(menubar)
    helpMenu.add_command(label="About", command=help.about)
    helpMenu.add_command(label="GitHub", command=help.GitHub)
    menubar.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    print("Please run 'main.py'")
