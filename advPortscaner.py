#!/usr/bin/python3

from argparse import ArgumentParser
from threading import Thread
from time import time
import socket

open_ports = []

def prepare_args():
	"""prepare arguments 

	    return:
	    	args(argparse.Namespace)
	"""
	parser = ArgumentParser(description="Python Based Fast Port Scanner",usage="%(prog)s <IP>",epilog="Example- %(prog)s -s 20 -e 4600 -t 500 -V 192.168.0,2")
	parser.add_argument(metavar="IPv4",dest="ip",help="host to scan")
	parser.add_argument("-s","--start",dest="start",type=int,metavar="",help="starting port",default=1)
	parser.add_argument("-e","--end",dest="end",type=int,metavar="",help="ending port",default=65535)
	parser.add_argument("-t","--threads",dest="threads",metavar="",type=int,help="Threads",default=500)
	parser.add_argument("-V","--verbose",dest="verbose",action="store_true",help="Verbose output")
	parser.add_argument("-v","--version",action="version",version="%(prog)s 1.0",help="Display Version")
	args = parser.parse_args()
	return args

def prepare_ports(start:int,end:int):
	"""generator function for ports
        yield store the value in arry & doesn't need to return automaticly store the value in port
		arguments:
			start(int) - starting port
			end(int) - ending port
	"""
	for port in range(start,end+1):
		yield port

def scan_port():
	"""Scan Port
		"next" give u port one by one & remove from list
		"\r" for don't repeat out print new output
		"StopIteration" when u scan all port then u'll get error
	"""

	while True:
		try:
			s=socket.socket()
			s.settimeout(1)
			port = next(ports)
			s.connect((arguments.ip,port))
			open_ports.append(port)
			if arguments.verbose:
				print(f"\r{open_ports}",end="")
		except (ConnectionRefusedError,socket.timeout):
			continue
		except StopIteration:
			break


def prepare_threads(threads:int):
	"""Create,start,join threads
		" _ " for save variable
		"thread.join"= join next thread to 1st thread

		arguments:
			threads(int) - Number of threads to use
	"""
	thread_list=[]
	for _ in range(threads+1):
		thread_list.append(Thread(target=scan_port))

	for thread in thread_list:
		thread.start()

	for thread in thread_list:
		thread.join()

if __name__ == "__main__":
	arguments = prepare_args()
	ports = prepare_ports(arguments.start,arguments.end)
	start_time = time()
	prepare_threads(arguments.threads)
	end_time = time()
	if arguments.verbose:
		print()
	print(f"Open Ports Found-{open_ports}")
	print(f"Time Taken - {round(end_time-start_time,2)}")