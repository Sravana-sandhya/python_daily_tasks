#Q9 : Smart Data Processing Pipeline 
# Scenario: 
# A system processes numeric data from file. 
# Task: 
# ● Read numbers from a file 
# ● Use NumPy for calculations (mean, std) 
# ● Convert results to Pandas DataFrame 
# ● Use exception handling for bad data 
# ● Use a generator to stream data 
# ● Apply decorator to measure execution time 
import numpy as np
import pandas as pd
import time
def execution_time(function):
    def wrapper():
        start = time.time()
        function()
        end = time.time()
        print("Execution time:", end - start, "seconds")
    return wrapper
def read_numbers():
    file = open("numbers.txt", "r")
    for line in file:
        try:
            number = float(line)
            yield number
        except ValueError:
            print("Bad data found:", line)
    file.close()
@execution_time
def process_data():
    numbers = []
    for number in read_numbers():
        numbers.append(number)
    print("Numbers:", numbers)
    arr = np.array(numbers)
    mean_value = np.mean(arr)
    std_value = np.std(arr)
    print("Mean:", mean_value)
    print("Standard Deviation:", std_value)
    df = pd.DataFrame({
        "Mean": [mean_value],
        "Standard Deviation": [std_value]
    })
    print(df)
process_data()