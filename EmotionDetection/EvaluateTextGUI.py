try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from math import log10
from WordFilter import WordFilter
from EvaluateText import evaluateWord
from EvaluateText import guessEmotion
from EmotionDetection import EvaluateText
from EmotionDetection import WordMap
import tkMessageBox


class EvalTextGUI():
    def __init__(self):
        main = tk.Tk()
        tk.Label(main, text="Text File:", font=(None, 15)).grid(row=0, pady=5)



        self.t = tk.StringVar()
        self.textFileInputStr = tk.Entry(main, textvariable=self.t, font=(None, 15))


        self.textFileInputStr.grid(row=0, column=1, sticky="W", pady=10)


        tk.Button(main,
                  text='Add File',
                  command=self.addFiles,fg='white',bg='blue',
                  font=(None, 15)).grid(row=2, column=1, rowspan=2, sticky="nsew", pady=9, padx=20)

        main.title("EVALUATE TEXT: GUI")
        main.grid_rowconfigure(0, weight=1, minsize=60)
        main.grid_columnconfigure(0, weight=2, minsize=150)
        main.grid_columnconfigure(1, weight=2, minsize=400)
        main.grid_rowconfigure(1, weight=1, minsize=30)
        main.grid_rowconfigure(2, weight=1, minsize=40)
        main.grid_rowconfigure(3, weight=1, minsize=40)

        tk.mainloop()

    def addFiles(self):

        try:
            print("Running Text Evaluation...\n")
            print(self.textFileInputStr)
            # tkMessageBox.showinfo("Running", "Loading input values into WordMap")
            with open("./data/" + self.textFileInputStr.get(), 'r') as textFile:

                    EvaluateText.evaluate(textFile)

        except IOError:
            print("File not found.\n")
            tkMessageBox.showerror("Error", "File not found")