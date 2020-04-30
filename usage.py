import time
import psutil

def main():
    # Original value of bandwidth usage is 0
    oldBandwidth = 0

    # int for week in seconds and for day in seconds
    weekSeconds: int = 604800
    daySeconds: int = 86400

    # Array for collecting daily usage times
    daily = []

    # Array for collecting average daily  usage times
    dailyAverage = []
        

    while True:

        # int of current time since script started
        current: int = int(time.perf_counter())

        # Checks for if a week has passed
        if ((current % weekSeconds) == 30 and current != 0):            
            # Reset array for next week
            return dailyAverage


        if ((current % daySeconds) == 10 and current != 0): 

            # Computer daily average
            averageValue = average(daily)
            dailyAverage += [averageValue]

            # Reset array for next day
            daily = []

        # Get network values from psutil
        newBandwidth = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        # Comparing oldBandwidth with newBandwidth
        if oldBandwidth:
            daily += [round(convert_to_gbit(newBandwidth - oldBandwidth), 4)]

        # Set new bandwidth
        oldBandwidth = newBandwidth

        # Continuing function every second instead of continuously
        time.sleep(1)


# Getting average of day
def average(array):
    counter = 0
    for i in array:
        counter += i
    counter = counter / len(array)
    return counter


# Converting to gigabytes
def convert_to_gbit(value):
    return value/1024./1024./1024.*8

# Printing value
def send_stat(value):
    return print("%0.3f" % convert_to_gbit(value))