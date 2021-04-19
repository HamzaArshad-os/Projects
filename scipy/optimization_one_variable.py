# scipy Optimization with .minimize
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdtech

import scipy.optimize as spo

# Function to minimize
def f(x):
    y = (x**2) - (12 * x) + 20
    return y

#Function to minimise for two coordinates  uses this later on in the video 
def f(xy):
    x = xy[0]
    y = xy[1]
    area = x * y
    return -area 
    
# Starting guess
x_start = 2.0

# optimizing
result = spo.minimize(f, x_start, options={"disp": True})

# Print result
if result.success:
    print("Success!")
    print(f"x = {result.x} y = {result.y}")  #you wrote result.fun before
else:
    print("Sorry, could not find a minimum.")
