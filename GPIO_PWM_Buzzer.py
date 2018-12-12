#########################################################################
# Date: 2018/09/07
# file name: GPIO_PWM_Buzzer_Example.py
# Purpose: this code has been generated for control Buzzer Module
# if program is run then buzzer will make sound!
#########################################################################

# coding=utf-8
"""
Buzzer 를 제어하기 위해 RPi.GPIO 모듈을 GPIO로 import 합니다.
sleep 함수를 사용하기 위해서 time 모듈을 import 합니다.
"""
import time
import RPi.GPIO as GPIO

class Buzzer:
    def __init__(self, buzzer_pin):
        
        # Raspberry Pi의 핀 번호를 의미합니다.
        self.buzzer_pin = buzzer_pin
        self.time = time.time()
        # Raspberry Pi의 핀 순서를 사용하도록 설정합니다.
        GPIO.setmode(GPIO.BOARD)

        """
        음계별 표준 주파수
        [ 도, 레, 미, 파, 솔, 라, 시, 도]
        """
        self.scale = [261.6, 293.6, 329.6, 349.2, 391.9, 440.0, 493.8, 523.2]
        self.sound = [self.scale[5], self.scale[2]]
        self.current_sound = 0

        """
        buzzer_pin 을 GPIO 출력으로 설정합니다. 이를 통해 led_pin으로
        True 혹은 False를 쓸 수 있게 됩니다.
        """
        GPIO.setup(buzzer_pin, GPIO.OUT)
        self.buzzer = GPIO.PWM(buzzer_pin, 50)

    def beep(self):
        try:
            self.buzzer.start(10)     # start the PWM on 5% duty cycle
            self.buzzer.ChangeFrequency(self.sound[self.current_sound])
            
            if time.time() - self.time > 0.7:
                if self.current_sound:
                    self.current_sound = 0
                else:
                    self.current_sound = 1
                self.time = time.time()
                
        except:
            self.stop()
            
    def mute(self):
        self.buzzer.ChangeFrequency(1)
            
    def stop(self):
        self.buzzer.stop()
        GPIO.cleanup()
        
if __name__ == '__main__':
    s = Buzzer(40)
    s.beep()
    time.sleep(1)
    s.mute()
    s.stop()