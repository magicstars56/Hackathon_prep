Hackathon_prep
==============

This repository is meant for testing ideas, prototyping and otherwise preparing for hackathons.

#New Ideas

###Location based emergency service
Technologies: iOS, Android, Chrome, Raspberry Pi, Firebase/MongoDB, Facebook, Twitter


###Pi Security Camera
Technologies: Raspberry Pi, Firebase/MongoDB, AngularJS

Given that the state of consumer level security cameras is so bad right now, I think creating a cheap and somewhat robust solution could be a good use of our time. This hack would require a raspberry pi (with wifi) and a cheap usb webcam. The main focus of this hack will be to process incoming images from the camera and detect motion when the camera is armed. It will be challenging to do this on a raspberry pi, given the constraints on processor power. We can then grow this to output a video stream online, and then if possible, also include apps for iOS and Android.

###EL Jacket
Technologies: Arduino, Raspberry Pi, Spotify, SoundCloud, Twilio, Android, iOS, Firebase/MongoDB, JavaScript

Take a jacket or something, wire it up with lots of EL wire in different colors, and add music. Have a RPi (or Edison or some other powerful embedded solution) decoding a music source (YouTube, Spotify, SoundCloud, locally stored music - think Beats by ACM), doing a FFT on it to perform frequency analysis, and flash the EL wire according to the different frequencies like a VU meter. Music will be played back on a sufficiently loud speaker connected to the RPi, and people can vote on the next track to play via web interface or by sending a text to a Twilio-powered backend. Network connectivity provided by Wi-Fi or tethered smartphone.

This idea is currently reserved for Wildhacks

###L4D2 Virtual Reality System
Technologies: Arduino, Intel Edison, Raspberry Pi, SourceMod (SourcePawn), Myo, Oculus Rift, Wii remotes, Wiigee-C++, flex sensors

Take a Nerf gun, rewire its electronics, and connect it to a microcontroller for trigger/reload control. Dual Myos for accelerometer/gyroscope data to determine arm position, angle, and movement for gestures like melee shove, ADS (aim down sights), and throwing objects. Use flex sensors on left hand for additional precision - point to vocalize 'look!', reach out and grab to interact with items, etc. Possible ammo/health counter. Walking can be emulated with 2 Wiimotes strapped to legs, a dance pad, or some other method. Use keybinds to translate from gestures to inputs. Haptic feedback vest with 48 PWM-drivable vibration motors controlled via RPi and LED drivers for feedback when player gets hit, with RGB LED lighting for health visualization (ie. lower brightness as user takes damage, flash all red when player goes down, etc.) To retrieve game data like ammo/health/hit position, write a SourceMod plugin that listens to events and sends data to a client (in this case, the RPi) via sockets which will process the data. Aiming system still unknown, but you can strap a Wiimote to the gun barrel and use a sensor bar to position track the gun.

Idea currently reserved for a 'big' hackathon (MHacks V), haptic feedback vest might be done separately and incorporated into the overall idea later

#Implemented Ideas

###Cellular Backend
Technologies: Twilio, Android, iOS, Raspberry Pi

**(Won Best Use of Twilio API at Boilermake) http://challengepost.com/software/cellularlock**

Using a cellular network as the backend of an app. This serves as a proof of concept for building connected digital systems without the need of a reliable internet connection. This is useful mainly becuase of the fact that many developing nations do not have extensive data networks, but do have extensive enough and reliable enough cellular networks to facilitate basic communicatio. This Cellular Backend can be used to help increase the utility of these cellular networks.



More ideas to be added soon (hopefully)



#Usage

Please create a top level folder for each idea, list the tools needed in this readme, and start testing.
