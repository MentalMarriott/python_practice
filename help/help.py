#!/usr/bin/env python

import sys			# <-- these are used to make comments 

def main(args):
    print args
    print "Hello World"		# the print outputs the text or variable to the console

if __name__ == '__main__': 	#is called on start
    main(sys.argv)		#calls main with arguments with those passed into it
