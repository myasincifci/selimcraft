import numpy as np
import matplotlib.pyplot as plt

CHUNKSIZE = 16

def gaussian(x, m=0.0, s=1.0):
    return (1/(s*np.sqrt(2*np.pi)))*np.exp(-(1/2)*(((x - m)**2)/s**2))

def main():
    X = np.arange(0, CHUNKSIZE)
    Y = gaussian(X, 7, 5)
    
    plt.plot(X, Y)
    plt.show()

if __name__ == '__main__':
    main()