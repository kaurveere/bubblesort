import matplotlib.pyplot as plt


#Fill this array with the collected energy values in Joules
x1 = [.., .., .., .., ..]
y1 = [10000, 20000, 30000, 40000, 50000]


#Fill this array with the time values in seconds
x2 = [.., .., .., .., ..]
y2 = [10000, 20000, 30000, 40000, 50000]


#Finding and applying the coefficient
k = 0
for i in range(len(x1)):
   k += x1[i]/x2[i]
k = k/len(x1)


for i in range(len(x2)):
   x2[i] = x2[i]*k


#Making the graph
plt.plot(x1, y1, 'o-', label='Energy usage (J)')
plt.plot(x2, y2, 's--', label='Time spent (s)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Time and energy usage comparison')
plt.grid(True)
plt.legend()
plt.show()