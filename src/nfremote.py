#!/usr/bin/python
# encoding: utf-8
#
# Copyright © 2015 andreas.grill@gmail.com
#
# MIT License. See http://opensource.org/licenses/MIT
#
# Created on 2015-01-03
#

import subprocess
import sys
import re
from AppKit import NSScreen, NSWorkspace, NSRunningApplication
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID, kCGWindowListExcludeDesktopElements

referenceWidth = 1920
referenceHeight = 1080
reCliArgument = re.compile(r'^(?P<op>[a-z]):(?P<val>[0-9,]+)$')

def netflix_remote(commands):
	callcmds = ["./cliclick", "m:0,0", "w:1"]
	browserBounds = get_browser_bounds()

	print browserBounds
	lastCoords = (0,0)
	for cmd in commands:
		cmdargs = parse_cliclick_argument(cmd)

		if(len(cmdargs[1]) == 2):
			coords = translate_coordinates(browserBounds, int(cmdargs[1][0]), int(cmdargs[1][1]))
			relCoords = (coords[0] - lastCoords[0], coords[1] - lastCoords[1])
			callcmds.append("%s:%+d,%+d" % (cmdargs[0], relCoords[0], relCoords[1]))
			lastCoords = coords
		else:
			callcmds.append(cmd)

	print commands
	print callcmds
	subprocess.call(callcmds)


def parse_cliclick_argument(argument):
	match = reCliArgument.match(argument)
	if match:
		return (match.group('op'),match.group('val').split(','))
	return ('no-op', [])

def get_browser_bounds():
	runningApp = NSWorkspace.sharedWorkspace().frontmostApplication()
	runningAppPid = runningApp.processIdentifier()
	windows = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly | kCGWindowListExcludeDesktopElements, kCGNullWindowID)

	possibleWindows = []
	for wnd in windows:
		if wnd['kCGWindowOwnerPID'] == runningAppPid:
			possibleWindows.append(wnd)

	fallback = False
	if len(possibleWindows) == 0:
		# fallback mode
		fallback = True
	elif len(possibleWindows) == 1:
		window = possibleWindows[0]
	else:
		fallback = True
		for wnd in possibleWindows:
			#if 'netflix' in wnd['kCGWindowName'].lower():
			if int(wnd['kCGWindowLayer']) < 0 :
				window = wnd
				fallback = False
				break
		
	if fallback:
		# return fallback
		return dict(
			Height = NSScreen.mainScreen().frame().size.height,
			Width = NSScreen.mainScreen().frame().size.width,
			X = 0,
			Y = 0
		)
	else:
		return window['kCGWindowBounds']


def translate_coordinates(browserBounds, x, y):
	newX = float(browserBounds['Width']) / referenceWidth * x + browserBounds['X']
	newY = float(browserBounds['Height']) / referenceHeight * y + browserBounds['Y']
	return (int(round(newX)), int(round(newY)))

if len(sys.argv) > 1:
	netflix_remote(["m:100,100", "w:50"] + sys.argv[1:] + ["w:50", "m:0,300"])
