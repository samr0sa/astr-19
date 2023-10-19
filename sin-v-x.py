import numpy as np

def main():
    x = np.linspace(0.0, 2*np.pi, num=1000)
    sin_x = np.sin(x)
    # Print the table of generated numbers
    for i in range(1000):
        print(f"{x[i]:.3f} \t  | \t {sin_x[i]:.3f}")
        # ^ the ":.3f" tells the script to only print out
        # to the nearest thousandth



# need to have the main program function
if __name__ == "__main__":
    print()
    print("x \t  | \t sin(x)")
    print("----------+-----------")
    # printing some aesthetic choices
    main()