import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)
years = ['2018', '2019', '2020'] #그래프는 리스트의 형태이어야 안깨짐
values = [100, 400, 900]

plt.bar(x, values)
plt.xticks(x, years)

plt.show()