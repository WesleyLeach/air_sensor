#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author  : Wleach
Date    : September 2021
Purpose : Monitor Air quality from a SDS011 sensor

Docs:
    https://www.raspberrypi.org/blog/monitor-air-quality-with-a-raspberry-pi/
    https://www.amazon.com/SDS011-Quality-Detection-Conditioning-Monitor/dp/B07FSDMRR5
    https://aqicn.org/sensor/sds011/
'''
import argparse
from datetime import datetime
import json
import logging
import serial, time


def main():
    '''
    Main Driver if called alone.
    '''
    ser = serial.Serial('/dev/ttyUSB0')
    while True:
        data = [ser.read() for _ in range(10) ]
        #for _ in range(0,10):
        #    datum = ser.read()
        #    data.append(datum)
        pmtofive = int.from_bytes(b''.join(data[2:4]), byteorder='little') /10
        pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') /10
        output_dict = {
            'timestamp': datetime.now().isoformat(),
            'pm_2_5': pmtofive,
            'pm_ten': pmten
        }
        logging.debug(json.dumps(output_dict, indent=4))
        time.sleep(10)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        add_help=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        '-l',
        '--logging',
        action='store',
        required=False,
        default="INFO",
        choices= [
            "DEBUG",
            "WARN",
            "INFO",
            "CRITICAL",
            "ERROR"
        ]
    )
    args = parser.parse_args()
    logging.basicConfig(
        level=args.logging,
        datefmt='%H:%M:%S'
    )
    main()



