/* Python script using the matplotlib library 
to create a line graph of the Packet Delivery Ratio (PDR) 
for both LEACH and OLSR under varying node 
mobility scenarios */

import matplotlib.pyplot as plt

# Data
node_mobility = [0.5, 1, 1.5, 2, 2.5]
leach_energy_consumption = [1200, 1500, 1800, 2100, 2500]
olsr_energy_consumption = [1500, 1200, 1300, 1400, 1600]

# Plotting the graph
plt.plot(node_mobility, leach_energy_consumption, marker='o', label='LEACH Energy Consumption (J)')
plt.plot(node_mobility, olsr_energy_consumption, marker='s', label='OLSR Energy Consumption (J)')

# Labels and title
plt.xlabel('Node Mobility (m/s)')
plt.ylabel('Energy Consumption (J)')
plt.title('Energy Consumption of LEACH and OLSR vs Node Mobility')

# Legend
plt.legend()

# Show the graph
plt.show()

