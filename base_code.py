from hub import light_matrix, motion_sensor, port, button, light
import runloop ,motor_pair,motor, hub, device, color_sensor, color
motor_pair.unpair(1)
motor_pair.pair(1,port.A,port.B)
soferDegrees=0
async def main():
    motion_sensor.reset_yaw(0)
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
    

    async def straight_gyro(distance, speed): #more code
        motor.reset_relative_position(port.A,0)
        KP=1.4
        KI=0  # pid 
        KI=0# pid
        PD=0
        motion_sensor.reset_yaw(0)
        tspeed=int(speed*6.6) # control true speed
        while abs(motor.relative_position(port.A))<abs(distance)*28:
            error=int(((0-(motion_sensor.tilt_angles()[0]/10)*KP)*KI)*PD) #calc error
            motor_pair.move_tank(1,tspeed-(error),tspeed+error,acceleration=1000) # moves the robots
        motor_pair.stop(1,stop=motor.SMART_BRAKE)
    async def keshet(distance, speed,a):
        motor.reset_relative_position(port.A,0)
        wheelSpeed=int(speed*6.6)
        keshetSpeed=0
        while abs(motor.relative_position(port.A))<distance*28:
            if wheelSpeed>0:
                motor_pair.move_tank(1,wheelSpeed,wheelSpeed*a)
                motor_pair.move_tank(1,wheelSpeed,int(wheelSpeed*a))
            else:
                motor_pair.move_tank(1,-a*wheelSpeed,-1*wheelSpeed)
                motor_pair.move_tank(1,-int(a*wheelSpeed),-1*wheelSpeed)
        motor_pair.stop(1, stop=motor.BRAKE)


    #write your code here
    await turn_to(90,20 )
    await straight_gyro( 15,75)
    await keshet(20,40,2)



    #await turn_to( 90,20 )
    #await turn_to( 45,20 )
    # speed must be negative to move back
    #await straight_gyro(-5,-20)
    #await keshet(20,20,2)
    await straight_gyro(25,45)
    await straight_gyro(12,-40)
    await turn_to(30,20)
    await straight_gyro(8,40)
    await turn_to(30,20)
    await straight_gyro(8,49)
runloop.run(main())