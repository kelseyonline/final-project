# BuffBuddy 
This is a basic workout tracker! Specifically, I made this to track my weight lifting because I was keeping it all in my notes app. 

### Function 
This app uses a form to collect data on your workout. You can choose a machine (based on the machines they have at PlanetFitness), number of reps, and weight. Datetime automatically logs the time. Upon submission, the data is entered into a CSV. The CSV data is dynamically shown on the history.html page, and stats are calculated and displayed on the stats.html page. 

### Required packages
This app uses the following: 
- From flask: Flask, render_template, request, redirect
- From datetime: date
- csv

### How to run 
I use Flask to run this program by inputting python app.py into the console (or pressing the run button in VSCode)

### Things I would like to add in another iteration of this: 
[] Make machine appear only after selecting muscle group 
[] Reformat date in table 
[] Create login and sessions 
[] Add animations
[] Add input warnings
[] Add "add another workout?" button upon form submission instead of going directly to history

### Font
OFL-1.1
Copyright 2011 The ABeeZee Project Authors (https://github.com/googlefonts/abeezee) with Reserved Font Name ABeeZee ABeeZee-Italic.ttf: Copyright 2011 The ABeeZee Project Authors (https://github.com/googlefonts/abeezee) with Reserved Font Name ABeeZee