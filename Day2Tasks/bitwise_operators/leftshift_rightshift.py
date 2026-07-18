# Q4 : Write a program to perform left shift (<<) and right shift (>>) operations on a number
n = int(input("Enter the value :"))
left_shift = n << 1
right_shift = n >> 1
print("left shift:", left_shift)
print("right shift:", right_shift)

# take 6 as input
# left shift means << 1 every bit is shifted to left by 1 position and 0 is added
# 6 - 0110 -original number
#     1100 - after left shift =12
# right shift means >> 1 every bit is shifted to right by 1 position and 0 is added
# 6 - 0110 - original number
#     0011 - after right shift =3