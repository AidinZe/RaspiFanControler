# RaspiFanControler
automatic fan controler for raspberry pi devices
In addition to compiling the code in raspberry pi, you must also have hardware board. To do this, we need a low ohm fan and a transistor.

![img](https://github.com/AidinZe/RaspiFanControler/blob/master/raspi%20fan.jpg)

# Auto-run Script Setup

Now we need to tell the operating system to run the script for the Pi user. In the command prompt or in a terminal window type :

> sudo nano /etc/profile

Scroll to the bottom and add the following line :

> sudo python /home/pi/fan.py

where “/home/pi/fan.py” is the path to your script.

Type “Ctrl+X” to exit, then “Y” to save followed by “Enter” twice.
A Script Without End

You will only be returned to the command line when your script is complete. If your script contains an endless loop then you may want to use this line in the profile file instead :

> sudo python /home/pi/fan.py &

This will allow the script to run in the background but you will not see any text output from it.
Reboot and Test

To test if this has worked reboot your Pi using :

> sudo reboot

علاوه بر کامپایل کد در رسپبری پای باید برد سخت افزاری را نیز بسازید برای این کار نیاز به یک فن مقاومت کم اهم و یک ترانزیستور نیاز داریم 
