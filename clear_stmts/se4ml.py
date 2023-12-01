import matplotlib.pyplot as plt
import numpy as np

y = np.array([25, 75])
mylabels = ["Direct Student Interaction", "Lack Direct Student Interaction"]

plt.pie(y, labels = mylabels, autopct='%.1f%%')
plt.show() 