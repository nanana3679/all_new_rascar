#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

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
        lab = 0
        
        while lab < 2:
            
            lt_status = self.car.line_detector.read_digital()
            current_direction = self.line_tracing(lt_status)
            
            self.car.accelerator.go_forward(current_speed)
            self.car.steering.turn(current_direction)
            current_distance = self.car.distance_detector.get_distance()
            print(lt_status, current_distance)
            
            if 0 < current_distance < 25:
                
                escape_time = 1.5
                
                print("loop 1 in")
                while 1 in lt_status:
                    self.car.steering.turn(90-35)
                    lt_status = self.car.line_detector.read_digital()
                    print(lt_status)
                time.sleep(escape_time)
                self.car.steering.turn(90)
                
                print("loop 2 in")
                while lt_status == [0,0,0,0,0]:
                    lt_status = self.car.line_detector.read_digital()
                
                print("loop 3 in")
                while 1 in lt_status:
                    self.car.steering.turn(90+35)
                    lt_status = self.car.line_detector.read_digital()
                    print(lt_status)
                    
                time.sleep(escape_time)
                self.car.steering.turn(90)
                print("loop 4 in")
                while lt_status == [0,0,0,0,0]:
                    lt_status = self.car.line_detector.read_digital()
                    
                print("loop out")
                
            if lt_status == [0,0,0,0,0]:
                
                print("back")
                if current_direction < 90:
                    self.car.steering.turn(90-35)
                    while not self.car.line_detector.read_digital()[3]:
                        self.car.accelerator.go_backward(current_speed)
                else:
                    self.car.steering.turn(90+35)
                    while not self.car.line_detector.read_digital()[1]:
                        self.car.accelerator.go_backward(current_speed)
                
                
            elif lt_status == [1,1,1,1,1]:
                lab += 1
                while lt_status == [1,1,1,1,1]:
                    lt_status = self.car.line_detector.read_digital()
            
            
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
