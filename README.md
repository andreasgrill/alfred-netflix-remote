# NfRemote
Control Netflix with Alfred Remote
![NfRemote](./icon_256.png)

## About this Project
With this [Alfred][alf] workflow you are able to control Netflix in your browser from your mobile device running [Alfred Remote][alfremote].
This workflow uses hotkeys and mouse emulation to gain access to the Netflix Browser UI. The mouse emulation is executed by the awesome command line utility [Cliclick][cliclick].
The icons are from [ionicons][ionicons].

## How to get it working / Troubleshooting
Netflix Remote sends hotkeys as well as mouse events to your browser, running Netflix. It works best in __full screen__ mode, otherwise some commands that rely on mouse positioning might not work as expected.
Multiple monitor setups are supported.

## What it can do
 * Press play/pause
 * Set the volume to 100%, 80%, 60%
 * Increase/decrease the volume
 * Fast forward/rewind
 * Mute/unmute the volume
 * Skip forward
 * Press "continue playing"
 * Go back to browsing (Stop Netflix)
 * Play next

## Version History
 * 1.4 Fullscreen button added, better icons for VolUP/Down + BackToBrowsing
 * 1.3 Added Rewind/Forward and VolUp/VolDown, now uses hotkeys if possible
 * 1.2 Added window autodetection through Quartz
 * 1.1 Small bugfixing release
 * 1.0 Initial release

## Screenshot
![Screenshot](./screenshot.png)

[alf]:http://www.alfredapp.com/
[alfremote]:http://www.alfredapp.com/remote/
[cliclick]:http://www.bluem.net/en/mac/cliclick/
[ionicons]:https://github.com/driftyco/ionicons/