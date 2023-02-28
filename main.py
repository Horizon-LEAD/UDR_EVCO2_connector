
import sys
import os 
import argparse
from datetime import datetime

import logging
from logging.handlers import RotatingFileHandler
from os import environ
from os.path import isfile, join, abspath, exists
from sys import argv
from argparse import (ArgumentParser, RawTextHelpFormatter,
                      ArgumentDefaultsHelpFormatter, ArgumentTypeError)

from dotenv import dotenv_values

#from .envctl import parse_env_values
# from .proc import start
from .UDR_EVCO2 import udr_evco2_connector


LOG_FILE_MAX_BYTES = 50e6
LOG_MSG_FMT = "%(asctime)s %(levelname)-8s %(name)s \
%(filename)s#L%(lineno)d %(message)s"
LOG_DT_FMT = "%Y-%m-%d %H:%M:%S"

logger = logging.getLogger("udr_evco2_connector")


class RawDefaultsHelpFormatter(ArgumentDefaultsHelpFormatter, RawTextHelpFormatter):
    """Argparse formatter class"""


def strfile(path):
    """Argparse type checking method
    string path for file should exist"""
    if isfile(path):
        return path
    raise ArgumentTypeError("Input file does not exist")


def strdir(path):
    """Argparse type checking method
    string path for file should exist"""
    if exists(path):
        return path
    raise ArgumentTypeError("Input directory does not exist")



def main():
    """Main method of Parcel Generation Model.
    """

    # command line argument parsing
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawDefaultsHelpFormatter)

    parser.add_argument('UDR_output', type=strfile,
                        help='The path of the UDR output (xlxs)')


    parser.add_argument('vehicle_type_flag', type=int,
                        help='if vehicle type flag == 1 for fleet of electric motorbikes, otherwise we have fleet of electric VANs')

    args = parser.parse_args(argv[1:])

    #print(args)
    #print(args.CPs, args.k)
    #res = start(args.ORDERS, args.CPs)
    res = udr_evco2_connector(args.UDR_output,args.vehicle_type_flag)
    print(res)

if __name__ == "__main__":
    main()


