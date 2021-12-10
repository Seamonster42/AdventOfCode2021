#dive_data should be a dataframe with the following layout
#index direction value
#0     forward   5
#1     down      5
#2     forward   8
#3     up        3
def determine_distance_depth(dive_data):
    distance = 0
    depth = 0
    for i in dive_data.index:
        if dive_data.loc[i, 'direction'] == 'forward':
            distance += dive_data.loc[i, 'value']
        elif dive_data.loc[i, 'direction'] == 'down':
            depth += dive_data.loc[i, 'value']
        elif dive_data.loc[i, 'direction'] == 'up':
            depth += -dive_data.loc[i, 'value']
    return distance * depth
