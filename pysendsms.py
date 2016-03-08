#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

# Configure Arguments:
aparser = argparse.ArgumentParser(prog='pysendsms', description='send SMS\
        message from csv file or string using one template.')
group = aparser.add_mutually_exclusive_group()
group.add_argument('-f', '--file',  help='file CSV to reading')
group.add_argument('-m', '--message', help='message to send')

aparser.add_argument(
        "-t", "--template", help="template for the message")
args = aparser.parse_args()

