import requests
import gpiozero as gz
import time as t

pir = gz.MotionSensor(4)

host = 'http://0.0.0.0:3937/'

def request(path):
    if len(path) > 0 and path[0] == '/':
        path = path[1:]

    return requests.get(host+path+"?source=motion")

value = False
past = int(t.time())


while True:
    current = int(t.time())
    if pir.value:
        if not value:
            print("Turning on!")
            request('on')
            value = True
            past = current
        else:
            print("Staying on!")
            past = current

    else:
        if value:
            if current - past > 20:
                print("Turning off!")
                request('off')
                value = False
            else:
                print("Waiting for input")
        else:
            print("Waiting for person")

    t.sleep(0.2)
