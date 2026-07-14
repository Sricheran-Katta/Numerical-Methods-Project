# importing the required libraries
import matplotlib.pyplot as plt
import numpy as np
import cmath
# defining the characteristic equation
f = lambda w: w**3 - (w**2) - w - 1
# j is the imaginary unit 

# defining and applying Muller's Method
def muller_method(char_eqn, w0, w1, w2, err):
    n = 1 # number of iterations
    roots = [] # an array to contain roots 
    errors = [] # an array to contain errors
    function = []
    while True:
        # P(x) = a(w2 - w)**2 + b(w - w2) + c
        # finding the coefficients of P(x)
        a = ((w1 - w2)*(f(w0) - f(w2)) - (w0 - w2)*(f(w1) - f(w2)))/((w0 - w2)*(w0 - w1)*(w1 - w2))
        b = ((((w0 - w2)**2)*(f(w1) - f(w2))) - (((w1 - w2)**2)*(f(w0) - f(w2))))/((w0 - w1)*(w0 - w2)*(w1 - w2))
        c = f(w2)
        function.append(abs(f(w2))) # storing the absolute functional values (magnitude)
        # calculating discriminant
        D = cmath.sqrt(b**2 - 4*a*c)
        # taking the greater value of denominator so that our root could be closer to our previous root
        if np.sign(b.real) == 1: # if sign of real part b is positive we are taking b + D else b - D. As b can be complex we are comparing real part of b.
            denom = b + D
        else : denom = b - D
        w3 = w2 - (2*c)/(denom) # w3 will be our new root, calculating it using our quadratic formula to fing roots
        w0, w1, w2 = w1, w2, w3 # resetting the values for next iteration
        error = abs((w2 - w1)/w2) # calculating the error(relative).
        errors.append(error) # appending error to the list
        roots.append(w2) # appending the root to the list
        #print(f"w0 = {w0}, w1 = {w1}, w2 = {w2}, error = {error}")
        print(f"The root after {n}th iteration is {w2}.")
        if error < err: # if tolerence condition is met the getting out of the loop
            return errors, function
        n += 1 # increasing the counter
print(muller_method(f, 1, 1.5, 1.8, 10**-4))
