# This file visualizes the histogram created in histogram.py

import numpy as np
import os
from matplotlib import pyplot as plt
import math

directory = os.getcwd()
fob = directory + "/" + "histogramdata.txt"
histdata = open(fob, "r")
objectlines = histdata.readlines()

nums = objectlines[0].split(',')
nums[0] = ' 18252' # Adjustment of the first and last elements of nums. This could be automated, but I only ran a few
                   #  histograms, so I didn't bother.
nums[-1] = ' 17867'

newnums = []
for num in nums:
    num = int(num)
    newnums.append(num)

bins = np.linspace(math.ceil(min(newnums)),
                   math.floor(max(newnums)),
                   40)
plt.hist(newnums, bins = bins, alpha=0.5)
plt.show()