# Dominae
Simple Bash based Discord.py bot

Q: What does it do?

A: Currently, it's running on my server. Users can run commands to trigger scripts on my linux box. Currently, commands include:

ssay: Convert some words into a big image

ssub: makes an image out of some text in a similar manner to a old anime sub. Will work on this later to add the ability to cusomize background images laters.

sfull: takes a full screenshot of my system

swindow: takes a screenshot of my currently active window

sselect: gives me a rectangle selection tool and sends the screenshot that generates to the server

sweb: takes a 1920x1080 still from my webcam and posts it on the server

smov: records a 10 second clip from my webcam with audio, converts it to vp9 webm, and uploads it to the server

svox: Automatically stitch together .wav files in the VOX folder by name and upload the combined file. Seen working here:
https://youtu.be/XMvf6feXLjI
`Note: They all have to be the same bitrate and use the same amount of channels to be used in the same sound composite.`

cls: Uploads a bunch of blank images to clear the chat window. I'd comment this out if you have some people who would spam it

screenfetch: just uploads a screenfetch (Specs) from the host PC.

Q: Why would you do this?

A: boredom, and its kind of neat being a human zoo.

Q: Can I run this?

A: Should be able to. It's obviously only going to work on a linux system, and the only thing I've tested it on is antergos, but as long as you have the prereqs installed and your API key slotted in it *should* work fine.

Q: Prereqs?

A: Glad you asked.

-screenfetch

-scrot

-ffmpeg

-fswebcam

-sox (Sound eXchange)

-ImageMagick (Convert)

-San-Francisco-Display-Light (Font. You can change it if you want in sfortune.sh and ssay.sh if you want )

-Python3 with Discord.py

Q: where should I put it?

A: just clone it into your home directory. Should work. 

`git clone https://github.com/Evshaddock/Dominae`

`python ~/.dominae/screengrab.py`
