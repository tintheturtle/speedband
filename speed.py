import time
import psutil

def main():
    rates = calculate_rates()
    print('Returning rate here: ')
    return rates

def calculate_rates():
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
    
    weekSeconds: int = 604800

    while(True):

        current: int = int(time.perf_counter())

        if ((current % weekSeconds) == 30 and current != 0):
            return download_collection, upload_collection

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

        if dl > 0.1 or ul >= 0.1:
            time.sleep(0.25)

main()