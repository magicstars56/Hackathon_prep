Hackathon_prep
==============

This repository is meant for testing ideas, prototyping and otherwise preparing for hackathons.

#New Ideas

###Location based emergency service
Platforms: iOS, Android, Chrome, Raspberry Pi, Firebase/MongoDB, Facebook, Twitter


###Pi Security Camera
Platforms: Raspberry Pi, Firebase/MongoDB, AngularJS

Given that the state of consumer level security cameras is so bad right now, I think creating a cheap and somewhat robust solution could be a good use of our time. This hack would require a raspberry pi (with wifi) and a cheap usb webcam. The main focus of this hack will be to process incoming images from the camera and detect motion when the camera is armed. It will be challenging to do this on a raspberry pi, given the constraints on processor power. We can then grow this to output a video stream online, and then if possible, also include apps for iOS and Android.

###EL Jacket
Platforms: Arduino, Raspberry Pi, Spotify, SoundCloud, Twilio, Android, iOS, Firebase/MongoDB, JavaScript

Take a jacket or something, wire it up with lots of EL wire in different colors, and add music. Have a RPi (or Edison or some other powerful embedded solution) decoding a music source (YouTube, Spotify, SoundCloud, locally stored music - think Beats by ACM), doing a FFT on it to perform frequency analysis, and flash the EL wire according to the different frequencies like a VU meter. Music will be played back on a sufficiently loud speaker connected to the RPi, and people can vote on the next track to play via web interface or by sending a text to a Twilio-powered backend. Network connectivity provided by Wi-Fi or tethered smartphone.

This idea is currently reserved for Wildhacks


#Implemented Ideas

###Cellular Backend
Platforms: Twilio, Android, iOS, Raspberry Pi

**(Won Best Use of Twilio API at Boilermake) http://challengepost.com/software/cellularlock**

Using a cellular network as the backend of an app. This serves as a proof of concept for building connected digital systems without the need of a reliable internet connection. This is useful mainly becuase of the fact that many developing nations do not have extensive data networks, but do have extensive enough and reliable enough cellular networks to facilitate basic communicatio. This Cellular Backend can be used to help increase the utility of these cellular networks.



More ideas to be added soon (hopefully)



#Usage

Please create a top level folder for each idea, list the tools needed in this readme, and start testing.
