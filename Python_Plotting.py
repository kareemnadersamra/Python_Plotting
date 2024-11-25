#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 04:59:13 2024

@author: kareem
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch

#This plotting is for Form3 Tension.
df1 = pd.read_excel(r'')
print(df1)


# Generate x-axis values
x1 = list(df1['Pressure-1'])
x2 = list(df1['Pressure-2'])
x3 = list(df1['Pressure-3'])

# Generate y-axis values for each graph
y1 = list(df1['enthalpy-1'])
y2 = list(df1['enthalpy-2'])
y3 = list(df1['enthalpy-3'])


# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(15, 10))



# Plot each graph
ax1.plot(x1, y1,marker="x", label='Form1', markersize= 12)
ax1.plot(x2, y2,marker='o' ,label='Form2', markersize=12)
ax1.plot(x3, y3,marker='^' ,label='Form3', markersize=12)

ax1.set_xlim(-0.002, 0.0016)

# Set the x-axis label
ax1.set_xticks([-0.002,-0.001, 0, 0.001, 0.002]) 

ax1.set_xlabel('Pressure by Ry/au^3', color="blue", fontsize=35)
ax1.set_ylabel('Enthalphy by Ry', color="blue", fontsize=35)
ax1.tick_params(axis='both', labelsize=35)  

# Set the title
ax1.set_title('Pressure Induced Phase Transition', color='Green', fontsize=30)

# Show the legend
ax1.legend(fontsize=30)

#Zoomed Graph
axins = ax1.inset_axes([0.45,0.1,0.52,0.39])
axins.plot(x1, y1, marker='x', label='Form1', markersize= 12, alpha=0.7)
axins.plot(x2, y2, marker='o', label='Form2', markersize= 12, alpha=0.7)
axins.plot(x3, y3 ,marker='^', label='Form3', markersize= 12, alpha=0.7)
x1, x2, y1, y2 = -0.00009, 0.0016, -194.5, -192.5
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
axins.tick_params(axis='both', labelsize=30)
ax1.indicate_inset_zoom(axins, edgecolor='purple', lw=7, ls='dashed')

# Show the plot

plt.show()
