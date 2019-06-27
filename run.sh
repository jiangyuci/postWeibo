#!/bin/sh
killall Xvfb
Xvfb -ac :7 -screen 0 1280x1024x8 -extension RANDR -nolisten inet6 &
export  DISPLAY=:7
python3 YOUR_PATH_TO_THIS_FOLDER/postWeibo/main.py
killall Xvfb