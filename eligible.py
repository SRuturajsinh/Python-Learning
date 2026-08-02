"""
This program calculates a student's grade based on their marks in different subjects,
using an if-elif-else chain.
"""

# --- User Input ---
student = input("Enter student name: ")
print(f"\nHello, {student}. Please enter the marks for the following subjects (out of 100).")

# Get marks for each subject and convert the input string to an integer.
maths = int(input("Enter Maths Marks: "))
science = int(input("Enter Science Marks: "))
english = int(input("Enter English Marks: "))

if (maths<0 or maths>100 or 
    science<0 or science>100 or 
    english<0 or english>100):

    print("Please Enter Valid Marks.")
    exit() # It will end the program here.

# --- Calculation ---
# Calculate the average score.
average = (maths + science + english) / 3

# --- Grading Logic using if-elif-else chain ---
# The program checks each condition from top to bottom and runs the code
# for the first one that is True.
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F (Fail)"

# --- Output ---
print(f"\n--- {student}'s Report Card ---")
print(f"Average Score: {average:.2f}%") # if your average is in float than by .2f we take only 2 digit after point
print(f"Final Grade: {grade}")
