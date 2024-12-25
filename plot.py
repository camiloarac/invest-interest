import matplotlib.pyplot as plt
import numpy as np

def plot_xy(x: list, y: list):
    x_arr = np.array(x)
    y_arr = np.array(y)
    fig, ax = plt.subplots()
    ax.plot(x_arr, y_arr, color="blue", linewidth=1)
    ax.set_xlabel("Years")
    ax.set_ylabel("Savings")
    ax.set_title("Savings over the years")

    plt.show()