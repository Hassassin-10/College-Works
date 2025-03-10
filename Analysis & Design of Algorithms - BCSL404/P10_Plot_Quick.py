import matplotlib.pyplot as plt

n_values = [10000, 20000, 30000, 35000, 50000]
time_taken = [0.0000, 0.015000, 0.011000, 0.002000, 0.017000]

plt.plot(n_values, time_taken, marker='o')
plt.title('Quick Sort Time Complexity')
plt.xlabel('Number of Elements (n)')
plt.ylabel('Time taken (seconds)')
plt.grid(True)
plt.show()