import time
import psutil

def main():
    print("Hello world")

    weekSeconds: int = 604800
    daySeconds: int = 86400

# Calculate bandwidth speed
    # Initial time of function call
    t0 = time.time()

    # Initial values for upload and download
    ul: float = 0.00
    dl: float = 0.00

    upload = psutil.net_io_counters().bytes_sent
    download = psutil.net_io_counters().bytes_recv

    up_down = (upload, download)

    download_collection = []
    upload_collection = []

# Calculate bandwidth usage
    # Array for collecting daily usage times
    daily = []

    # Array for collecting average daily  usage times
    dailyAverage = []

    oldBandwidth = 0

# Calculate ping/latency

    while (True):

        current: int = int(time.perf_counter())
        if (current % weekSeconds == 0 and current != 0):
            return download_collection, upload_collection, dailyAverage

        # Bandwidth speed
        last_up_down = up_down

        upload = psutil.net_io_counters().bytes_sent
        download = psutil.net_io_counters().bytes_recv

        t1 = time.time()
        up_down = (upload, download)

        try:
            ul, dl  = [ (now - last) / (t1 - t0) / 1024 for now, last in zip(up_down, last_up_down)]
            t0 = time.time()
        except:
            pass

        if ul > 2000:
            upload_collection += [ul]
        if dl > 2000: 
            download_collection += [dl]
        
        if dl > 2000 or ul > 2000:
            print('UL: {:0.2f} kB/s \n'.format(ul)+'DL: {:0.2f} kB/s'.format(dl))
            print()

        # Usage 
        if ((current % daySeconds) == 0 and current != 0): 

            # Computer daily average
            averageValue = average(daily)
            if (averageValue != 0.0):
                dailyAverage += [averageValue]

            # Reset array for next day
            daily = []

        # Get network values from psutil
        newBandwidth = upload - download

        # Comparing oldBandwidth with newBandwidth
        if oldBandwidth:
            daily += [round(convert_to_gbit(newBandwidth - oldBandwidth), 4)]

        # Set new bandwidth
        oldBandwidth = newBandwidth

        # Continuing function every second instead of continuously
        if dl > 0.1 or ul >= 0.1:
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

main()