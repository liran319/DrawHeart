# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0, 3.0, 0.01)
theta = 2 * np.pi * r
ax = plt.subplot(111, polar=True)
ax.grid(False)
# ax.set_title("r=a(1-sinθ)")
# ax.plot(theta, 1 - np.sin(theta), color='r', linewidth=2)
plt.fill(theta, (1 - np.sin(theta)), 'r', lw=1)  # Fill the heart.
plt.show()
