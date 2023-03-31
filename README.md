HOW TO USE
1. download at least servobackend.py and servolib.py
2a. download motion frontend.py for motion control
2b. download flask 2.py and the templates folder for internet control
3. use 'sudo pigpiod' to start the pin factory
4. run servobackend.py
5. run one or both the frontends

PREREQUISITES
* You need to have a servo motor taped to your light switch
* You need to have a PIR sensor connected to your pi trough GPIO pin 17
* You need to have the servo connected to your pi trough GPIO pin 27
* You need to have the following libraries installed:
  * Flask
  * GPIOzero
  * Time
  * Requests
