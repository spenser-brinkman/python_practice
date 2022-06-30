try:
  pointspossible = int(input("Enter the total points possible:\n"))
except Exception:
  print("Please provide a valid number")

studentname = input("Please enter the student's name:\n")
score = input(f"Please enter the number of points earned by {studentname}:\n")
grade = score / pointspossible

# A: 100-90
# B: 89-80
# C: 79-70
# D: 69-60
# F: 59-0

if 1 >= grade >= 0.9:
  print("{} received an A".format(studentname))
elif 0.89 >= grade >= 0.9:
  print("{} received a B".format(studentname))
elif 0.79 >= grade >= 0.7:
  print("{} received a C".format(studentname))
elif 0.69 >= grade >= 0.6:
  print("{} received a D".format(studentname))
else:
  print("{} received an F".format(studentname))
