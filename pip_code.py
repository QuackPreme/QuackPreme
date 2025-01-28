158159160161162163164165166167168174175176157156155154177178179169171172173153170
    await drive(4.5, -75)    await drive(8, default_speed)    await turn(42, -30)    await drive(8.6, -40)    await turn(6.5, 30)    await drive(0.0001, 0.01)    await turn(6, 30)    await motor.run_for_degrees(port.C, 450, 400)    await drive(3, default_speed)    await turn(120, 50)    await drive(2, -150)    await turn(45, -30)    await drive(44.5, -default_speed)    print(motion_sensor.tilt_angles()[0])    default_speed = 125async def aquanaut():    default_speed = 150    await motor.run_for_degrees(port.C, 450, 400)    await motor.run_for_degrees(port.C, 450, -400)    await drive(15, default_speed)    await turn(25, -30)    await drive(30, default_speed)async def shark_coral():    #(pair, degrees, angle)    await turn(5, -30)
    await drive(8.6, -40)
    await turn(6.5, 30)
    await drive(0.0001, 0.01)
    await turn(6, 30)
    await motor.run_for_degrees(port.C, 450, 400)
    await drive(3, default_speed)
    await turn(120, 50)
    await drive(2, -150)
    await motor.run_for_degrees(port.C, 450, -400)
    await turn(5, -30)

0451425152-61-1202-92252
In the previous chapters, you tried using variables and random numbers to control the motors and the light. Now you’ll use a sensor value to control a motor.

Connect a motor to port A and a Force Sensor to port B and try the program below.



import force_sensor
import motor
from hub import port

# Store the force of the Force Sensor in a variable.
force = force_sensor.force(port.B)

# Print the variable to the Console.
print(force)

# Run the motor and use the variable to set the velocity.
motor.run(port.A, force)
Press the Force Sensor while the program is running. That didn’t do much, right? Luckily, the example uses the built-in print() function to write the force variable to the Console, so that you can easily see what went wrong.

The Console
Sometimes your program doesn’t do what you expect it to do. You can use the print() function to debug your program when that happens. The print() function writes whatever you pass as the argument to the Console window below the Code Editor, in this case the force of the Force Sensor. Run the program again and notice the value that appears in the Console.

You’ll see a single number in the console, and unless you were pressing the Force Sensor when you started the program, that number is 0. Running a motor at 0 degrees per second doesn’t do much, so the problem is that the program only checks the sensor value once at the start of the program. To update the motor velocity based on the force for as long as the program runs, you’ll need to use the while True loop again.

The Console also displays error messages when something goes wrong while running your program. One common error happens when you run a program to control a motor or read a sensor that isn’t connected. Disconnect the Force Sensor and run the same program one last time. You’ll see an error in the Console informing you that there was a problem, what the problem was, and on what line of code it happened.

Fix the Bugs
The Console helped you find two bugs. Reconnect the Force Sensor to port B to fix the second bug and then run the program below that fixes the first bug by wrapping the code in a while True loop.


import force_sensor
import motor
from hub import port

while True:
    # Store the force of the Force Sensor in a variable.
    force = force_sensor.force(port.B)

    # Print the variable to the Console.
    print(force)

    # Run the motor and use the variable to set the speed.
    motor.run(port.A, force)
Press the Force Sensor while the program is running. You’ll see the motor speeding up or slowing down depending on how hard you press the Force Sensor. You’ll also see a lot of variable values written in the Console. The Force Sensor force is measured in decinewtons (dN) and since the maximum force it can measure is 10 newtons, the maximum value in dN is 100. Running a motor at 100 degrees per second still isn’t very fast!

Function Return Values
Instead of storing the value of the Force Sensor in a variable, you can also define a function that returns this value. Separating the different parts of your program this way makes it easier to organize your code and fix bugs if they happen.

The next program defines a motor_velocity() function that returns the desired motor velocity based on the force of the Force Sensor instead of using a variable.


import force_sensor
import motor
from hub import port

# This function returns the desired motor velocity.
def motor_velocity():
    # The velocity is five times the force of the Force Sensor.
    return force_sensor.force(port.B) * 5

while True:
    # Run the motor like before.
    # Use the `motor_velocity()` function return value for velocity.
    motor.run(port.A, motor_velocity())
Press the Force Sensor while the program is running. You’ll see the motor speeding up or slowing down depending on how hard you press the Force Sensor. The motor_velocity() function multiplies the force value by 5, so the velocity will be between 0 and 500 degrees per second.

Challenge
Can you change the code to run the motor at 1000 degrees per second when the Force Sensor is fully pressed?
