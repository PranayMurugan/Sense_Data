# Collect the temperature amd humidity readings from sense hat and save it in a .csv file
# To start the program, press the forward button on the joystick and to stop the observation press the down button

from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from datetime import datetime
import time
import csv
from csv import writer
from gpiozero import CPUTemperature

sense = SenseHat()
sense.clear()

temp = []
hum = []
cpu = []
interval = []

logging = False

print("Press the UP button in joystick to start the program")

def get_sense_data():
    sense_data = []
    temp2 = round(sense.get_temperature(),3)            #rounds the temperature to the 3rd order
    hum2 = round(sense.get_humidity(),3)
    cpu1 = CPUTemperature()
    cpu2 = cpu1.temperature
    dt = datetime.now()
    dt2 = dt.strftime("%X")

    temp.append(temp2)
    sense_data.append(temp2)

    hum.append(hum2)
    sense_data.append(hum2)

    cpu.append(cpu2)
    sense_data.append(cpu2)

    interval.append(dt2)
    sense_data.append(dt2)

    return sense_data

def start_obs(event):
    global logging
    if event.action == ACTION_PRESSED:
        print("Collecting data... \nPress the DOWN arrow to stop reading")
        logging = True

def end_obs(event):
    global logging
    if event.action != ACTION_PRESSED:
        print("Saved data to data.csv... \nPress ctrl+c to exit from program...")
        logging = False
        #quit()

sense.stick.direction_up = start_obs
sense.stick.direction_down = end_obs


with open('data.csv', 'w', newline='') as f:
    data_writer = writer(f)
    data_writer.writerow(['temp','hum','cpu','interval'])
    while True:
        if logging:
            data = get_sense_data()
            time.sleep(10)              #takes reading every 10 seconds
            data_writer.writerow(data)
