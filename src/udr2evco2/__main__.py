"""UDR-2-EVCO2

Translates the data retrieved from the UDR model into the format accepted by the EVCO2 model.
"""

import logging
from os.path import isfile, isdir
from sys import argv
from argparse import (ArgumentParser, RawTextHelpFormatter,
                      ArgumentDefaultsHelpFormatter, ArgumentTypeError)

from .proc import run


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
    if isdir(path):
        return path
    raise ArgumentTypeError("Input directory does not exist")



def main():
    """Main method of UDR_EVCO2 connector
    """

    # command line argument parsing
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawDefaultsHelpFormatter)

    parser.add_argument('udr_output', type=strfile,
                        help='The path of the UDR output (xlxs)')
    parser.add_argument('vehicle_type_flag', type=int,
                        help='if vehicle type flag == 1 for fleet of electric motorbikes, '
                             'otherwise we have fleet of electric VANs')
    parser.add_argument('out_dir', type=strdir, help='The output directory')

    args = parser.parse_args(argv[1:])

    #print(args)
    #print(args.CPs, args.k)
    #res = start(args.ORDERS, args.CPs)
    res = run(args.udr_output, args.vehicle_type_flag, args.out_dir)
    print(res)


if __name__ == "__main__":
    main()
