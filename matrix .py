import ultrasonic as ultrasonic
import hall_counter as hlc
import movement as move
import time
import detection
import npk_handle

initial_direction = 0
alternate_direction = 0
breadth = int(input("Enter Breadth (X Axis): "))  # X Axis
length = int(input("Enter Length (Y axis): "))  # Y Axis



x = 1
y = 1
max_flag = 0

forwardDelay = int(input("Enter Forward delay offset value:"))
stopDelay = int(input("Enter Stop delay offset value:"))
rotateDelay = int(input("Enter Rotate delay offset value:"))
passDelay = int(input("Enter Pass delay offset value:"))

initial_direction = ultrasonic.min_distance()
alternate_direction = ultrasonic.alt_direction(initial_direction)



def active():
    global x
    global y
    move.rotate(initial_direction)
    print(f"Rotate INIT-{initial_direction} Direction")
    time.sleep(rotateDelay)
    while y < length:
        if y%2==0:
            y +=1
        x = 1
        for x in range(x, breadth,1):
            move.movement("FORWARD")
            print("moving Forward")
            time.sleep(forwardDelay)
            print("Stopped!")
            move.stop()
            detection.detect(alternate_direction)
            npk_handle.test()
            time.sleep(stopDelay)
            print("Arrived Plot", "(", y, ",", x, ")", end="\t")
            if x == breadth-1:
                y += 1
                move.rotate(alternate_direction)
                print(f"Rotate ANTI-INIT-{alternate_direction} Direction")
                time.sleep(rotateDelay)
                move.stop()
                time.sleep(stopDelay)
                print("Stopped!")
                move.passing()
                print("Passing")
                time.sleep(passDelay)
                move.stop()
                print("Stopped!")
                time.sleep(stopDelay)
                move.rotate(alternate_direction)
                print(f"Rotate ANTI-INIT-{alternate_direction} Direction")
                time.sleep(rotateDelay)
                move.stop()
                print("Stopped!")
                time.sleep(stopDelay)
                for x in range(x,0,-1):
                    move.movement("FORWARD")
                    print("moving Forward")
                    time.sleep(forwardDelay)
                    move.stop()
                    print("Stopped!")
                    detection.detect(initial_direction)
                    npk_handle.test()
                    time.sleep(stopDelay)
                    print("Arrived Plot", "(", y, ",", x, ")", end="\t")
                    if x == 1:
                        move.rotate(initial_direction)
                        print(f"Rotate INIT-{initial_direction} Direction")
                        time.sleep(rotateDelay)
                        move.stop()
                        print("Stopped!")
                        time.sleep(stopDelay)
                        move.passing()
                        print("Passing")
                        time.sleep(passDelay)
                        move.stop()
                        print("Stopped!")
                        time.sleep(stopDelay)
                        move.rotate(initial_direction)
                        print(f"Rotate INIT-{initial_direction} Direction")
                        time.sleep(rotateDelay)
                        move.stop()
                        print("Stopped!")
                        time.sleep(stopDelay)
            print("\n")
active()