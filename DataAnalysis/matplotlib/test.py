from matplotlib import pyplot as plt
import numpy as np
x=range(2,26,2)
y=[12,13,14,15,16,17,18,19,20,15,14,16]
plt.figure(figsize=(20,8),dpi=80)
plt.xticks(np.arange(10,30 ,0.5))
plt.plot(x,y)
plt.savefig("../img/test.png")
plt.show()

