import schedule
import time
import pigpio
#from machine import PWM
#rød
GPIO_pin = 17
#blå
LED_BLA_GPIO_PIN = 16
pi = pigpio.pi()
pi.set_PWM_range(GPIO_pin, 100)
pi.set_PWM_range(LED_BLA_GPIO_PIN, 100)
pi.set_PWM_frequency(GPIO_pin, 100000)
pi.set_PWM_frequency(LED_BLA_GPIO_PIN, 100000)

class lightsch:
    def __init__(self, start_time, stop_time, GPIO_pin):
        self.start_time = start_time
        self.stop_time = stop_time
        self.duty = None
        self.GPIO_pin = GPIO_pin
        self.pi = pigpio.pi()
        self.pi.set_PWM_range(self.GPIO_pin, 100)
    def init_schedule(self):
        schedule.every().day.at(self.start_time).do(self.on)
        schedule.every().day.at(self.stop_time).do(self.off)
    def on(self):
        self.pi.set_PWM_dutycycle(self.GPIO_pin, 50)
    def off(self):
        self.pi.set_pwm_dutycycle(self.GPIO_pin, 0)
    def slow(self):
        self.pi.set_PWM_dutycycle(self.GPIO_pin, 0)
        for i in range(1,50):
            self.pi.set_PWM(dutycycle(self.GPIO_pin, i))

if __name__ == "__main__":
    lamp = lightsch("15:54", "15:55", GPIO_pin)
    lamp.init_schedule()
    while True:
        schedule.run_pending()
        time.sleep(1)
