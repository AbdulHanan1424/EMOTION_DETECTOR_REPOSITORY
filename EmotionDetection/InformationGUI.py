try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from math import log10
from WordFilter import WordFilter
from EvaluateText import evaluateWord
from EvaluateText import guessEmotion
from EmotionDetection import WordMap
import tkMessageBox

# def printInfo():

#     print("EmotionDetection v1, sentiment analysis system operating off a multinomial")
#     print("Naive Bayes classififer. There are 13 possible labels that text can be")
#     print("labelled as, the emotions are :empty, sadness, enthusiasm, neutral, worry,")
#     print("surprise, love, fun, hate, happiness, boredom, relief and anger.\n")
#     print("1. Training      - Generates a WordMap using a text file and emotion value file.")
#     print("                   A word map is required for both testing and evaluation.\n")
#     print("2. Testing       - Run the system and test its accuracy by supplying correct ")
#     print("                   emotion values. Also produces reports and confusion plot\n")
#     print("3. Evaluate Text - Run the system without given values. Used to evaluate input ")
#     print("                   file that has not been pre-labelled.")
#     print(78 * "-", "\n")
#     input("Press enter to return to menu...\n")

class infoGUI():
    def __init__(self):
        main = tk.Tk()
        tk.Label(main, text="EmotionDetection, sentiment analysis system operating off a multinomial \nNaive Bayes classififer. There are 13 possible labels that text can\nbe labelled as, the emotions are :empty, sadness, enthusiasm,\nneutral, worry,surprise, love, fun, hate, happiness, boredom,\nrelief and anger.").grid(row=0)
        tk.Label(main,text="1. Training      - Generates a WordMap using a text file and emotion value file.\nA word map is required for both testing and evaluation.").grid(row=1)
        tk.Label(main,text="2. Testing       - Run system and test's accuracy by supplying correct emotion\nvalues. Also produces reports and confusion plot").grid(row=2)
        tk.Label(main,text="3. Evaluate Text - Run system without given values. Used to evaluate input file\nthat has not been pre-labelled.").grid(row=3)


        main.title("INFORMATION: GUI")
        main.resizable(0, 0)
        main.grid_rowconfigure(0, weight=1, minsize=60)
        main.grid_columnconfigure(0, weight=2, minsize=150)
        main.grid_columnconfigure(1, weight=2, minsize=400)
        main.grid_rowconfigure(1, weight=1, minsize=30)
        main.grid_rowconfigure(2, weight=1, minsize=40)
        main.grid_rowconfigure(3, weight=1, minsize=40)

        tk.mainloop()



