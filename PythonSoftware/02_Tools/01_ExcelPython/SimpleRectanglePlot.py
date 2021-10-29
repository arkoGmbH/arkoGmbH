# Simple plot example
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['toolbar'] = 'None'

B=2100.0
H=3200.0

# Data for plotting
x=np.array([0, B, B, 0, 0])
y = np.array([0, 0, H, H, 0])

# Create ne axes subplot
fig, ax = plt.subplots()
#fig.suptitle("Title centered above all subplots", fontsize=14)


# Scatterplot on the axes
ax.plot(x, y)


# Axes labeling
ax.set(xlabel='', ylabel='',
       title='Fensterabmessungen')
ax.grid()

# Save the figure
fig.savefig("Fenster.png")
plt.show()

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()