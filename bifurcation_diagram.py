#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 10:50:52 2020

@author: evan
"""

# period-doubling bifurcation

# see: https://en.wikipedia.org/wiki/Logistic_map
# https://en.wikipedia.org/wiki/Bifurcation_diagram

import numpy as np
import matplotlib.pyplot as plt

plt.figure()
rr = np.linspace(2.6, 4, 281)
for r in rr:
    ni = 600            # number of iterations
    x = np.zeros(ni)
    x[0] = np.random.rand()     # random starting point
#    x[0] = 0.5                 # fixed starting point
    for i in np.arange(1, ni):
        x[i] = r * x[i-1] * (1 - x[i-1])
    # plot the second half of x, i.e. the steady state
    plt.plot(r*np.ones(int(ni/2)), x[-int(ni/2):], 'k.', markersize=0.5)
plt.ylim(0, 1)
plt.xlabel('r')
plt.ylabel(r'$\lim_{n \to \infty} x_n$')
plt.show()
