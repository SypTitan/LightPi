import flask
import gpiozero as gz
import time as t
import servolib as sl

app = flask.Flask(__name__)

acceptmotion = [True, True]

@app.route('/on')
def turn_on():
    source = flask.request.args.get('source')
    if source == 'motion' and acceptmotion[0] == False:
        return "Sorry, the motion sensor cannot turn on the lights right now"
    servo.max()
    return "Lights turned on!"

@app.route('/off')
def turn_off():
    source = flask.request.args.get('source')
    if source == 'motion' and acceptmotion[1] == False:
        return "Sorry, the motion sensor cannot turn off the lights right now"
    servo.min()
    return "Lights turned off!"

@app.route('/switch')
def switch():
    v = servo.getvalue()
    if v == servo.getmax():
        servo.min()
        return "Lights turned off!"
    else:
        servo.max()
        return "Lights turned on!"

@app.route('/value')
def getvalue():
    return f"<h1>{servo.getvalue()}</h1>"

@app.route('/config/motion')
def configmotion():
    output = ""
    on = flask.request.args.get('on')
    if on == "true":
        acceptmotion[0] = True
        output += "The motion sensor can turn the lamp on. "
    elif on == "false":
        acceptmotion[0] = False
        output += "The motion sensor can no longer turn the lamp on. "

    off = flask.request.args.get('off')
    if off == "true":
        acceptmotion[1] = True
        output += "The motion sensor can turn the lamp off. "
    elif off == "false":
        acceptmotion[1] = False
        output += "The motion sensor can no longer turn the lamp off. "

    return f"<h2>Configurated!</h2><p>{output}</p>"

@app.route('/end')
def stop():
    quit()
    return "Bye!"



if __name__=="__main__":
    servo = sl.Servo(-0.25, 0.45, False, 27, 0.5)
    
    app.run(host='0.0.0.0',port=3937,debug=False)
