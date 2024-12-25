import matplotlib.pyplot as plt
import numpy as np

def plot_xy(x: list, y: list):
    x_arr = np.array(x)
    y_arr = np.array(y)
    fig, ax = plt.subplots()
    ax.scatter(x_arr, y_arr)
    plt.show()