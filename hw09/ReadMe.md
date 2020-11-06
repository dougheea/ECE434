# hw09 grading

| Points      | Description |
| ----------- | ----------- |
|  0 | Project Timeline - *mising*
| 10 | Logging to Sheets
|  3 | Logging to ThingSpeak - optional
|  2 | Extras
| 15 | **Total**

*My comments are in italics. --may*

### temp_logger.py
This file takes the temperature of the room from 2 different tmp101 sensors and logs them to a google sheet: https://docs.google.com/spreadsheets/d/1nytQJZmAPP3sAD1jyL4Ix__gswq_vsJ2V9dkHYUuOXI/edit#gid=0. The data is then plotted onto the graph in the google sheet. The credentials.json file is used to authenticate the user and allow them to edit the sheet. The images of the data and plot I tested with can be see in tempData.pdf.

### temp.py
This file takes the temperature from the 2 sensors and plots them on ThingSpeak. A setup files is used to set the temp sensors and to set the Write Key for ThingSpeak. An image of the data collected can be seen in ThingSpeakImage.pdf