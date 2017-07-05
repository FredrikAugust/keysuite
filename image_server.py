#!/usr/bin/python3

from flask import Flask, send_file
import subprocess

app = Flask(__name__)

# This will make an external call to `raspistill` and then save the image
def take_picture():
  subprocess.call(["raspistill",
                   "-o", "/home/pi/Pictures/key-image.jpg", # output file
                   "-w", "1680", "-h", "800", # width/height
                   "-n", # no preview
                   "-t", "1"]) # take picture right away


# This is the main route, will create a subprocess that takes a picture, and
# then sends it back to the requester
@app.route("/")
def index():
  take_picture()
  return send_file("/home/pi/Pictures/key-image.jpg", mimetype="image/jpeg")
