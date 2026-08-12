# Q7 : Generator-based Log Reader 
# Scenario: 
# A large log file needs to be processed. 
# Task: 
# ● Create a generator to read file line by line 
# ● Use loop to process logs 
# ● Use condition to filter errors 
# ● Count occurrences using a dictionary
def read_logs():
    file = open("log.txt", "r")
    for line in file:
        yield line
    file.close()
errors = {}
for line in read_logs():
    if "ERROR" in line:
        error = line.replace("ERROR: ", "").strip()
        if error in errors:
            errors[error] += 1
        else:
            errors[error] = 1
print("Error Occurrences:")
for error, count in errors.items():
    print(error, ":", count)