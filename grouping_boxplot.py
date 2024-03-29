import numpy as np
import matplotlib.pyplot  as plt
spread = 100*np.random.rand(100)
center = np.ones(50)*50
print(spread)
print(center)
flier_high = 100*np.random.rand(10)+100
flier_low = -100*np.random.rand(100)
print(flier_high)
print(flier_low)
data = np.concatenate((spread,center,flier_high,flier_low))

plt.boxplot(data,sym='gx',widths=.75,notch=True)
plt.show()
