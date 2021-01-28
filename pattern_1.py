n = int(input("Enter any number:"))
for i in range(n):
    print("* " * 5, end="\n")

# Enter any number:5
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

n = int(input("Enter any number:"))
for i in range(n):
    print("* " * (i + 1))

# Enter any number:5
# *
# * *
# * * *
# * * * *
# * * * * *


n = int(input("Enter a number :"))
for i in range(n):
  for j in range(n):
    print(n-j, end= " ")
  print()

# Enter any number:5
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1


n = int(input("Enter a number :"))
for i in range(n):
  for j in range(i+1):
    print(j+1, end = " ")
  print()

# Enter any number:5
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
