#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from netaddr import IPNetwork
from signal import signal, SIGINT

import argparse
import os
import subprocess
import sys

class IPListArgumentsParser(argparse.ArgumentParser):
	def error(self, message):
		sys.stderr.write("error: %s\n" % message)
		self.print_help()
		sys.exit(2)

def signal_handler(signal_received, frame):
	exit(0)

def main():
	signal(SIGINT, signal_handler)

	argp = IPListArgumentsParser()
	argp.add_argument('-n', '--network', help='Network range to display. Example: 10.100.5.0/24.', required=True)
	argp.add_argument('-d', '--delimiter', help='Delimiter between each IP address. Default is \\n.')
	argp.add_argument('-p', '--ping', help='Ping each IP and only display hosts that are up.', action='store_true')
	argp.add_argument('-q', '--quiet', help='Do not display details about the network.', action='store_true')
	args = argp.parse_args()

	if args.delimiter == '' or args.delimiter == '\n':
		args.delimiter = '\n'

	ip_list = IPNetwork(args.network)

	if args.quiet != True:
		print("Network:   %s" % args.network)
		print("Range:     %s - %s" % (ip_list[0], ip_list[ip_list.size-1]))
		print("Addresses: %s\n" % ip_list.size)

	if (args.ping == True):
		print("Checking for hosts that are up, this may take some time. Press Ctrl-C to cancel.\n")

	for ip in ip_list:
		octets = str(ip).split('.')
		if octets[3] > '0' and octets[3] < '255':
			if args.ping != True:
				print(ip, end=args.delimiter)
			else:
				try:
					subprocess.check_output(["ping", "-c1", "-t1", str(ip)])
					ip_up = True
				except subprocess.CalledProcessError:
					ip_up = False

				if ip_up == True:
					print(ip, end=args.delimiter)
	
	if args.delimiter != '\n':
		print("\n", end='')

if __name__ == '__main__': main()