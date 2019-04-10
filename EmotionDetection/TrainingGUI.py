try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import ttk
from ttk import Progressbar
from EmotionDetection import WordMap
import tkMessageBox,tkFileDialog,os

class TrainGUI():
    def __init__(self):
        main = tk.Tk(self)
        tk.Label(main, text="Text File:", font=(None, 15)).grid(row=0, pady=5)
        tk.Label(main, text="Values File:", font=(None, 15)).grid(row=1)

        self.v = tk.StringVar()
        self.t = tk.StringVar()
        self.textFileInputStr = tk.Entry(main, textvariable= self.t , font=(None, 15))
        self.textValuesFileInputStr = tk.Entry(main, textvariable=self.v, font=(None, 15))

        self.textFileInputStr.grid(row=0, column=1, sticky="W", pady=10)
        tk.Button(main,
                  text='Browse File',
                  command=self.selectFile, fg='white', bg='blue',
                  font=(None, 12)).grid(row=0, column=2, sticky="nsew", pady=9, padx=20)

        self.textValuesFileInputStr.grid(row=1, column=1, sticky="W")
        tk.Button(main,
                  text='Browse File',
                  command=self.selectValueFile, fg='white', bg='blue',
                  font=(None, 12)).grid(row=1, column=2,  sticky="nsew", pady=9, padx=20)

        tk.Button(main,
                  text='Add Files',
                  command=self.addFiles,fg='white',bg='blue',
                  font=(None, 15)).grid(row=2, column=1, rowspan=2, sticky="nsew", pady=9, padx=20)

        main.title("TRAINING: GUI")
        main.grid_rowconfigure(0, weight=1, minsize=60)
        main.grid_columnconfigure(0, weight=2, minsize=150)
        main.grid_columnconfigure(1, weight=2, minsize=400)
        main.grid_rowconfigure(1, weight=1, minsize=30)
        main.grid_rowconfigure(2, weight=1, minsize=40)
        main.grid_rowconfigure(3, weight=1, minsize=40)

        main.mainloop()

    def selectFile(self):
        try:

            file_path = tkFileDialog.askopenfilename()
            obj=os.path.basename(file_path)
            self.textFileInputStr.insert(0,obj)

        except IOError:
            print("File not found.\n")
            tkMessageBox.showerror("Error", "File not selected")

    def selectValueFile(self):
        try:

            file_path = tkFileDialog.askopenfilename()
            obj = os.path.basename(file_path)
            self.textValuesFileInputStr.insert(0, obj)

        except IOError:
            print("File not found.\n")
            tkMessageBox.showerror("Error", "File not selected")

    def addFiles(self):

        try:



            print("Loading input values into WordMap...\n")
            # tkMessageBox.showinfo("Running", "Loading input values into WordMap")
            with open("./data/" + self.textFileInputStr.get(), 'r') as textFile:
                with open("./data/" + self.textValuesFileInputStr.get(), 'r') as valueFile:
                  WordMap.buildWordMap("y", textFile, valueFile)
                  tkMessageBox.showinfo("Its Done", "Training Completed")



        except IOError:
            print("File not found.\n")
            tkMessageBox.showerror("Error", "File not found")

