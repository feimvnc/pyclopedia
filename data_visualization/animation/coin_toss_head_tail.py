import matplotlib.pyplot as plt 
import random 

heads_tails = [0, 0]
for _ in range(1000):
    plt.clf()
    heads_tails[random.randint(0, 1)] += 1
    plt.bar([0,1], heads_tails, color=("blue", "red"))
    plt.pause(0.001)

plt.show()

# following is from perplexity.ai by asking "write a python matplot script for coin toss animation"
# import numpy as np
# import matplotlib.pyplot as plt
# import random

# def coin_toss_animation(n_tosses):
#     # Create a list of random tosses
#     tosses = [random.choice([True, False]) for _ in range(n_tosses)]

#     # Create a list of x values for the line
#     x = np.linspace(0, 1, n_tosses)

#     # Create a list of y values for the line using the tosses list
#     y = [1 if toss else 0 for toss in tosses]

#     # Plot the coin tosses
#     plt.plot(x, y, marker='o', linestyle='-')

#     # Set the x-axis label
#     plt.xlabel('Number of Tosses')

#     # Set the y-axis label
#     plt.ylabel('Heads (1) or Tails (0)')

#     # Display the plot
#     plt.show()

# # Number of coin tosses
# n_tosses = 100

# # Call the coin_toss_animation function
# coin_toss_animation(n_tosses)