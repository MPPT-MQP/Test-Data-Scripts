import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as Tk
from tkinter import filedialog
from datetime import datetime
from numpy.polynomial import Polynomial
import os

# File Picker
# Tk.Tk().withdraw() # prevents an empty tkinter window from appearing

# filepath = filedialog.askopenfilename()
# # print(filepath)

# fileName = os.path.basename(filepath)
# print(fileName)

####################################################
#    ADD YOUR PATH TO THE FOLDER WITH CSV FILES
####################################################
# path = "C:/Users/temp/Documents/WPI/MQP/TestData/TestGraphData"
print("============\nMQP GRAPHING: \nEntire folder will be read and ALL CSV files will be converted into graphs."
"\nGraphs will be placed in the graphs subdirectory in your specified path.\n\n")
path = input("Enter folder path to CSV files: ")

userInput = input("Is this path correct? (y/n): " + path + " ")
if userInput != 'y':
    print("Stopping Execution")
    quit()


filesToGraph = []
# return all files as a list
for fileName in os.listdir(path):
     # check the files which are end with specific extension
    if fileName.endswith(".csv"):
        # Save path of all CSV files
        filesToGraph.append(path + "/" + fileName)

resultsPath = path + "/Graphs/"
# Check if subdir exists, if not create it
if not os.path.exists(resultsPath): 
    # then create it. 
    os.makedirs(resultsPath)


for csvFile in filesToGraph:
    print("Creating graphs for: " + csvFile)
    df = pd.read_csv(csvFile, encoding='ISO-8859-1', sep=',', usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13])

    # Global Text size and font config
    plt.rc('font', size=20) #Set font size
    plt.rcParams["font.family"] = "Aptos" #Set font


    # Column format
    # Timestamp, PM1 (V), PM1(I), PM1(W), PM2 (V), PM2(I), PM2(W), PM3 (V), PM3(I), PM3(W), Temp (C), Light (W/m^2), Duty, Algorithm
    # plt.scatter(df.iloc[:, X], df.iloc[:, Y])


    """ Create Voltage vs current graph """
    x = df.iloc[:, 1] #X axis is col 1
    y = df.iloc[:, 2] #Y axis is col 2

    # Trendline?
    # z = np.polyfit(x, y, 2)
    # p = np.poly1d(z)
    # plt.scatter(x,y)
    # plt.plot(x, p(x), "g-")  # 'g-' is for a green solid line

    fig, ax = plt.subplots()
    # ax.plot(x,y, c="#AC2B37")
    ax.scatter(x,y, marker= "^", c="#AC2B37")
    fig.set_size_inches(12, 8, forward=True)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (A)")
    plt.title("Current vs Voltage")
    plt.grid(which='major', linestyle='-', linewidth=1, alpha=0.8)
    ax.minorticks_on()
    plt.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.8)
    ax.set_ylim([0, 2.5])
    ax.set_xlim([0, 25])

    SplitName = csvFile.split("__")
    SplitName = SplitName[1].split(".")
    SaveFileName = SplitName[0] + "- CvsV"

    fig.savefig(resultsPath + SaveFileName + '.svg', dpi=fig.dpi, bbox_inches='tight', pad_inches=0.5)



    """ Create power vs voltage graph """
    x = df.iloc[:, 1] #X axis is col 0
    y = df.iloc[:, 3] #Y axis is col 3

    # Trendline?
    # z = np.polyfit(x, y, 2)
    # p = np.poly1d(z)
    # plt.scatter(x,y)
    # plt.plot(x, p(x), "g-")  # 'g-' is for a green solid line

    fig, ax = plt.subplots()
    ax.scatter(x,y, marker= "^", c="#AC2B37")
    fig.set_size_inches(12, 8, forward=True)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Power (W)")
    plt.title("Power vs Voltage")
    plt.grid(which='major', linestyle='-', linewidth=1, alpha=0.8)
    ax.minorticks_on()
    plt.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.8)
    # ax.set_ylim([0, 30])

    SplitName = csvFile.split("__")
    SplitName = SplitName[1].split(".")
    SaveFileName = SplitName[0] + "- PvsV"

    fig.savefig(resultsPath + SaveFileName + '.svg', dpi=fig.dpi, bbox_inches='tight', pad_inches=0.5)



    """ Create power vs time graph """
    x = df.iloc[:, 0] #X axis is col 0
    y = df.iloc[:, 3] #Y axis is col 3

    # Trendline?
    # z = np.polyfit(x, y, 2)
    # p = np.poly1d(z)
    # plt.scatter(x,y)
    # plt.plot(x, p(x), "g-")  # 'g-' is for a green solid line

    fig, ax = plt.subplots()
    ax.plot(x,y, c="#AC2B37")
    ax.scatter(x,y, marker= "^", c="#AC2B37")
    fig.set_size_inches(12, 8, forward=True)
    plt.xlabel("Time (S)")
    plt.ylabel("Power (W)")
    plt.title("Power vs Time")
    plt.grid(which='major', linestyle='-', linewidth=1, alpha=0.8)
    ax.minorticks_on()
    plt.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.8)
    ax.set_ylim([0, 30])

    SplitName = csvFile.split("__")
    SplitName = SplitName[1].split(".")
    SaveFileName = SplitName[0] + "- PvsT"

    fig.savefig(resultsPath + SaveFileName + '.svg', dpi=fig.dpi, bbox_inches='tight', pad_inches=0.5)


    """ Create light vs time graph """
    x = df.iloc[:, 0] #X axis is col 0
    y = df.iloc[:, 11] #Y axis is col 3

    # Trendline?
    # z = np.polyfit(x, y, 2)
    # p = np.poly1d(z)
    # plt.scatter(x,y)
    # plt.plot(x, p(x), "g-")  # 'g-' is for a green solid line

    fig, ax = plt.subplots()
    ax.plot(x,y, c="#AC2B37")
    fig.set_size_inches(12, 8, forward=True)
    plt.xlabel("Time (S)")
    plt.ylabel("Light (W/m^2)")
    plt.title("Light vs Time")
    plt.grid(which='major', linestyle='-', linewidth=1, alpha=0.8)
    ax.minorticks_on()
    plt.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.8)
    # ax.set_ylim([0, 1300])

    SplitName = csvFile.split("__")
    SplitName = SplitName[1].split(".")
    SaveFileName = SplitName[0] + "- LightvsT"

    fig.savefig(resultsPath + SaveFileName + '.svg', dpi=fig.dpi, bbox_inches='tight', pad_inches=0.5)

print("Graphs Created")