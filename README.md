# Pi3TVClock
## What is Pi3TVClock
Pi3TVClock is a script base on Raspberry Pi3 with OSMC.
This script can automatic start TV by IR and automatic play video.
Using btn3stop.py with physical button can iterrupt Pi3TVClock.py.
## Previously Prepared
  * Have a Raspberry Pi3 and Install OS with OSMC.
  * Plugin IR receiver on Pi3 and use IR receiver to GET TV IR signal. \\
    After get TV IR signal, changing name to "Pi3TVClock" which in your lircd.conf.
  * Plugin IR transmitter and test it work.
  * Plugin a physical button and test it work. 
  * Use HDMI to connect Pi3 and TV.
## Installation
Installing request package
<pre>
sudo apt-get install -y gcc python python-pip git
sudo pip install RPi.GPIO
sudo pip install xbmc-client
</pre>

## Start script
###Start btn2stop to background:
<pre>sudo python btn2stop.py &</pre>

###Direct start Pi3TVClock.py
<pre>sudo python Pi3TVClock.py</pre>

###Using crontab to start Pi3TVClock.py
<pre>sudo crontab -e</pre>
Setting crontab
<pre>0 */1 * * * sudo python Pi3TVClock.py & > /dev/null 2>&1 </pre>

