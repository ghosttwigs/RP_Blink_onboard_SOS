#This script blinks the onboard LED (GPIO pin 25) on a Raspberry Pi Pico RP2040.

import machine #Loads machine library, which allows us to control GPIO pins
import utime   #Loads the microtime library, which allows us to keep track of time

led_onboard = machine.Pin(25, machine.Pin.OUT) #Sets GPIO pin 25 as an output and assigns it to an object called "led_onboard"

while True:  #This creates a continous loop
  led_onboard.value(1)  #Sets the pin high, which turns the LED on
  utime.sleep(0.5)      #Waits half of second
  led_onboard.value(0)  #Sets the pin low, which turns the LED off
  utime.sleep(0.5)      #Waits half of second
  led_onboard.value(1)  #Sets the pin high, which turns the LED on
  utime.sleep(0.5)      #Waits half of second
  led_onboard.value(0)  #Sets the pin low, which turns the LED off
  utime.sleep(0.5)      #Waits half of second
  led_onboard.value(1)  #Sets the pin high, which turns the LED on
  utime.sleep(0.5)      #Waits half of second
  led_onboard.value(0)  #Sets the pin low, which turns the LED off
  
  utime.sleep(1)        #Waits one second before changing to next part
  
  led_onboard.value(1)  #Sets the pin high, which turns the LED on
  utime.sleep(1)        #Waits one second
  led_onboard.value(0)  #Sets the pin low, which turns the LED off
  utime.sleep(0.5)      #Waits half of second
  led_onboard.value(1)  #Sets the pin high, which turns the LED on
  utime.sleep(1)        #Waits one second
  led_onboard.value(0)  #Sets the pin low, which turns the LED off
  utime.sleep(0.5)      #Waits half of second
  led_onboard.value(1)  #Sets the pin high, which turns the LED on
  utime.sleep(1)        #Waits one second
  led_onboard.value(0)  #Sets the pin low, which turns the LED off
  
  utime.sleep(1)        #Waits one second before changing to next part
  
  led_onboard.value(1)  #Sets the pin high, which turns the LED on
  utime.sleep(0.5)      #Waits half of second
  led_onboard.value(0)  #Sets the pin low, which turns the LED off
  utime.sleep(0.5)      #Waits half of second
  led_onboard.value(1)  #Sets the pin high, which turns the LED on
  utime.sleep(0.5)      #Waits half of second
  led_onboard.value(0)  #Sets the pin low, which turns the LED off
  utime.sleep(0.5)      #Waits half of second
  led_onboard.value(1)  #Sets the pin high, which turns the LED on
  utime.sleep(0.5)      #Waits half of second
  led_onboard.value(0)  #Sets the pin low, which turns the LED off
  
  utime.sleep(5)        #Waits five seconds before repeating
