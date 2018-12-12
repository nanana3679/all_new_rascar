#########################################################################
# Date: 2018/09/07
# file name: GPIO_Button_Example.py
# Purpose: This code has been generated for control Button Module
# if Button is Pressed then console print '0' else console print '1'
#########################################################################
                                                                                                                
# coding=utf-8
import RPi.GPIO as GPIO
import time

# Raspberry Pi 3번 핀을 버튼 입력으로 사용합니다.
class Button:
    def __init__(self, button_pin):
        self.button_pin = button_pin

        # Raspberry Pi 보드의 핀 순서를 사용합니다.
        GPIO.setmode(GPIO.BOARD)

        # button_pin을 GPIO 입력으로 설정합니다.
        GPIO.setup(button_pin, GPIO.IN)

    def wait_press(self):
        
        try:
            '''
            계속 반복해서 button_pin의 상태를 읽어 
            buttonInput 변수에 저장합니다.
            '''
            button_input = GPIO.input(self.button_pin)
            while button_input == GPIO.input(self.button_pin):
                pass
            print('button pressed')
               
        except KeyboardInterrupt:
            GPIO.cleanup()

"""
KeyboardInterrupt가 발생하면 핀 설정 상태를 초기화 합니다.
"""
if __name__ == '__main__':
    b = Button(29)
    b.wait_press()