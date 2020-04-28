import time
import psutil

def main():
    # Original value of bandwidth usage is 0
    oldBandwidth = 0

    # int for week in seconds
    weekSeconds: int = 604800
        
    while True:

        # int of current time since script started
        current: int = int(time.perf_counter())

        # Checks for if a week has passed
        if ((current % weekSeconds) == 0 and current != 0):
            print("True")

        # Get network values from psutil
        newBandwidth = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        # Comparing oldBandwidth with newBandwidth
        if oldBandwidth:
            send_stat(newBandwidth - oldBandwidth)

        # Set new bandwidth
        oldBandwidth = newBandwidth

        # Continuing function every second instead of continuously
        time.sleep(1)


# Converting to gigabytes
def convert_to_gbit(value):
    return value/1024./1024./1024.*8

# Printing value
def send_stat(value):
    return print("%0.3f" % convert_to_gbit(value))