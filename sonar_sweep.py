import numpy as np
import pandas as pd


# Count number of depth measurement increases by comparing each value with the previous one
# There is no measurement before the first measurement, so this can not contribute
# The boolean create_output_file will print the output file at the end of the function
#depth_data should be a dataframe with the following layout
#index depth_measurement
#0     199.0
#1     200.0
#2     208.0
#3     210.0
def count_increasing_depth(depth_data, create_output_file):
    times_depth_measurements_increases = 0
    output = []
    for i in depth_data.index:
        if i == 0 or depth_data.loc[i - 1, 'depth_measurement'] == '':
            output.append("(N/A - no previous measurement)")
        elif depth_data.loc[i, 'depth_measurement'] > depth_data.loc[i - 1, 'depth_measurement']:
            times_depth_measurements_increases += 1
            output.append('(increased)')
        elif depth_data.loc[i, 'depth_measurement'] < depth_data.loc[i - 1, 'depth_measurement']:
            output.append('(decreased)')
        elif depth_data.loc[i, 'depth_measurement'] == depth_data.loc[i - 1, 'depth_measurement']:
            output.append('(No increase or decrease in depth)')
    if create_output_file:
        print(output)
    return times_depth_measurements_increases
