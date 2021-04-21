# for Akuji project
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.font as tkFont
import time as tm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

class App:
    def __init__(self, root):
        # setting title
        root.title("Show me what you got")
        # setting window size
        width = 1000
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
    

        '''self.my_window = tk.Tk(root)
        self.my_window.title('Current Time')
        ft = tkFont.Font(family='Times', size=10)
        self.current_time=tm.strftime('%H: %M: %S')
        self.clock_lable=tk.Label(my_window,font='ariel 80',bg='blue',fg='red',text=current_time)
        self.clock_lable.grid(row=0,column=0)'''







if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='python.png'))
    root.mainloop()


    #my_window.mainloop()