# Import pertinent libraries
import matplotlib.pyplot as plt
import numpy as np


########## FORMAT CSV ##########
# Initialize the dataset
# 1-5 represent ore, settling, chat, wetland core, and floodplains, respectively
data_raw = {
    5: { 'Zn': [], 'Cd': [], 'Pb': []},
    4: { 'Zn': [], 'Cd': [], 'Pb': []},
    3: { 'Zn': [], 'Cd': [], 'Pb': []},
    2: { 'Zn': [], 'Cd': [], 'Pb': []},
    1: { 'Zn': [], 'Cd': [], 'Pb': []}
}

with open('! compiled- loc v. concentration.csv') as f:   # Open the CSV

    for line in f:   # Read the file line-by-line
        row = line.strip().split(',')   # Split the items per row by commas
        
        if len(row[0]) == 1:   # Ignore the CSV headers by counting item length
            loc = int(row[0])   # Set the location

            # Populate the data_raw dataset
            data_raw[loc]['Zn'].append(float(row[2]))
            data_raw[loc]['Cd'].append(float(row[3]))
            data_raw[loc]['Pb'].append(float(row[4]))


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


########## GENERATE GRAPH ##########

# Format avgs into a graphable format
x = [1,2,3,4,5]
y_zn = [ data_avg[1]['Zn'], data_avg[2]['Zn'], data_avg[3]['Zn'], data_avg[4]['Zn'], data_avg[5]['Zn'] ]
y_cd = [ data_avg[1]['Cd'], data_avg[2]['Cd'], data_avg[3]['Cd'], data_avg[4]['Cd'], data_avg[5]['Cd'] ]
y_pb = [ data_avg[1]['Pb'], data_avg[2]['Pb'], data_avg[3]['Pb'], data_avg[4]['Pb'], data_avg[5]['Pb'] ]


# Finagling setup to get text x labels.
# http://stackoverflow.com/questions/11244514/modify-tick-label-text
fig, ax = plt.subplots()
fig.canvas.draw()


# Set auxiliary plot details, ex: title, labels, etc.
# http://stackoverflow.com/questions/12444716/how-do-i-set-the-figure-title-and-axes-labels-font-size-in-matplotlib
title_size = 20
label_size = title_size * 0.75

x_labels = ['Ore', '', 'Settling', '', 'Chat Piles', '', 'Wetland Cores', '', 'Floodplains']
ax.set_xticklabels(x_labels)


plt.legend()
plt.xlabel('Location', fontsize=label_size)
plt.ylabel('Concentration', fontsize=label_size)
plt.title('Location v. Heavy Metal Concentrations', fontsize=title_size)

# Plot
plt.plot(x, y_zn, label='[Zn]')
plt.plot(x, y_cd, label='[Cd]')
plt.plot(x, y_pb, label='[Pb]')
# Show plot
plt.show()