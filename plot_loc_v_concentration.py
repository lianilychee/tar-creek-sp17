# Import pertinent libraries
import matplotlib.pyplot as plt
import numpy as np


########## FORMAT CSV ##########
# Initialize the dataset
# 1-5 represent ore, settling, chat, wetland core, and floodplains, respectively
data_raw = {
    5: { 'Zn': [], 'Cd': [], 'Pb': [], 'Zn e': [], 'Cd e': [], 'Pb e': []},
    4: { 'Zn': [], 'Cd': [], 'Pb': [], 'Zn e': [], 'Cd e': [], 'Pb e': []},
    3: { 'Zn': [], 'Cd': [], 'Pb': [], 'Zn e': [], 'Cd e': [], 'Pb e': []},
    2: { 'Zn': [], 'Cd': [], 'Pb': [], 'Zn e': [], 'Cd e': [], 'Pb e': []},
    1: { 'Zn': [], 'Cd': [], 'Pb': [], 'Zn e': [], 'Cd e': [], 'Pb e': []}
}

with open('dataset2.csv') as f:   # Open the CSV

    for line in f:   # Read the file line-by-line
        row = line.strip().split(',')   # Split the items per row by commas

        if len(row[0]) == 1:   # Ignore the CSV headers by counting item length
            loc = int(row[0])   # Set the location

            # Populate the data_raw dataset
            data_raw[loc]['Zn'].append(float(row[4]))
            data_raw[loc]['Cd'].append(float(row[5]))
            data_raw[loc]['Pb'].append(float(row[6]))
            data_raw[loc]['Zn e'].append(float(row[7]))
            data_raw[loc]['Cd e'].append(float(row[8]))
            data_raw[loc]['Pb e'].append(float(row[9]))


########## CALCULATE AVERAGES ##########
# Initialize the dataset
data_avg = {
    5: { 'Zn': [], 'Cd': [], 'Pb': []},
    4: { 'Zn': [], 'Cd': [], 'Pb': []},
    3: { 'Zn': [], 'Cd': [], 'Pb': []},
    2: { 'Zn': [], 'Cd': [], 'Pb': []},
    1: { 'Zn': [], 'Cd': [], 'Pb': []}
}

# Calculate the averages per location per element, and add to data_avg dataset
for loc in data_raw:
    data_avg[loc]['Zn'] = np.mean(data_raw[loc]['Zn'])
    data_avg[loc]['Cd'] = np.mean(data_raw[loc]['Cd'])
    data_avg[loc]['Pb'] = np.mean(data_raw[loc]['Pb'])
    data_avg[loc]['Zn e'] = np.mean(data_raw[loc]['Zn e'])
    data_avg[loc]['Cd e'] = np.mean(data_raw[loc]['Cd e'])
    data_avg[loc]['Pb e'] = np.mean(data_raw[loc]['Pb e'])


########## FORMAT DATA INTO PLOTTABLE FORMAT ##########

# Format avgs into a plottable format
x = [1,2,3,4,5]
y_zn = [ data_avg[1]['Zn'], data_avg[2]['Zn'], data_avg[3]['Zn'], data_avg[4]['Zn'], data_avg[5]['Zn'] ]
y_cd = [ data_avg[1]['Cd'], data_avg[2]['Cd'], data_avg[3]['Cd'], data_avg[4]['Cd'], data_avg[5]['Cd'] ]
y_pb = [ data_avg[1]['Pb'], data_avg[2]['Pb'], data_avg[3]['Pb'], data_avg[4]['Pb'], data_avg[5]['Pb'] ]

# Calculate errors
err_zn = [ np.sqrt(data_avg[1]['Zn']) + data_avg[1]['Zn e'], 
            np.sqrt(data_avg[2]['Zn']) + data_avg[2]['Zn e'], 
            np.sqrt(data_avg[3]['Zn']) + data_avg[3]['Zn e'], 
            np.sqrt(data_avg[4]['Zn']) + data_avg[4]['Zn e'], 
            np.sqrt(data_avg[5]['Zn']) + data_avg[5]['Zn e'] ]

err_cd = [ np.sqrt(data_avg[1]['Cd']) + data_avg[1]['Cd e'], 
            np.sqrt(data_avg[2]['Cd']) + data_avg[2]['Cd e'], 
            np.sqrt(data_avg[3]['Cd']) + data_avg[3]['Cd e'], 
            np.sqrt(data_avg[4]['Cd']) + data_avg[4]['Cd e'], 
            np.sqrt(data_avg[5]['Cd']) + data_avg[5]['Cd e'] ]

err_pb = [ np.sqrt(data_avg[1]['Pb']) + data_avg[1]['Pb e'], 
            np.sqrt(data_avg[2]['Pb']) + data_avg[2]['Pb e'], 
            np.sqrt(data_avg[3]['Pb']) + data_avg[3]['Pb e'], 
            np.sqrt(data_avg[4]['Pb']) + data_avg[4]['Pb e'], 
            np.sqrt(data_avg[5]['Pb']) + data_avg[5]['Pb e'] ]


########## GENERATE PLOT ##########

# Fontsize variables
title_size = 30
label_size = title_size * 0.8

# X-axis formatting
# Finagling to get text x-labels, instead of values
# http://stackoverflow.com/questions/11244514/modify-tick-label-text
fig, ax = plt.subplots()
fig.canvas.draw()
x_labels = ['Ore', '', 'Settling', '', 'Chat Piles', '', 'Wetland Cores', '', 'Floodplains']
ax.set_xticklabels(x_labels, fontsize=label_size)
plt.xlabel('Location', fontsize=label_size)

# Y-axis formatting
ax.tick_params(axis='y', which='major', labelsize=label_size)
ax.set_yscale('log')
plt.ylabel('Concentration (ppm)', fontsize=label_size)

# Plot data
plt.errorbar(x, y_zn, yerr=err_zn, label='[Zn]', marker='o', linewidth=7)
plt.errorbar(x, y_cd, yerr=err_cd, label='[Cd]', marker='o', linewidth=7)
plt.errorbar(x, y_pb, yerr=err_pb, label='[Pb]', marker='o', linewidth=7)

# Show plot
plt.title('Location v. Heavy Metal Concentrations', fontsize=title_size)
plt.legend(loc=3, fontsize=label_size)
plt.grid()
plt.show()