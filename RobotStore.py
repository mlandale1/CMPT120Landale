# Matthew Landale
# Lab 8
# 15 November 2019

def main():
    print()
    print("Available Products")
    print("------------------")
main()

cash = float(input("How much money do you have: "))
while cash > 0:
    

print("------------------")
 
class RobotStore:
    
    def __init__(self):  
        self.Ultrasonic_range_finder = "Ultrasonic range finder [$2.50] [Q:4]"
        self.Servo_motor = "Servo motor [$14.99] [Q:10]"
        self.Servo_controller = "Servo controller [$44.95] [Q:10]"
        self.Microcontroller_Board = "Microcontroller Board [$34.95] [Q:7]"
        self.Laser_range_finder = "Laser range finder [$149.99] [Q:2]"
        self.Lithium_polymer_battery = "Lithium polymer battery [$8.99] [Q:8]"

    def print_RobotStore(self):
        print(self.Ultrasonic_range_finder)
        print(self.Servo_motor)
        print(self.Servo_controller)
        print(self.Microcontroller_Board)
        print(self.Laser_range_finder)
        print(self.Lithium_polymer_battery)

obj = RobotStore()

obj.print_RobotStore()



