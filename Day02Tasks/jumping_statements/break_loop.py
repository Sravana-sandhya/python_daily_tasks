# Q4 : Write a program that searches for a number in a list and breaks the loop when found.
num = [10,20,5,6,30,8,60]
search_num = 6
for i in num:
    if i == search_num:
       print("number found:", i)
       break