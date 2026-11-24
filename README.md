# Sensor Data Analysis Tool

The program makes random sensor readings, shows some statistics and makes 2 graphs.

## How it works

When you start the program you choose:
- 1 - make new readings
- 2 - load readings from a csv file

For new readings the program asks for the sensor type, how many readings, the min value, the max value and the alert threshold. The readings are saved in readings.csv.

After that the program shows the mean, min, max, standard deviation and the readings that are above the threshold. Then it shows a line plot and a histogram.

## Install

```
pip install -r requirements.txt
```

## Run

```
python sensor_monitor.py
```

## Files

- sensor_monitor.py - the program
- requirements.txt - numpy and matplotlib
- readings.csv - example data
- line_plot.png and histogram.png - example graphs