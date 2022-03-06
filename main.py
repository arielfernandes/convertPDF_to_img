#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
from convert_controller import ConvertFile as conv


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(dest='command')
    parser.add_argument('-f', '--file', type=str, help="The filename",
                        required=True)
#     parser.add_argument('-t', '--type', type=str,
#                         help="Pass type jpg jpeg png", required=True)
    parser.add_argument(
        '-b', '--begin', type=int, help="Initial page", default=0)
    parser.add_argument(
        '-e', '--end', type=int, help="Final page", default=0)
    args = parser.parse_args()
    if args.command == 'convert':
        print('File:', args.file,
              #               '\ntype:', args.type,
              '\nbegin:', args.begin,
              '\nfinal:', args.end)
    c = conv(args.file, args.begin, args.end)
    c.convert_pdf()

    return 0


if __name__ == '__main__':
    sys.exit(main())
