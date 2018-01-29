#raspberry_py_automatic_fan_control
#programmer:Aidin_Zehtab
from subprocess import PIPE, Popen
import RPi.GPIO as GPIO
import time

def temp():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    stroutput=output.decode("utf-8")
    temp = stroutput.replace("temp=","").replace("'C\n","")
    return temp

max_temp = 40#You can change the temperature limit 
pin = 22#You can change the gpio pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.setwarnings(False)

while 1:
    real_temp = float(temp())
    print(real_temp)
    if real_temp >= max_temp:
        GPIO.output(pin, True)
    else:
        GPIO.output(pin, False)
    time.sleep(2)
   
