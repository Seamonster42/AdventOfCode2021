import pandas as pd
import sonar_sweep
import dive
import binary_diagnostics

###Day 1###
path_to_file = './inputs/sonar_sweep_input.txt'
df_depth_data = pd.read_csv(path_to_file, header=None, names=['depth_measurement'], dtype=float)
#print(df_depth_data)
print(sonar_sweep.count_increasing_depth(df_depth_data, False))

###Day 2###
path_to_file = './inputs/dive_input.txt'
df_dive_data = pd.read_csv(path_to_file, header=None, delimiter=' ', names=['direction', 'value'], dtype={'direction': str, 'value': float})
#print(df_dive_data)
print(dive.determine_distance_depth(df_dive_data))

###Day 3###
path_to_file = './inputs/binary_diagnostics_input.txt'
df_diagnostics_data = pd.read_csv(path_to_file, header=None, names=['binary_value'], dtype=str)
#print(df_diagnostics_data)
print(binary_diagnostics.determine_power_consumption(df_diagnostics_data))