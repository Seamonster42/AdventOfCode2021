import numpy as np
#This function checks each first, second, etc of the input
#If the most common bit is 1, then the gamma factor will have a 1 on that bit
#If the most common bit is 0, then the gamma factor will have a 0 on that bit
#The epsilon factor is defined similarly
#If the most common bit is 1, then the gamma factor will have a 0 on that bit
#If the most common bit is 0, then the gamma factor will have a 1 on that bit
#This means that the gamma and epsilon factor should sum up to 2**bitsize - 1
#diagnostics_data should be a dataframe with the following layout
#index binary_value
#0     00100
#1     11110
#2     10110
def determine_power_consumption(diagnostics_data):
    gamma = 0
    epsilon = 0
    bit_size = len(diagnostics_data.loc[0, 'binary_value'])
    for b in range(bit_size):
        count_bit_is_zero = 0
        count_bit_is_one = 0
        for i in diagnostics_data.index:
            bit = diagnostics_data.loc[i, 'binary_value']
            if bit[b] == '0':
                count_bit_is_zero += 1
            elif bit[b] == '1':
                count_bit_is_one += 1
        if count_bit_is_zero < count_bit_is_one:
            gamma += pow(2, 5-b-1)
        elif count_bit_is_zero > count_bit_is_one:
            epsilon += pow(2, 5-b-1)
    #print(gamma)
    #print(epsilon)
    print('The sum of the gamma and epsilon factor is ' + str(gamma+epsilon) + ' and the bitsize allowed for a max value of ' + str(pow(2, bit_size)-1))
    return gamma * epsilon