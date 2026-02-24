import matplotlib.pyplot as plt
import numpy as np

def model_one():
    x = np.arange(-2.0, 2.0, .01)
    y = x**2-1
    plt.plot(x, y)
    plt.xlabel('time (s)')
    plt.ylabel('volts (mV)')
    plt.show()

if __name__ == "__main__":
    model_one()

 