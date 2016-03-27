#!/usr/bin/env python
# Original source: http://www.blackcoder.info/c/cmschecker.txt
# Usage example: $ python cms-checker.py --addr 192.168.1.1

import urllib2
import argparse
import os
import sys

class neo:
	def cmsfinder(self):

		url = "http://api.hackertarget.com/reverseiplookup/?q="+args.addr
		rever = urllib2.Request(url)
		conn = urllib2.urlopen(rever).read()
		sp = conn.split("\n")

		for s in sp:
			CMS_URL = "http://"+s
			_Con = urllib2.Request(CMS_URL)
			_Data = urllib2.urlopen(_Con).read()
			
			if 'Joomla' in _Data:
				print "\t\t"+ s + '\t\033[1;34m --> Joomla\033[1;m'

				with open('Joomla.txt', 'a') as j:
					j.write(s+"\n")

			elif 'wordpress' in _Data:
				print "\t\t"+ s + '\t\033[1;38m --> WordPress\033[1;m'

				with open('Wordpress.txt', 'a') as w:
					w.write(s+"\n")

			elif 'Drupal' in _Data:
				print "\t\t"+ s + '\t\033[1;36m --> Drupal\033[1;m'

				with open('Drupal.txt', 'a') as D:
					D.write(s+"\n")

			elif 'vBulletin' in _Data:
				print "\t\t"+ s + '\t\033[1;38m --> vBulletin \033[1;m'
				with open('vBulletin.txt', 'a') as vB:
					vB.write(s+"\n")
			
			else:
				print "\t\t"+ s + '\t\033[1;37m --> No CMS \033[1;m'
				with open('normal_site.txt', 'a') as f:
					f.write(s+"\n")

	def __init__(self):
		if os.name == "nt":
			os.system('cls')
		else:
			os.system('clear')

		banner = """ \t\t\t\t
\t\t\t\t\033[1;31m		                                              
\t\t\t\t _____ _____ _____    _____ _       _         
\t\t\t\t|     |     |   __|  |   __|_|___ _| |___ ___ 
\t\t\t\t|   --| | | |__   |  |   __| |   | . | -_|  _|
\t\t\t\t|_____|_|_|_|_____|  |__|  |_|_|_|___|___|_|  
 \t\t\t\t                                            \033[1;m
                        \t\t\t\tCoded By Ne0-h4ck3r
		"""
		print banner
		print ""
		print "\t\t" + "-" * 100
		print ""

		if len(sys.argv) == 1:
			print ""
			print "\t\tHow To Use: python sitecheker.py --addr [ IP ]"
			print ""
			sys.exit(1)

black = argparse.ArgumentParser()
black.add_argument('--addr', help="Enter Your IP-ADDRESS: ")
args = black.parse_args()


if __name__ == "__main__":
	neo().cmsfinder()

