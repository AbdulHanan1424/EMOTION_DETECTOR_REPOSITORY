# -*- coding: UTF-8 -*-
# main.py
# Root file for EmotionDetection program.

# Prints out command line menu and handles user choices

from __future__ import print_function
from EmotionDetection import WordMap
from EmotionDetection import EvaluateText
from EmotionDetection import TrainingGUI,InformationGUI,GUI,TestingGUI,EvaluateTextGUI
import tkMessageBox,Tkconstants, tkFileDialog
import Tkinter as tk

try:
    input = raw_input
except NameError:
    pass

import sys

reload(sys)
sys.setdefaultencoding('utf8')



win = tk.Tk()

coolFrame = tk.Frame(win)
coolFrame.pack()

text = ""
values = ""
reset=""
# def printMenu():
#     print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,", "EmotionDetection", ",¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°\n")
#     print("1. Training")
#     print("2. Testing")
#     print("3. Evaluate Text")
#     print("4. GUI Evaluation")
#     print("5. Information")
#     print("6. Exit\n")
#     print(78 * "-", "\n")


# def main():
    # choice = True
    # while choice:
        # printMenu()
        # choice = input("Select option [1-6]: ")
      # print




def train():

    TrainingGUI.TrainGUI()




def test():
    TestingGUI.TestGUI()
    # text = input("Text file: ")
    # values = input("Value file: ")
    # print("")
    # print ("values file is " ,  "./data/" + values)
    # try:
    #     print("\nRunning text evaluation...\n")
    #     with open("./data/" + text, 'r') as textFile:
    #         print ("text found")
    #         with open("./data/" + values, 'r') as valueFile:
    #             print ("values found")
    #             EvaluateText.evaluate(textFile, valueFile)
    #
    # except IOError:
    #     print("File not found. Returning to main menu...\n")
    #     tkMessageBox.showerror("Error","File not found")


def evaluate():
    EvaluateTextGUI.EvalTextGUI()
    # text = input("Text file: ")
    # print("")
    #
    # try:
    #     print("Running text evaluation...\n")
    #     with open("./data/" + text, 'r') as textFile:
    #         EvaluateText.evaluate(textFile)
    #
    # except IOError:
    #     print("File not found. Returning to main menu...\n")
    #     tkMessageBox.showerror("Error", "File not found")


def gui():
    GUI.Evaluator()


def printInfo():
     InformationGUI.infoGUI()


def close():

    tkMessageBox.showinfo("Information", "Window Exiting")
    win.quit()


tk.Button(coolFrame,
                  text='Training',fg='white',bg='blue',
                  command=train,
                  font=(None, 15)).grid(row=0, column=3, stick="nsew", pady=(8, 2), padx=10)
tk.Button(coolFrame,
                  text='Testing',fg='white',bg='blue',command=test,
                  font=(None, 15)).grid(row=0, column=4, stick="nsew", pady=(8, 2), padx=10)

tk.Button(coolFrame,
                  text='Evaluate Text',fg='white',bg='blue',
                  command=evaluate,
                  font=(None, 15)).grid(row=1, column=3, stick="nsew", pady=(8, 2), padx=10)

tk.Button(coolFrame,
                  text='GUI Evaluation',fg='white',bg='blue',
                  command=gui,
                  font=(None, 15)).grid(row=1, column=4, stick="nsew", pady=(8, 2), padx=10)
tk.Button(coolFrame,
                  text='Information',fg='white',bg='blue',
                  command=printInfo,
                  font=(None, 15)).grid(row=2, column=3, stick="nsew", pady=(8, 2), padx=10)
tk.Button(coolFrame,
                  text='Exit',
                  command= close,fg='white',bg='blue',
                  font=(None, 15)).grid(row=2, column=4, stick="nsew", pady=(8, 2),padx=10)

win.title("EMOTION DETECTOR: GUI")
win.geometry("400x400")
win.resizable(0,0)
win.grid_rowconfigure(0, weight=1, minsize=60)
win.grid_columnconfigure(0, weight=2, minsize=150)
win.grid_columnconfigure(1, weight=2, minsize=400)
win.grid_rowconfigure(1, weight=1, minsize=30)
win.grid_rowconfigure(2, weight=1, minsize=40)
win.grid_rowconfigure(3, weight=1, minsize=40)

win.mainloop()

        # if choice == "1":
        #     train()
        # elif choice == "2":
        #     test()
        # elif choice == "3":
        #     evaluate()
        # elif choice == "4":
        #     gui()
        # elif choice == "5":
        #     printInfo()
        # elif choice == "6":
        #     print("Exiting....\n")
        #     choice = False
        # else:
        #     print("Invalid choice.")
        #     choice = True


# Training Program, builds map of words and emotion values from annotated corpus





