import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time

height = 0.0
velocity = 0.0
angle = 0.0
timesteps = 0.0
drop = []
distance = []
time_t = 0
#request input from the user, screen for correct input
#each of the while loops checks for valid inputs, printing an error is the input is wrong.
def Inputdata(a,b,c,d):
    while True:
        try:
            a = float(input("Please enter your height:"))
            a= abs(a)
            print("Height accepted")
            time.sleep(1)
            break
        except ValueError:
            print("This is not a valid input, please try again.")
            time.sleep(1)
            continue

    while True:
        try:
            b = float(input("Please Enter your initial velocity:"))
            b = abs(b)
            print("Velocity accepted")
            time.sleep(1)
            break
        except ValueError:
            print("This is not a valid input, please try again.")
            time.sleep(1)
            continue

#extra checks to see if the angle is within a forward motion
    while True:
        try:
            c = float(input("Please enter your initial angle in degrees:"))
        except ValueError:
            print("This is not a valid input, please try again.")
            time.sleep(1)
            continue
        if c < -90.0:
            print("The angle is too low, please enter a valid angle")
            time.sleep(1)
            continue
        if c > 90.0:
            print("The angle is too large, please enter a valid angle")
            time.sleep(1)
            continue
        print("angle accepted")
        time.sleep(1)
        break
        # we add an iterative step function to allow us to sample as precisely as the user wants
    while True:
        try:
            d = float(input("Please Enter the iteration steps:"))
            d = abs(d)
            print("Steps accepted")
            time.sleep(1)
            break
        except ValueError:
            print("This is not a valid input, please try again.")
            time.sleep(1)
            continue
#asks the user if the program should finally be run with their input:
    while True:
        ask = input("Do you wish to run the simulation? Y/N:\n")
        if ask == "Y":
            print("Running Simulation....")
            time.sleep(2)
            break
        if ask == "N":
            print("Quitting program....")
            time.sleep(1)
            quit()
        elif ask!= "Y" or ask!= "N":
            print("please enter a valid input")
            time.sleep(1)
            continue
    return a, b, c, d
#we define our simulation function
def simulation_simple_throw (h,a,v,s):
    #first we split velocity into x any y and define the starting time:
    t = 0.0
    vel_x = v * math.cos(math.radians(a))
    vel_y = v * math.sin(math.radians(a))
    #we define our variable storage:
    total_time = 0.0
    h_list = []
    d_list = []
    #we run the simulation here, first we check for a velocity in y, then solve for y:
    if vel_y == 0.0 :
        total_time = math.sqrt(2*h/9.81)
        max_height = h
        time_steps = total_time/s
        distance_max = vel_x*total_time
        while t <= total_time:
            h2 = -0.5*9.81*math.pow(t,2)+h
            h_list.append(h2)
            dist = vel_x * t
            d_list.append(dist)
            t+=time_steps
            continue
    elif vel_y != 0.0 :
        total_time = (vel_y/9.81) + math.sqrt(math.pow(vel_y/9.81,2)+(2*h/9.81))
        time_max_height = vel_y/9.81
        max_height = -1/2*9.81*math.pow(time_max_height,2)+vel_y*time_max_height+h
        timesteps = total_time/s
        distance_max = vel_x*total_time
        while t <= total_time:
            h2 = -0.5*9.81 * math.pow(t,2) + vel_y * t + h
            dist = vel_x * t
            h_list.append(h2)
            d_list.append(dist)
            t+=timesteps
            continue
    return h_list, d_list, total_time,max_height,distance_max

height, velocity, angle, timesteps = Inputdata(height, velocity, angle, timesteps)
drop, distance, time_t , height_max, max_distance= simulation_simple_throw(height,angle,velocity,timesteps)
print("Your values are: {},{},{}".format(height,velocity,angle))
time.sleep(2)
#we write our code to print out the plotted data
plt.plot(distance,drop,'bs')
plt.xlabel("Distance")
plt.ylabel("Height")
plt.figtext(0.6,0.8, "Relevant information:\n Time of flight: {:.3f} \n Maximum height: {:.3f} \n Maximum distance: {:.3f}" .format(time_t,height_max,max_distance))
plt.show()

