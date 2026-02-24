import matplotlib.pyplot as plt
import random

def model_two(npts):
    numbers = []
    for _ in range(npts):
        numbers.append(random.random())
    plt.hist(numbers, 50)
    plt.show()

if __name__ == "__main__":
    model_two(100)

 

 

