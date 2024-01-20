import ipywidgets 
import numpy as np 
import matplotlib.pyplot as plt 

def plot_fct(w=1):
    X = np.random.uniform(low=0, high=5, size=100)
    y = 2 * X + w * np.random.normal(size =100)
    plt.scatter(X, y)
    plt.show()

# simple basic plot 
# plot_fct(10)

# interactive plot 
ipywidgets.interact(plot_fct, w=(0, 5, 0.5))