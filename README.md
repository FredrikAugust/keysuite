# Keysuite

## Requirements

- Raspberry Pi 3 Model B
- `raspivid` and `raspistill`, most likely shipped with your Rasbian distribution
- Python, pip (package manager for python)
- Raspberry Pi Camera v2
- NPN Resistor (I used 2N 2222)
- 1k ohm resistor
- Cables
- Soldering iron
- Wire- cutter/stripper

## Setup

- Use `raspi-config` to enable support for the camera
  - Should be found under interface options
  - Requires a reboot after changing
- Make sure all the packages are up-to-date by running `apt update` and `apt
upgrade`
- Save all of the scripts to `~/bin` (you can change this, but then you will have to change the paths in `key_suite`)
- Make all of the scripts executable (`chmod +x <path to script>`)
- Install `flask` (python server library)
  - `pip install flask`
- Set up the wiring [as following](http://i.imgur.com/ACVbinT.png)

## Running

You can run the entire suite by running `~/bin/key_suite` (presuming you put the file
in `~/bin`). If you want to run an individual program you can use the
`livestream` and `image_server` scripts instead.

PS: If you add the `bin` dir to `PATH` you don't have to prefix the program with the path.

## Stopping the program

**Killing the livestream**: `Control-c` when livestream is open

**Killing the webserver**: Either locate the PID using htop/top/ps or similar,
or use this _short_ command: `kill $(ps aux | grep "flask" | grep -oP "pi\s+\d+" | head -n 1)`.
