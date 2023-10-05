import numpy as np

def main():
    i = 0 # integers can be delcared with a number
    n = 10 # here is another integer
    x = 19.0 # floating point numbers are delcared with a "."

    # we can used numpy to declare arrays quickly

    y = np.zeros(n,dtype=float) # delcares 10 zeros as floats using np

    # we can use for loops to iterate with a variable

    for i in range(n): # i in range [0,n-1]
        y[i] = 2.0 * float(i) + 1. #set y = 2i+1 as floats


    #we can also simply iterate through a variable
    for y_element in y: print(y_element)

#execute the main function
if __name__ == "__main__":
    main()