# Dominae
Simple Bash based Discord.py bot

Q: What does it do?

A: Currently, it's running on my server. Users can run commands to trigger scripts on my linux box. Currently, commands include:

ssay: Convert some words into a big image

sfortune: Gives a fortune in the same format

sfull: takes a full screenshot of my system

swindow: takes a screenshot of my currently active window

sselect: gives me a rectangle selection tool and sends the screenshot that generates to the server

sweb: takes a 1920x1080 still from my webcam and posts it on the server

smov: records a 10 second clip from my webcam with audio, converts it to vp9 webm, and uploads it to the server


Q: Why would you do this?

A: boredom, and its kind of neat being a human zoo.

Q: Can I run this?

A: Should be able to. It's obviously only going to work on a linux system, and the only thing I've tested it on is antergos, but as long as you have the prereqs installed and your API key slotted in it *should* work fine.

Q: Prereqs?

A: Glad you asked.

-scrot

-ffmpeg

-fswebcam

-fortune

-ImageMagick (Convert)

-San-Francisco-Display-Light (Font. You can change it if you want in sfortune.sh and ssay.sh if you want )

-Python3 with Discord.py

Q: where should I put it?

A: just clone it into your home directory. Should work. 

`git clone https://github.com/Evshaddock/Dominae`

`python ~/.dominae/screengrab.py`
