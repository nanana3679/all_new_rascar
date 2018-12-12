#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time
from GPIO_LED import LED
from GPIO_Button import Button
from GPIO_PWM_Buzzer import Buzzer

class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)
        self.ledl = LED(22)
        self.button = Button(29)
        self.ledr = LED(36)
        self.buzzer = Buzzer(40)
        
    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    
    # Complete the code to perform Second Assignment
    # =======================================================================
    
    def line_tracing(self, lt_status):
        
        if lt_status == [0,0,1,0,0] or lt_status == [0,1,1,1,0]:
                return 90
                
        elif lt_status == [0,1,1,0,0] or lt_status == [1,1,1,1,0]:
                return 90-15
                
        elif lt_status == [0,0,1,1,0] or lt_status == [0,1,1,1,1]:
                return 90+15
                
        elif lt_status == [0,1,0,0,0] or lt_status == [1,1,1,0,0]:
                return 90-10
                
        elif lt_status == [0,0,1,1,1] or lt_status == [0,0,0,1,0]:
                return 90+10
                
        elif lt_status == [1,1,0,0,0]:
                return 90-30
                
        elif lt_status == [0,0,0,1,1]:
                return 90+30
                
        elif lt_status == [1,0,0,0,0]:
                return 90-35
            
        elif lt_status == [0,0,0,0,1]:
                return 90+35
        else:
            return 90
            
    def car_startup(self):
        
        current_speed = self.car.SLOW
        current_direction = 90
        current_distance = self.car.distance_detector.get_distance()
        
        while current_distance > 25 or current_distance == -1:
            
            lt_status = self.car.line_detector.read_digital()
            current_direction = self.line_tracing(lt_status)
            
            self.car.accelerator.go_forward(current_speed)
            self.car.steering.turn(current_direction)
            current_distance = self.car.distance_detector.get_distance()
            print(lt_status, current_distance)
            
            if current_direction > 90:
                self.ledl.turn_on()
                self.ledr.turn_off()
            else:
                self.ledl.turn_off()
                self.ledr.turn_on()
                
            if lt_status == [0,0,0,0,0]:
                
                print("back")
                if current_direction < 90:
                    self.ledl.turn_off()
                    self.ledr.turn_on()
                    self.car.steering.turn(90-35)
                    while not self.car.line_detector.read_digital()[3]:
                        self.car.accelerator.go_backward(current_speed)
                else:
                    self.ledl.turn_on()
                    self.ledr.turn_off()
                    self.car.steering.turn(90+35)
                    while not self.car.line_detector.read_digital()[1]:
                        self.car.accelerator.go_backward(current_speed)
                    self.ledl.turn_off()
                    self.ledr.turn_off()
                
        self.car.accelerator.stop()    
        self.button.wait_press()
        current_speed = self.car.NORMAL
        self.car.accelerator.go_forward(current_speed)
        lt_status = self.car.line_detector.read_digital()
                    
        while True:
                
                escape_time = 1.3
                self.buzzer.time = time.time()
                self.ledl.blink()
                self.ledr.blink()
                
                print("loop 1 in")
                while 1 in lt_status:
                    self.car.steering.turn(90-35)
                    lt_status = self.car.line_detector.read_digital()
                    print(lt_status)
                    self.buzzer.beep()
                    self.ledl.blink()
                    self.ledr.blink()
                    
                time.sleep(escape_time)
                self.car.steering.turn(90)
                
                print("loop 2 in")
                while lt_status == [0,0,0,0,0]:
                    lt_status = self.car.line_detector.read_digital()
                    self.buzzer.beep()
                    self.ledl.blink()
                    self.ledr.blink()
                
                print("loop 3 in")
                while 1 in lt_status:
                    self.car.steering.turn(90+35)
                    lt_status = self.car.line_detector.read_digital()
                    print(lt_status)
                    self.buzzer.beep()
                    self.ledl.blink()
                    self.ledr.blink()
                    
                time.sleep(escape_time+0.5)
                self.car.steering.turn(90)
                print("loop 4 in")
                while lt_status == [0,0,0,0,0]:
                    lt_status = self.car.line_detector.read_digital()
                    self.buzzer.beep()
                    self.ledl.blink()
                    self.ledr.blink()
                    
                print("loop out")
                break
                
        current_distance = self.car.distance_detector.get_distance()
        current_speed = self.car.NORMAL
        while current_distance > 15 or current_distance == -1:
            
            lt_status = self.car.line_detector.read_digital()
            current_direction = self.line_tracing(lt_status)
        
            self.car.accelerator.go_forward(current_speed)
            self.car.steering.turn(current_direction)
            current_distance = self.car.distance_detector.get_distance()
            print(lt_status, current_distance)
            self.buzzer.beep()
            self.ledl.blink()
            self.ledr.blink()
            
            
            if current_direction > 90:
                self.ledl.turn_on()
                self.ledr.turn_off()
            else:
                self.ledl.turn_off()
                self.ledr.turn_on()
                
            if lt_status == [0,0,0,0,0]:
                
                print("back")
                if current_direction < 90:
                    self.ledl.turn_off()
                    self.ledr.turn_on()
                    self.car.steering.turn(90-35)
                    while not self.car.line_detector.read_digital()[3]:
                        self.car.accelerator.go_backward(current_speed)
                        self.buzzer.beep()
                else:
                    self.ledl.turn_on()
                    self.ledr.turn_off()
                    self.car.steering.turn(90+35)
                    while not self.car.line_detector.read_digital()[1]:
                        self.car.accelerator.go_backward(current_speed)
                        self.buzzer.beep()
                    self.ledl.turn_off()
                    self.ledr.turn_off()
        
        current_speed = self.car.NORMAL
        self.buzzer.mute()

        self.car.accelerator.go_backward(current_speed)
        self.car.steering.turn(90+25)
        time.sleep(1.7) 
        
        self.car.accelerator.go_forward(current_speed)
        self.car.steering.turn(25)
        time.sleep(0.5)
        t = time.time()
        
        while time.time() - t < 2:
            
            lt_status = self.car.line_detector.read_digital()
            current_direction = self.line_tracing(lt_status)
        
            self.car.accelerator.go_forward(current_speed)
            self.car.steering.turn(current_direction)
            current_distance = self.car.distance_detector.get_distance()
            print(lt_status, current_distance)
            
            if lt_status == [0,0,0,0,0]:
                
                print("back")
                if current_direction < 90:
                    self.ledl.turn_off()
                    self.ledr.turn_on()
                    self.car.steering.turn(90-35)
                    while not self.car.line_detector.read_digital()[3]:
                        self.car.accelerator.go_backward(current_speed)
                else:
                    self.ledl.turn_on()
                    self.ledr.turn_off()
                    self.car.steering.turn(90+35)
                    while not self.car.line_detector.read_digital()[1]:
                        self.car.accelerator.go_backward(current_speed)
                    self.ledl.turn_off()
                    self.ledr.turn_off()
        
        self.car.accelerator.stop()
        self.car.steering.center_alignment()
        print("stop")
        
if __name__ == "__main__":
    try:
        myCar  = myCar("CarName")
        myCar.car_startup()
        
        
    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
