#importing libraries

from gpiozero import DistanceSensor
from gpiozero import LED



#setting up LED

led = LED(21)



#setting up distancesensor for autonomous drive

ultrasonic = DistanceSensor(echo =24, trigger =18, threshold_distance = 0.1)
ultrasonic.distance



#autonomous drive:
#If object is in range (10 cm) switch on the LED
#if object moves away, switch off the LED

while True:
    ultrasonic.wait_for_in_range()
    print"in range"
    led.on()
    ultrasonic.wait_for_out_of_range()
    print"out of range"
    led.off()
   
