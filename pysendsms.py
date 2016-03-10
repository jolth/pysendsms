#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import threading
from string import Template
import queue
import gammu
import json


# Configure Arguments:
aparser = argparse.ArgumentParser(prog='pysendsms', description='send SMS\
        message from csv file or string using one template.')
group = aparser.add_mutually_exclusive_group()
group.add_argument('-f', '--file',  help='file CSV to reading')
group.add_argument('-m', '--message', help='message to send')
group.add_argument('-t', '--template', help='template for the message. i.e:\
        \"Sr. [$name|${name}], your number account isn\'t active\"')
aparser.add_argument('-n', '--number', help='number to sms send')
aparser.add_argument('-i', '--identifiers', help='identifiers that is using\
        into templatesi. i.e: {"name":"jorge",...}')
args = aparser.parse_args()


class SendSMS(threading.Thread):
    def __init__(self):
        pass


def identifiers(i):
    """return one dictionary with all identifiers"""
    i = json.loads(i.replace('\'', '\"'))
    return i


if __name__ == '__main__': 
 
    fifo = queue.Queue()
    print(args) #debug Arg
