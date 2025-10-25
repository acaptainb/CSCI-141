import matplotlib.pyplot as plt

data = {}
for i in range(10):
    data[i] = i * i
plt.bar(list(data.keys()), list(data.values()), color='skyblue')
plt.show()