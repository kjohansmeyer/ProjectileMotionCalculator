import numpy as np
import matplotlib.pyplot as plt

# -------------- Projectile Motion Function (do not change this) ---------------
def projectile_motion(v0,thetaD,initialHeight):
  """ Function parameters:
  v0 - initial velocity (meters per second)
  thetaD - angle of launch (degrees) measured from the horizontal, must be on interval [-90,90]
  initialHeight - initial height of launch (meters) [or "height of cliff"]
  
  Program plots the object's trajectory along with useful values at maximum
  height and point of impact.
  """
  if thetaD in range(-90,90) and initialHeight >=0 and v0 >= 0:
    thetaR = (thetaD/180)*np.pi #convert degrees to radians (np.cos expects radians)
    g = -9.8 #meters per second squared (acceleration due to gravity)

    # Time
    tmax = max(np.roots([(1/2)*g,v0*np.sin(thetaR),initialHeight]))
    deltat = 0.001
    t = np.arange(0,tmax,deltat)
    
    # Position
    x = np.zeros(len(t)) # x-position
    y = np.zeros(len(t)) # y-position
    x[0] = 0 # initial x-position
    y[0] = initialHeight # initial y-position

    # Velocity
    vx = np.zeros(len(t)) # x-velocity
    vy = np.zeros(len(t)) # y-velocity
    vx[0] = v0*np.cos(thetaR) # initial x-velocity
    vy[0] = v0*np.sin(thetaR) # initial y-velocity
    

    for n in range(0,len(t)):
      x[n] = v0*np.cos(thetaR)*t[n] # x-position
      y[n] = initialHeight + v0*np.sin(thetaR)*t[n] + (1/2)*g*(t[n])**2 # y-position
      vx[n] = v0*np.cos(thetaR) # x-velocity (constant)
      vy[n] = v0*np.sin(thetaR) + g*t[n] # y-velocity


    xmax = x[len(t)-1]
    tHighestPoint = -v0*np.sin(thetaR)/g
    xHighestPoint = v0*np.cos(thetaR)*tHighestPoint
    yHighestPoint = max(y)
    finalVelocity = np.sqrt((vx[len(t)-1]**2 + vy[len(t)-1]**2))
    
    # -------------------------------- Plotting --------------------------------
    plt.plot(xHighestPoint,yHighestPoint,'bo') # Plot blue dot at highest point
    plt.plot(x[len(t)-1],y[len(t)-1],'ro') # Plot red dot at final point
    plt.plot(x,y) # Plots x and y values
    plt.title("Projectile Motion Plot") # Creates title for plot
    plt.ylabel("Vertical Position (meters)") # y-axis label
    plt.xlabel("Horizontal Position (meters)") # x-axis label
    plt.vlines(0,0,initialHeight) # Plots vertical cliff line
    plt.hlines(initialHeight,-1,0) # Plots horizontal ground line (take-off)
    plt.hlines(0,0,x[len(t)-1]+1) # Plots horizontal ground line (landing)
    if xHighestPoint > 0:
      plt.vlines(xHighestPoint,0,yHighestPoint,linestyles="dotted")
    plt.axis('equal') # Makes the x and y intervals the same
    plt.text(0,-yHighestPoint/4,"$v_0 =$ {}".format(v0))
    plt.text((2.5/8)*xmax,-yHighestPoint/4,"theta = {}".format(thetaD))
    plt.text((5.5/8)*xmax,-yHighestPoint/4,"Initial height = {}".format(initialHeight))
    plt.show()

    # ----------------------------- Print Outputs ------------------------------
    print("Peak of Trajectory (blue dot):")
    print("Time to Reach Maximum Height:",tHighestPoint,"seconds")
    print("Maximum Height:",yHighestPoint,"meters")
    print("")
    print("End of Trajectory (red dot):")
    print("Hangtime:",tmax,"seconds")
    print("Total Horizontal Displacement:",xmax,"meters")
    print("Final Horizontal Velocity:",vx[len(t)-1],"meters per second")
    print("Final Vertical Velocity:",vy[len(t)-1],"meters per second")
    print("Final Velocity (resultant):",finalVelocity,"meters per second")

  else:
    print("Error: use thetaD on interval [-90,90] and positive v0 & initial height values")

  return

# ----------------------------------- Example ----------------------------------
# Now we have to call the function and specify the needed parameters 
# (initial velocity, theta in degrees, and initial height). Below is an example 
# for a projectile with an initial velocity of  10  meters per second, an 
# initial angle of  20 degrees, and an initial height of  5  meters.
projectile_motion(10,20,5)
