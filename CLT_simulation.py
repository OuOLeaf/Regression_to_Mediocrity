import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


p = 0.5
bins = 10
beads = 10000
np.random.seed(0)
samples = list(np.random.binomial(n = bins, p = p, size = beads))


plt.style.use('dark_background')
falling = []
times = 20
add_beads = int(beads/times)
for i in range(times + 1):
    n = (i + 1) * add_beads
    plt.hist(falling, bins = list(range(1, 11)), color = "orange", edgecolor = "purple", alpha = 1)
    plt.ylim(0, 2600)
    falling = np.append(falling, samples[:add_beads-1])
    del samples[:add_beads-1]
    plt.pause(0.1)
    plt.suptitle("Galton Board")
    plt.title(f"Binomial Simulation of {n} samples")
plt.show()