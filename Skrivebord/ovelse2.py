from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import pigpio
from time import sleep

LED_ROD_GPIO_PIN = 17
LED_BLA_GPIO_PIN = 16
pi = pigpio.pi()
app = Flask(__name__)
socketio = SocketIO(app)
pi.set_PWM_range(LED_ROD_GPIO_PIN, 100)
pi.set_PWM_range(LED_BLA_GPIO_PIN, 100)
pi.set_PWM_frequency(LED_ROD_GPIO_PIN, 100000)
pi.set_PWM_frequency(LED_BLA_GPIO_PIN, 100000)
@socketio.on('skru_bla_browser')
def skrubl(data):
    lysstyrkebla = int(data['lysstyrkebla'])
    if lysstyrkebla < 0:
       lysstyrkebla = 0
    if lysstyrkebla > 77:
       lysstyrkebla = 77
    pi.set_PWM_dutycycle(LED_BLA_GPIO_PIN, lysstyrkebla)
@socketio.on('skru_rod_browser')
def skru(data):
    lysstyrke = int(data['lysstyrke'])
    if lysstyrke < 0:
       lysstyrke = 0
    if lysstyrke > 58:
       lysstyrke = 58
    pi.set_PWM_dutycycle(LED_ROD_GPIO_PIN, lysstyrke)

@app.route('/')
def index():
    return render_template('ovelse2.html')

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)
