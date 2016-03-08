# Pi3TVAlarm


## What is Pi3TVAlarm
Pi3TVAlarm is a script base on Raspberry Pi3 with OSMC.
This script can automatic start TV by IR and automatic play video.
Using btn3stop.py with physical button can iterrupt Pi3TVAlarm.py.


## Previously Prepared
  * Have a Raspberry Pi3 and Install OS with OSMC.
  * Plugin IR receiver on Pi3 and use IR receiver to GET TV IR signal.
    After get TV IR signal, changing name to "Pi3TVAlarm" which in your lircd.conf.
  * Plugin IR transmitter and test it work.
  * Plugin a physical button and test it work. 
  * Use HDMI to connect Pi3 and TV.


## Installation
Install request package
<pre>
sudo apt-get install -y gcc python python-pip git
sudo pip install RPi.GPIO
sudo pip install xbmc-client
</pre>

Install Pi3TVClock
<pre>git clone https://github.com/kigipaul/Pi3TVAlarm.git</pre>


## Start script
###Start btn2stop to background:
<pre>
cd Pi3TVClock
sudo python btn2stop.py &
</pre>

###Direct start Pi3TVAlarm.py
<pre>
cd Pi3TVAlarm
sudo python Pi3TVAlarm.py
</pre>

###Using crontab to start Pi3TVAlarm.py
<pre>sudo crontab -e</pre>
Setting crontab
<pre>0 */1 * * * cd Pi3TVAlarm && sudo python Pi3TVAlarm.py & > /dev/null 2>&1 </pre>

