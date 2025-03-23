import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as Tk
from tkinter import filedialog

# File Picker
Tk.Tk().withdraw() # prevents an empty tkinter window from appearing


filepath = filedialog.askopenfilename()
print(filepath)


# filename = input('Please enter filename: ')
df = pd.read_csv(filepath, encoding='ISO-8859-1', sep=',', usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13])
print('File read, available columns to plot (Starts at 1): ')
print(df.columns)
x_data = int(input('Enter column number for x-axis data: '))
x_label = input('Enter x-axis label: ')
y_data = int(input('Enter column number for y-axis data: '))
y_label = input('Enter y-axis label: ')
plt.scatter(df.iloc[:, x_data-1], df.iloc[:, y_data-1])
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.show()
