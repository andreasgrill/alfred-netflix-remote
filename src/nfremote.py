#!/usr/bin/python
# encoding: utf-8
#
# Copyright © 2015 andreas.grill@gmail.com
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2015-01-03
#

import subprocess
import sys
import re
from AppKit import NSScreen

widthFactor = float(NSScreen.mainScreen().frame().size.width) / 1920
heightFactor = float(NSScreen.mainScreen().frame().size.height) / 1080
reCliArgument = re.compile(r'^(?P<op>[a-z]):(?P<val>[0-9,]+)$')

def netflix_remote(commands):
	callcmds = ["./cliclick"]

	for cmd in commands:
		cmdargs = parse_cliclick_argument(cmd)

		if(len(cmdargs[1]) == 2):
			coords = translate_coordinates(int(cmdargs[1][0]), int(cmdargs[1][1]))
			callcmds.append("%s:%d,%d" % (cmdargs[0], coords[0], coords[1]))
		else:
			callcmds.append(cmd)

	subprocess.call(callcmds)


def parse_cliclick_argument(argument):
	match = reCliArgument.match(argument)
	if match:
		return (match.group('op'),match.group('val').split(','))
	return ('no-op', [])

def translate_coordinates(x, y):
	return (int(round(widthFactor * x)), int(round(heightFactor * y)))

if len(sys.argv) > 1:
	netflix_remote(["m:100,100", "w:50"] + sys.argv[1:] + ["w:50", "m:0,300"])
