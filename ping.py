import os
import time
import subprocess

address = 'google.com'

def main():
    response = ''
    try:
        response = subprocess.check_output(['ping', '-c', '5', 'google.com'], universal_newlines=True)
        response = response.split("\n")
    except subprocess.CalledProcessError:
        response = None



    return response


values = main()
for i in values:
    print(i.split(" "))
