import gpiozero as gz
import time as t


class Servo():
    def __init__(self, base: float = -0.1, delta: float = 0.6, reverse: bool = False, pin: int = 27, timeout: float = 0.5):
        global servo, servodelta, servobase

        self.pinfac = gz.pins.pigpio.PiGPIOFactory(host='127.0.0.1')

        self.servo = gz.Servo(pin, pin_factory=self.pinfac, initial_value = base)
        self.servobase = base
        self.servodelta = delta
        self.reverse = reverse
        self.lastvalue = self.servobase

        self.timeout = timeout

        t.sleep(timeout)
        self.value = None

    def __del__(self):
        self.servo.close()

    def set(self, value):
        self.servo.value = value
        t.sleep(self.timeout)
        self.servo.value = None
        return value

    def min(self):
        self.servo.value = self.getmin()
        self.lastvalue = self.getmin()
        t.sleep(self.timeout)
        self.servo.value = None
        return self.getmin()

    def max(self):
        self.servo.value = self.getmax()
        self.lastvalue = self.getmax()
        t.sleep(self.timeout)
        self.servo.value = None
        return self.getmax()

    def reset(self):
        self.servo.value = self.servobase
        self.lastvalue = self.servobase
        t.sleep(self.timeout)
        self.servo.value = None
        return self.servobase

    def getvalue(self):
        return round(self.lastvalue, 1)

    def getmax(self):
        if self.reverse:
            return round(self.servobase - self.servodelta, 1)
        return round(self.servobase + self.servodelta, 1)

    def getmin(self):
        if self.reverse:
            return round(self.servobase + self.servodelta, 1)
        return round(self.servobase - self.servodelta, 1)

if __name__ == "__main__":
    servo = Servo(-0.25, 0.45, False, 27, 0.5)
    
    while 1:
        x = input()
        servo.min()
        x = input()
        servo.max()
