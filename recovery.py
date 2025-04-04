import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as Tk
from tkinter import filedialog
from datetime import datetime
from numpy.polynomial import Polynomial
import os
from dataclasses import dataclass
import mplcursors



# File Picker
Tk.Tk().withdraw() # prevents an empty tkinter window from appearing

filepath = filedialog.askopenfilename()
# print(filepath)

fileName = os.path.basename(filepath)
print(fileName)
# ******************************
#       Enter CSV File Name
# ******************************
csvFile = filepath

print("Creating graphs for: " + csvFile)
df = pd.read_csv(csvFile, encoding='ISO-8859-1', sep=',', usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])

# Global Text size and font config
plt.rc('font', size=20) #Set font size
plt.rcParams["font.family"] = "Aptos" #Set font

# #Create folder for graph results
# CSVName = fileNameList[i].split(".csv")
# resultsPath = path + "/Graphs/" + CSVName[0] + "/"
# # Check if subdir exists, if not create it
# if not os.path.exists(resultsPath): 
#     # then create it. 
#     os.makedirs(resultsPath)

#Filter name for graphs
# GraphName = CSVName[0].split('__')
# GraphName = GraphName[1]

#Create array of time that is in seconds instead of ms
x = df.iloc[:, 1] #X axis is col 1 (elapsed time)
xArray = np.array(x)
TimeSec = xArray / 1000


# Column format (starts at 0)
# Timestamp, Elapsed Time, PM1 (V), PM1(I), PM1(W), PM2 (V), PM2(I), PM2(W), PM3 (V), PM3(I), PM3(W), Temp (C), Light (W/m^2), Duty, Algorithm
# plt.scatter(df.iloc[:, X], df.iloc[:, Y])

""" Create power vs time graph + light over time """
x = TimeSec
y = df.iloc[:, 4] #Y axis is col 4 (POWER)
z = df.iloc[:, 12] #Y2 axis, is col 12 (LIGHT)

fig, ax = plt.subplots()
ax2 = ax.twinx()
Power, = ax.plot(x,y, c="#AC2B37", label = "Power")
ax.scatter(x,y, marker= "^", c="#AC2B37")
Light, = ax2.plot(x,z, c="#003f5c", label = "Light")
fig.set_size_inches(12, 8, forward=True)
ax.set_xlabel("Time (S)")
ax.set_ylabel("Power (W)")
ax2.set_ylabel("Light (W/m^2)")
plt.title("Power and Light vs Time")
ax.grid(which='major', linestyle='-', linewidth=1, alpha=0.8)
ax.minorticks_on()
ax2.minorticks_on()
ax.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.8)
ax.set_ylim([0, 30])
ylim = ax2.get_ylim()
ylim = ylim[1] * (1.1)
ax2.set_ylim(bottom = 0, top = ylim)
# Function add a legend
plt.legend(handles = [Power, Light], loc="center left")
mplcursors.cursor(multiple=True)
plt.show()
# SaveFileName = GraphName + "- Power vs Time W-Light"

# fig.savefig(resultsPath + SaveFileName + '.svg', dpi=fig.dpi, bbox_inches='tight', pad_inches=0.5)
# plt.close()