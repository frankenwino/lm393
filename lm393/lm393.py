"""Main module."""
import RPi.GPIO as GPIO

def dark_or_light(sensor_readout):
    if sensor_readout == 0:
        return {'light': True}
    else:
        return {'light': False}

pin = 37 # Physical numbering
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN)

sensor_value = GPIO.input(pin)
GPIO.cleanup()

if __name__ == '__main__':
    from pprint import pprint
    result = dark_or_light(sensor_readout=sensor_value)
    pprint(result)
