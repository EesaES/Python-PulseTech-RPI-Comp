import time
import drivers
import requests
from gpiozero import Buzzer
from gpiozero import Button
from gpiozero import LED
from time import sleep
from random import uniform
from os import _exit
from datetime import datetime
from max30105 import MAX30105, HeartRate

display = drivers.Lcd()
buzzer = Buzzer(26)


with open("hr.txt", "w") as file:
        file.write(str("Heartrate"))
        
max30105 = MAX30105()
max30105.setup(leds_enable=2)

max30105.set_led_pulse_amplitude(1, 0.2)
max30105.set_led_pulse_amplitude(2, 12.5)
max30105.set_led_pulse_amplitude(3, 0)

max30105.set_slot_mode(1, 'red')
max30105.set_slot_mode(2, 'ir')
max30105.set_slot_mode(3, 'off')
max30105.set_slot_mode(4, 'off')

def display_heartrate(beat, bpm, avg_bpm):
    print("{} BPM: {:.0f}  AVG: {:.0f}".format("<3" if beat else "  ",
          bpm, avg_bpm))
    bpm = round(bpm,1)
    mystatus = "Norm"
    if bpm < 60:
        mystatus = "Too low "
        print("Too Low")
    elif 60 <= bpm <= 100:
        mystatus = ""
        print("Normal")
    else:
        mystatus = "Too High"
        print("Too High")
    
    display.lcd_display_string(str(bpm), 2)
    #display.lcd_display_string(mystatus, 3)
    
    
    with open("hr.txt", "a") as file:        
        file.write(str("\n"))
        file.write(str(bpm))
        
        
         
        

     
  
button = Button(5)

def upload():
    url = '##Your website link here##'
    files = {'file': open('hr.txt', 'r')}

    r = requests.post(url, files=files)
    print(r.text)
    print("##and here##/upload/static/uploads/hr.txt")

def pressed(button):
    if button.pin.number == 5:
        print("Button Pressed")
        upload()
    else:
        print("No Button")
    
button.when_pressed = pressed

hr = HeartRate(max30105)

delay = 5

print("Starting readings in {} seconds...\n".format(delay))
time.sleep(delay)
display.lcd_display_string(str(datetime.now().strftime("Gauntlet       %H:%M")), 1)

try:
    hr.on_beat(display_heartrate, average_over=4)
except KeyboardInterrupt:
    pass


