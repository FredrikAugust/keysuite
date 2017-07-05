# Keysuite

## Requirements

- Raspberry Pi 3 Model B
- `raspivid` and `raspistill`, most likely shipped with your Rasbian distribution
- Python 3, pip (package manager for python)
- Raspberry Pi Camera v2

## Setup

- Use `raspi-config` to enable support for the camera
  - Should be found under interface options
  - Requires a reboot after changing
- Make sure all the packages are up-to-date by running `apt update` and `apt
upgrade`
- Save all the scripts and the python program from this repo to your machine
(preferrably somewhere that is in `PATH`)
- Make all of the scripts executable (`chmod +x <path to script>`)
- Install `flask` (python server library)
  - `pip install flask`

## Running

You can run the entire suite by running `key_suite` (presuming you put the file
in `PATH`). If you want to run an individual program you can use the
`livestream` and `image_server` scripts instead.

**PS**: If your program is in a folder that's not in path, you have to either
specify the path to the program (e.g. `./bin/<program>`) or add the folder to
path (`export PATH=$PATH:<insert absolute path to folder here>`; put this in
a startup script (e.g. `.bashrc`)).

## Stopping the program

**Killing the livestream**: `Control-C` when livestream is open

**Killing the webserver**: Either locate the PID using htop/top/ps or similar,
or use this _short_ command: `kill $(ps aux | grep "flask" | grep -oP "pi\s+\d+" | head -n 1)`.
