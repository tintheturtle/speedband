import os
import time
import subprocess


def main():
    address = 'google.com'

    ping_response = get_ping(address)

    total = 0
    if (ping_response):
        ping_response = ping_response[1:6]
        for response in ping_response:
            response_time = response[6].split('=')[1]
            total += float(response_time)
    return int(total/5)

def get_ping(address):
    response = ''
    try:
        response = subprocess.check_output(['ping', '-c', '5', address], universal_newlines=True)
        response = response.split("\n")
        for i in range(len(response)):
            response[i] = response[i].split(' ')
    except subprocess.CalledProcessError:
        response = None

    return response
