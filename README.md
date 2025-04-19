# TestData & Scripts
Solar Panel Graphing Scripts + Test Data and Graphs

## Test Data
CSV files containing measurements for all tests can be found in the TestData folder. Each folder also contains graphs for each test.

## How to Use Scripts
Once all required packages are installed run one of the following:
- autoPlot.py
- recovery.py
- interactive.py

#### autoPlot.py
Within a folder than contains CSV files, a graphs subfolder is created. Within the graphs folder, each CSV file creates a new subdirectory for that specific test which will hold the graphs. Up to seven graphs are created depending on which algorithm was run
- A path to a folder that holds <b>ONLY</b> CSV files is required
- A graphs subdirectory will be created to hold all of the SVG graphs that are created

#### recovery.py
Plots power vs time with irradiance from the specified csv file that is selected from the file picker. Graph can be adjusted interactively and points can be selected by right clicking or removed by left clicking

#### interactive.py
Plots one of the ten possible graphs from a csv file that is selected from the file picker. Graph can be adjusted interactively and points can be selected by right clicking or removed by left clicking. Two of the graphs are animated so it appears that the data is being plotted in real time.

---
##### Author: Kyle Rabbitt, Frank Parsons
##### Organization: MPPT MQP @ WPI
