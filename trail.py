import tkinter as tk
from tkinter import filedialog
import os
root = tk.Tk()
root.withdraw()
a=filedialog.askopenfilename(parent=root,initialdir=os.getcwd(),title="Please select a file:")

