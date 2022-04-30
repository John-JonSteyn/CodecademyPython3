# CodeCademy Python 3 Course
# Project 05: Gradebook
# Lists

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Declare subjects & grades
subjects = ["physiscs", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Combine subjects & grades
gradebook = [
  [subjects[0], grades[0]],
  [subjects[1], grades[1]],
  [subjects[2], grades[2]],
  [subjects[3], grades[3]],
]

# Append subjects & grades
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Modify visual arts += 5
adjustment = gradebook[-1][-1]
adjustment += 5
gradebook[-1][-1] = [adjustment]

# Remove poetry
gradebook.remove(["poetry", 85])

# Append poetry
gradebook.append(["poetry", "pass"])

# Concat gradebooks
full_gradebook = last_semester_gradebook + gradebook

# Print gradebook
print(full_gradebook)