import collatz_steps
import matplotlib.pylab as plt

data = {}
for n in range(1, 10001):
    steps = collatz_steps.collatz_steps(n, False)
    if steps not in data:
        data[steps] = 0
    data[steps] += 1
lists = sorted(data.items())
x, y = zip(*lists)
plt.bar(x, y, color = "red", width = 1)
plt.xlabel("Step Count")
plt.ylabel("Frequency")
plt.title("'Frequency' vs 'Step Count' for 1 < N < 10000")
plt.show()
