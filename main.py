import time
import psutil

import usage
import speed
import ping

# Command to install modules using pip -> python3 -m pip install psutil

def main():
    print("Hello world")

    usageReturn = usage.main()

    if (usageReturn):
        speedReturn = speed.calculate_rates()
        if (speedReturn):
            pingReturn = ping.main()

    # Call bandwidth function
    print(usageReturn)
    print()

    print(speedReturn)
    print()

    print(pingReturn)
    print()


main()