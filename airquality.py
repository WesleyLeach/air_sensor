#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author  : Wleach
Date    : September 2021
Purpose : Monitor Air quality from a SDS011 sensor

'''
import argparse
from datetime import datetime
import json
import logging
import serial, time


def main(parsed_args):
    '''
    Main Driver if called alone.
    '''
    # Note this should point to whichever serial connection exists
    # for your sensor
    ser = serial.Serial('/dev/ttyUSB0')
    output_file = "/var/log/air_quality.log"
    while True:
        data = [ser.read() for _ in range(10) ]
        pmtofive = int.from_bytes(b''.join(data[2:4]), byteorder='little') /10
        pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') /10
        output_dict = {
            'timestamp': datetime.now().isoformat(),
            'sensor_name': parsed_args.name,
            'sensor_location': parsed_args.location,
            'pm_2_5': pmtofive,
            'pm_ten': pmten
        }
        logging.debug(json.dumps(output_dict, indent=4))
        with open(output_file, 'a') as out_file:
            out_file.write(json.dumps(output_dict, indent=4))
        time.sleep(10)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        add_help=True,
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
    parser.add_argument(
        '--rate',
        action='store',
        help="Sample rate for sensor.",
        required=False,
        choices= [
          3,
          10,
          15,
          30,
          60,
          300,
          600,
        ]
    )
    parser.add_argument(
        '--location',
        action='store',
        help="Location meta-data for sensor",
        required=False,
        default="",
    )
    parser.add_argument(
        '--name',
        action='store',
        help="Name meta-data for sensor",
        required=False,
        default="",
    )
    args = parser.parse_args()
    logging.basicConfig(
        level=args.logging,
        datefmt='%H:%M:%S'
    )
    main(args)



