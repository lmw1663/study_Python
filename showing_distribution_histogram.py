import numpy as np
import matplotlib.pyplot as plt

x= 20*np.random.randn(10000)

plt.hist(x,25,range=(-50,50),histtype='stepfilled',align='mid',color='g',label='Test Data')
plt.legend()
plt.title('Step Filled Histogram')
plt.show()