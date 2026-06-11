# Student Grade Report: 
# Given a list of marks for 5 subjects, calculate total, percentage, and assign a grade (A/B/C/D/F). 
# Print a report card. Bonus: flag if the student failed any single subject. 

# marks = [90,88,91,95,99]
marks = []
for i in range (5):
    mark = int(input(f"Enter your mark for  subject {i+1} : "))

    if 0 <= mark <= 100:
        marks.append(mark)
    else:
        print("Invalid mark")
        exit()
    
total = sum(marks)
length = len(marks)

percentage = total / length

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

# Check for failed subjects (<35)
# failed = any(mark < 35 for mark in marks)

failed = False
for mark in marks:
    if mark < 35:
        failed = True
        break

print("\n -----REPORT CARD----- \n")
print("Marks:",marks)
print("Total:",total)
print(f"Percentage:{percentage :.2f}%")
print("Grade:",grade)

if failed:
    print("Result:FAIL")
else:
    print("Result:PASS")




