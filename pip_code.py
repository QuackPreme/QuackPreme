from hub import hardware_id, light_matrix, port, motion_sensor, button, light
from motor import BRAKE, ERROR, stop, velocity
import color_sensor, color, runloop, motor_pair, motor, hub, device


motor_pair.unpair(1)
WHEELS = motor_pair.PAIR_1
motor_pair.pair(WHEELS, port.A, port.B)

async def turn(angle,speed): # od code
        motion_sensor.reset_yaw(0)
        tspeed = int(speed*3.5)
        while abs(motion_sensor.tilt_angles()[0])<=angle*10:
            motor_pair.move_tank(0,tspeed,tspeed*-1)
        motor_pair.stop(0,stop=motor.BRAKE)
        print(motion_sensor.tilt_angles()[0])
    

async def drive_turn(distance, speed):
        motor.reset_relative_position(port.B,0)
        motor.reset_relative_position(port.A,0)
        wheelSpeed=int(speed*6.6)
        if wheelSpeed>0:
            while abs(motor.relative_position(port.B))<distance*28:
                motor_pair.move_tank(1,wheelSpeed,wheelSpeed+int(motor.relative_position(port.B)*motor.relative_position(port.B)))
def eatza(time):
        speed=(abs(motor.relative_position(port.B)*28)/(time*time))
        return speed

async def drive(distance, speed, mekadem=4): #more code
        motor.reset_relative_position(port.A,0)
        KP=2
        KI=1.1
        KD=1.00312
        x=1
        newSpeed=36
        motion_sensor.reset_yaw(0)
        tspeed=int(speed*mekadem)
        while abs(motor.relative_position(port.A))<abs(distance)*28:
            if newSpeed<tspeed:
                newSpeed+=int(eatza(x))
                x+=1
            elif newSpeed>=tspeed:
                newSpeed=tspeed
            error=int(((0-(motion_sensor.tilt_angles()[0]/10)*KP)*KI)*KD)
            motor_pair.move_tank(0,newSpeed-(error),newSpeed+error)
        motor_pair.stop(0,stop=motor.SMART_BRAKE)

def closest(angle,wheelsOrGyro=True): #code
    goTo=0
    if wheelsOrGyro:
        goTo_1=angle-((motion_sensor.tilt_angles()[0]/10)%360)
        goTo_2=(angle-((motion_sensor.tilt_angles()[0]/10)%360))+360
        goTo_3=(angle-((motion_sensor.tilt_angles()[0]/10)%360))- 360
        if abs(goTo_1)<abs(goTo_2) and abs(goTo_1)<abs(goTo_3):
            goTo=goTo_1
        elif abs(goTo_2)<abs(goTo_1) and abs(goTo_2)<abs(goTo_3):
            goTo=goTo_2
        elif abs(goTo_3)<abs(goTo_1) and abs(goTo_3)<abs(goTo_2):
            goTo=goTo_3
    else:
        goTo_1=angle-(motor.absolute_position(port.C)%360)
        goTo_2=(angle-(motor.absolute_position(port.C)%360))+360
        goTo_3=(angle-(motor.absolute_position(port.C)%360))- 360
        if abs(goTo_1)<abs(goTo_2) and abs(goTo_1)<abs(goTo_3):
            goTo=goTo_1
        elif abs(goTo_2)<abs(goTo_1) and abs(goTo_2)<abs(goTo_3):
            goTo=goTo_2
        elif abs(goTo_3)<abs(goTo_1) and abs(goTo_3)<abs(goTo_2):
            goTo=goTo_3
    return int(goTo)


async def straight_gyro(distance, speed): #more code
    motor.reset_relative_position(port.A,0)
    KP=1.4
    KI=0# pid
    KI=0# pid
    PD=0
    motion_sensor.reset_yaw(0)
    tspeed=int(speed*6.6) # control true speed
    while abs(motor.relative_position(port.A))<abs(distance)*28:
        error=int(((0-(motion_sensor.tilt_angles()[0]/10)*KP)*KI)*PD) #calc error
        motor_pair.move_tank(0,tspeed-(error),tspeed+error,acceleration=1000) # moves the robots
    motor_pair.stop(1,stop=motor.SMART_BRAKE)

async def turn_to(targetAngle,speed):
        goTo = closest(targetAngle) # the shortest path
        motion_sensor.reset_yaw(0)
        goTo = closest(180-targetAngle) # the shortest path
        wheelSpeed = int(speed*6.6) # the true speed
        while abs(goTo) > 0:
            newSpeed = int(wheelSpeed*(abs(goTo)/goTo)) #direction
        while abs(goTo) > 0:
            newSpeed = int(wheelSpeed*(abs(goTo)/goTo)) #direction
            motor_pair.move_tank(1,newSpeed,newSpeed*-1) # moves robot
            goTo = closest(targetAngle) # new error
            goTo = closest(180-targetAngle) # new error
        motor_pair.stop(1)

#Comments Below                 #Comments Below                 #Comments Below                 #Comments Below                 #Comments Below



"when im at 0 and i want to get to -100 so the traffic(how much i passed) will decrease by __ until it reaches -100"


#Active code below                  #Active code below                  #Active code below                  #Active code below


#Yellow
async def kraken_chest():
    print(motion_sensor.tilt_angles()[0])
    await drive(29, 150, 4)
    await turn(85, 45)
    await drive(10, 60, 2)
    await drive(10, -100, 4)
    await turn(90, -45)
    await drive(25, -100, 4)
    exit(1)
    await motor_pair.move_for_degrees(0, 147, 100)
    await motor_pair.move_for_degrees(0, 355, 0, velocity= 175)
    await motor.run_for_degrees(port.D, -45, 155)
    await motor_pair.move_for_degrees(0, 35, 0, velocity=275)
    await motor.run_for_degrees(port.D, 55, 160)

#Black
async def collection_red():
    print(motion_sensor.tilt_angles()[0])
    await motor_pair.move_for_degrees(0, 825, 0, velocity=700)
    await motor_pair.move_for_degrees(0,45,-100)
    await motor_pair.move_for_degrees(0, 135, 0, velocity=200)
    await motor_pair.move_for_degrees(0,275,-100, velocity=150)
    await motor_pair.move_for_degrees(0, 650, 0, velocity=650)

#Red
async def shark_coral():    #(pair, degrees, angle)
    print(motion_sensor.tilt_angles()[0])
    await straight_gyro(30, -40)
    await turn(35, 30)
    return
    await drive(40, -200, 4)
    await motor_pair.move_for_degrees(0, 40, 100)
    await motor_pair.move_for_degrees(0, 1295, 0, velocity=-600)
    await motor_pair.move_for_degrees(0, 70, -100)
    await motor_pair.move_for_degrees(0, 160, 0, velocity=-400)
    await motor_pair.move_for_degrees(0, 300, 0, velocity=400)
    await motor_pair.move_for_degrees(0, 68, -100)
    await motor_pair.move_for_degrees(0, 250, 0, velocity=-250)
    await motor.run_for_degrees(port.C, 450, 400)
    await motor_pair.move_for_degrees(0, 35, 100)
    await motor_pair.move_for_degrees(0, 300, 0, velocity=500)
    await motor_pair.move_for_degrees(0, 150, 100)
    await motor_pair.move_for_degrees(0, 70, 0, velocity=500)
    await motor_pair.move_for_degrees(0, 13, 100)
    await motor_pair.move_for_degrees(0, 110, 0, velocity=-300)
    await motor.run_for_degrees(port.C, 410, -600)
    await motor_pair.move_for_degrees(0, 8, 100)
    await motor_pair.move_for_degrees(0, 20, 100)
    await motor_pair.move_for_degrees(0, 1500, 0 , velocity=600)

#Magenta
async def collection_blue():
    print(motion_sensor.tilt_angles()[0])
    await motor_pair.move_for_degrees(0, 120, 0, velocity=600)
    await turn(43, -45)
    await drive(25, 115, 4)
    await motor_pair.move_for_degrees(0, 210, 0, velocity=-500)
    await turn(25,45)
    await drive(6, 100, 4)
    await turn(20, 45)
    await drive(11, 100, 4)
    await turn(5, 45)
    await drive(9, 100, 4)
    await motor_pair.move_for_degrees(0, 310, 0, velocity=-550)
    await turn(20, -45)
    await drive(11, 100)
    await turn(90, 45)
    await motor_pair.move_for_degrees(0, 205, 0, velocity=300)
    await motor_pair.move_for_degrees(0, 210, 0, velocity=-300)
    await motor_pair.move_for_degrees(0, 180, 100)
    await drive(15, 150, 4)
    await turn(20, -45)
    await drive(22, 150, 4)



async def gyro_test():
    await drive_turn(45, 45)
    await drive(25, 200, 4)
    await turn (90, -50)
    print(motion_sensor.tilt_angles()[0])



async def main():
    if color_sensor.color(port.E)== color.BLACK:
        await collection_red()
    if color_sensor.color(port.E)== color.YELLOW:
        await kraken_chest()
    if color_sensor.color(port.E)== color.RED:
        await shark_coral()
    if color_sensor.color(port.E)== color.MAGENTA:
        await collection_blue()
        

runloop.run(main())
