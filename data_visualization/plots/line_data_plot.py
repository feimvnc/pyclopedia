import csv
import random
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import numpy as np 
from itertools import count
import pandas as pd 

# Define the data
# data = [
#     (1, 2),
#     (3, 4),
#     (5, 6),
#     (7, 8),
#     (9, 10),
#     (11, 12),
#     (13, 14),
#     (15, 16),
#     (17, 18),
#     (19, 20)
# ]

# create random numbers 
data = [] 
for i in range(100):
    data.append((i, random.randint(0,100)))

# Write the data to a CSV file
with open('example.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['x', 'y'])
    for row in data:
        csv_writer.writerow(row)


df = pd.read_csv(r"example.csv")
x = [] 
y = [] 

fig, ax = plt.subplots()
ax.plot(x, y)

counter = count(0, 1)
def update(i):
    idx = next(counter)
    x.append(df.iloc[idx, 0])
    y.append(df.iloc[idx, 1])
    plt.cla()
    ax.plot(x, y)

ani = FuncAnimation(fig = fig, func = update, interval = 200)
plt.show()


 
