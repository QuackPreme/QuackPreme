from hub import hardware_id, light_matrix, port, motion_sensor, button, light
from motor import BRAKE, ERROR, stop, velocity
import color_sensor, color, runloop, motor_pair, motor, hub, device
#from typing import Awaitable


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
                motor_pair.move_tank(0,wheelSpeed,wheelSpeed+int(motor.relative_position(port.B)*motor.relative_position(port.B)))
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
    motor_pair.stop(0,stop=motor.SMART_BRAKE)


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
        motor_pair.stop(0)

async def keshet(distance, speed,a):
        motor.reset_relative_position(port.A,0)
        wheelSpeed=int(speed*6.6)
        keshetSpeed=0
        while abs(motor.relative_position(port.A))<distance*28:
            if wheelSpeed>0:
                motor_pair.move_tank(0,wheelSpeed,int(wheelSpeed*a))
                motor_pair.move_tank(0,wheelSpeed,int(wheelSpeed*a))
            else:
                motor_pair.move_tank(0,int(-a*wheelSpeed),-1*wheelSpeed)
                motor_pair.move_tank(0,-int(a*wheelSpeed),-1*wheelSpeed)
        motor_pair.stop(0, stop=motor.BRAKE)

#Comments Below                #Comments Below                #Comments Below                #Comments Below                #Comments Below



"when im at 0 and i want to get to -100 so the traffic(how much i passed) will decrease by __ until it reaches -100"


#Active code below                #Active code below                #Active code below                #Active code below


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
    default_speed = 125
    print(motion_sensor.tilt_angles()[0])
    await drive(44.5, -default_speed)
    await turn(45, -30)
    await drive(4.5, -75)
    await drive(8, default_speed)
    await turn(42, -30)
    await drive(8.6, -40)
    await turn(6.5, 30)
    await drive(0.0001, 0.01)
    await turn(2, 30)
    await motor.run_for_degrees(port.C, 450, 400)
    await drive(3, default_speed)
    await turn(120, 50)
    await drive(2, -150)
    await motor.run_for_degrees(port.C, 450, -400)
    await turn(5, -30)
    await drive(17, default_speed)
    await turn(25, -30)
    await drive(30, default_speed)



async def aquanaut():
    default_speed = 150
    await motor.run_for_degrees(port.C, 450, 400)
    await drive(25, -default_speed)
    await turn(27, 30)
    await drive(16, -default_speed)
    await turn(5, 30)
    await motor.run_for_degrees(port.C , 450, -400)
    await turn(5, -30)
    await drive(25, default_speed)
    await turn(45, -30)
    await drive(16, default_speed)


#Magenta
async def collection_blue():
    default_speed = 125
    print(motion_sensor.tilt_angles()[0])
    # octopus
    await drive(6, default_speed, 4) # 70
    await turn(43, -30)
    await drive(20, 100, 4) #115
    # shrips/coral
    await motor_pair.move_for_degrees(0, 260, 0, velocity=-500)
    await turn(28,30)
    await drive(4, default_speed, 4)
    await turn(16, 30)
    await drive(18, default_speed , 4) # 150
    await motor_pair.move_for_degrees(0, 100, 0, velocity=-500)
    exit(1)
    await turn(10, 30)
    await drive(3, default_speed)
    await motor_pair.move_for_degrees(0, 100, 0, velocity=500)
    await motor_pair.move_for_degrees(0, 260, 0, velocity=-500)
    await turn(18, -30)
    await drive(18, default_speed)
    await motor_pair.move_for_degrees(0, 180, 0, velocity=-500)
    await turn(90, 30)
    await drive(5, default_speed)
    await drive(5, -default_speed)

async def collection_blue2 ():
    default_speed = 125
    await drive(6, default_speed, 4) # 70
    await turn(43, -30)
    await drive(20, 100, 4) #115
    # shrips/coral
    await motor_pair.move_for_degrees(0, 260, 0, velocity=-500)
    await turn(28,30)
    await drive(4, default_speed, 4)
    await turn(15, 30)
    await drive(15, default_speed)
    await motor_pair.move_for_degrees(0, 250, 0, velocity=-500)
    await turn(20, -30)
    await drive(8, default_speed)
    exit(1)
    await turn(25, 30)
    await drive(10, default_speed)
    await drive(6, -default_speed)
    await motor_pair.move_for_degrees(0, 250, 0, velocity=-500)

async def octopus ():
    default_speed = 125
    await drive(10, 100)
    await turn (45,-50)
    await drive(17, 100)
    await drive(9, -100)
    await turn (23,50)
    await drive(14, 100)
    await turn (50,15)
    await(50,-15)
    await drive(16, 100)
    await drive(20, -70)




async def platipus ():
    default_speed = 125
    await drive(20, 100)
    await turn (25,-50)
    await drive(10, 70)
    await turn (25,50)
    await drive(7, 70)
    await turn (30,50)
    await drive(14, 50)
    await drive(15, -70)
    await turn (37,-50)
    await drive(20, -60)
    await turn (20,-70)
    await drive(20, -70)

async def combined_2 ():
    default_speed = 100
    #octopus
    await drive(1, 150)
    await turn(55, -40)
    await drive(38, default_speed)
    await turn(55, 20)
    await drive(4, default_speed)
    await drive(3.5, -default_speed)
    #fish
    await turn(20, -30)
    await drive(4, default_speed)
    await turn(8, -30)
    await drive(15, default_speed)
    await turn(178, 30)
    await drive(1, default_speed)
    await turn(20, 30)
    exit(1)
#Loop Thingy
    await drive(9, default_speed)
    await turn(175, 50)
    await drive(3, -default_speed)
    await turn(30, 30)
    await motor.run_for_degrees(port.D, 450, 400)
    await drive(7, -default_speed)
    await motor.run_for_degrees(port.D, 450, -400)
    await drive(7, default_speed)
    await turn(35, 30)
    await drive(6, -500)
    await turn(5, 30)
    await drive(6, 125)
    await turn(50, 30)
    await drive(20, 100)
    await turn(50, -30)
    await drive(50, 100)



async def bigboat():
    await drive(15, 175, 4)
    await motor.run_for_degrees(port.D, 350, 200)
    await drive(10, -200, 4)
    await motor.run_for_degrees(port.D, 350, -200)

async def sharkplace():
    default_speed = 125
    await drive(30.5, default_speed)
    await turn(45, -30)
    await drive(8, 25)
    await drive(4, 50)
    await drive(2, -default_speed)
    await turn(40, 30)
    await drive(50, default_speed)
    await turn(40, 30)
    await drive(20, default_speed)

async def bigboat():
    default_speed = 30
    await drive(12, 45)
    await drive(12, -30)

async def gyro_test():
    await drive_turn(45, 45)
    await drive(25, 200, 4)
    await turn (90, -50)
    print(motion_sensor.tilt_angles()[0])



async def main():
    if color_sensor.color(port.E)== color.GREEN:
        await bigboat()
    if color_sensor.color(port.E)== color.BLACK:
        await collection_red()
    if color_sensor.color(port.E)== color.YELLOW:
        await sharkplace()
    if color_sensor.color(port.E)== color.RED:
        await shark_coral() # aquanaut()
    if color_sensor.color(port.E)== color.MAGENTA:
        await octopus()
    if color_sensor.color(port.E)== color.BLUE:
        await combined_2()
    if color_sensor.color(port.E)== color.WHITE:
        await bigboat()
    if color_sensor.color(port.E)== color.AZURE:
        await platipus()
runloop.run(main())
