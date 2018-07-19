#!/bin/bash
ffmpeg -f alsa -i pulse -i /dev/video0 -to 00:00:10 -c:v libvpx -b:v 6M -c:a libvorbis ~/.dominae/smov.webm -y -loglevel panic