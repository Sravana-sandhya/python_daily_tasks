#Q4 : Basic File Logger 
# Scenario: 
# A system logs user actions. 
# Task: 
# ● Take user input 
# ● Store logs in a file 
# ● Use loop to allow multiple entries 
# ● Handle file errors using exception handling 
try:
  file = open("user_logs.txt","a")
  for i in range(5):
    action = input("Enter user action:")
    file.write(action + "\n")
  file.close()
  print("Logs saved Successfully")
except:
  print("Error in file handling")
  