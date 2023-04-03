/* Python script using the matplotlib library to create a line graph of the Packet Delivery Ratio (PDR) 
for both LEACH and OLSR under varying node mobility scenarios */

import matplotlib.pyplot as plt

node_mobility = [0.5, 1, 1.5, 2, 2.5]
leach_pdr = [85, 80, 75, 70, 65]
olsr_pdr = [92, 95, 97, 98, 99]

plt.plot(node_mobility, leach_pdr, marker='o', label='LEACH')
plt.plot(node_mobility, olsr_pdr, marker='s', label='OLSR')

plt.xlabel('Node Mobility (m/s)')
plt.ylabel('Packet Delivery Ratio (%)')
plt.title('Packet Delivery Ratio vs. Node Mobility')

plt.legend()
plt.grid()

plt.show()
