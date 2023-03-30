import flask
import requests

app = flask.Flask(__name__)
host = 'http://0.0.0.0:3937/'

def request(path):
    if len(path) > 0 and path[0] == '/':
        path = path[1:]

    return requests.get(host+path)

@app.route('/')
def main():
    options = ['on', 'off', 'switch']
    if (chosen:=flask.request.args.get('option')) in options:
        request(chosen)
    return flask.render_template('index.html')

@app.route('/on')
def turn_on():
    print(request('/on'))
    return "<h1>Tha lamp</h1><p>Tha lamp is turned ON</p>"

@app.route('/off')
def turn_off():
    print(request('/off'))
    return "<h1>Tha lamp</h1><p>Tha lamp is turned OFF</p>"

@app.route('/switch')
def switch():
    output = request('/switch').text
    if output[-2] == 'n':
        return "<h1>Tha lamp</h1><p>Tha lamp has been switched ON</p>"
    elif output[-2] == 'f':
        return "<h1>Tha lamp</h1><p>Tha lamp has been switched OFF</p>"
    else:
        return "Funky Error Help"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6969, debug = True)
