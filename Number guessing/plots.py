import matplotlib.pyplot as plt

period = [0.02, 0.04, 0.06] # Period values in seconds

frequency = [1 / T for T in period] # Calculate frequencies using the formula f = 1/T

plt.plot(period, frequency)
plt.xlabel('Period (s)')
plt.ylabel('Frequency (Hz)')
plt.title('Relationship between Period and Frequency')
plt.show()