Hackathon_prep
==============

This repository is meant for testing ideas, prototyping and otherwise preparing for hackathons.

#Ideas:

1. Location based emergency service
  iOS, Android, Chrome, Raspberry Pi, Firebase, Facebook, Twitter,

2. Pi Security Camera
  Given that the state of consumer level security cameras is so bad right now, I think creating a cheap and somewhat robust solution could be a good use of our time. This hack would require a raspberry pi (with wifi) and a cheap usb webcam. The main focus of this hack will be to process incoming images from the camera and detect motion when the camera is armed. It will be challenging to do this on a raspberry pi, given the constraints on processor power. We can then grow this to output a video stream online, and then if possible, also include apps for iOS and Android.
  
3. Cellular Backend
  Using a cellular network as the backend of an app.

4. Music + EL Wire
  Take a jacket or something, wire it up with lots of EL wire in different colors, and add music. Have a RPi (or Edison or some other powerful embedded solution) decoding a music source (YouTube, Spotify, SoundCloud, locally stored music - think Beats by ACM), doing a FFT on it to perform frequency analysis, and flash the EL wire according to the different frequencies like a VU meter. Music will be played back on a sufficiently loud speaker connected to the RPi, and people can vote on the next track to play via web interface or by sending a text to a Twilio-powered backend. Network connectivity provided by Wi-Fi or tethered smartphone.

More ideas to be added soon (hopefully)



#Usage

Please create a top level folder for each idea, list the tools needed in this readme, and start testing.
